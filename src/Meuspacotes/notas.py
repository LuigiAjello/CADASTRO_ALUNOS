from Meuspacotes.dados import carregar_dados, salvar_dados
from Meuspacotes.alunos import listar_matriculas, verificar_matricula_existente
from Meuspacotes.visualizacao import visualizar_notas  # Importar a função visualização
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

YAHOO_USER = os.getenv("YAHOO_USER")
YAHOO_PASSWORD = os.getenv("YAHOO_PASSWORD")

def enviar_email(usuario, senha, destinatario, assunto, mensagem, anexo=None):
    servidor_smtp = 'smtp.mail.yahoo.com'
    porta = 587

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))

    if anexo:
        with open(anexo, 'rb') as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(anexo))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(anexo)}"'
            msg.attach(part)

    servidor = smtplib.SMTP(servidor_smtp, porta)
    servidor.starttls()

    servidor.login(usuario, senha)

    servidor.sendmail(usuario, destinatario, msg.as_string())

    servidor.quit()

def adicionar_notas():
    df_alunos, df_disciplinas, df_notas = carregar_dados()
    
    if df_alunos.empty:
        print("Nenhum aluno cadastrado.")
        return

    while True:
        listar_matriculas(df_alunos)
        matricula = input("Digite a matrícula do aluno para adicionar nota: ")
        aluno_existe = verificar_matricula_existente(df_alunos, matricula)
        
        if not aluno_existe:
            resposta = input("Matrícula não encontrada. Deseja tentar novamente? (s/n): ").lower()
            if resposta != 's':
                return
            continue

        aluno_nome = df_alunos[df_alunos['Matrícula'] == matricula]['Nome'].values[0]
        email_aluno = df_alunos[df_alunos['Matrícula'] == matricula]['email'].values[0]  # Obter o email do aluno
        
        disciplinas_do_aluno = df_disciplinas[df_disciplinas['Matrícula'] == matricula]['Disciplina'].tolist()
        
        if not disciplinas_do_aluno:
            print("O aluno não está matriculado em nenhuma disciplina.")
            return

        notas_preenchidas = 0  # Contador de notas preenchidas
        notas = []

        for i, disciplina in enumerate(disciplinas_do_aluno, 1):
            print(f"{i}. {disciplina}")

        while notas_preenchidas < 5:
            try:
                escolha = int(input(f"Escolha a disciplina para adicionar a nota (1-{len(disciplinas_do_aluno)}): "))
                if 1 <= escolha <= len(disciplinas_do_aluno):
                    disciplina = disciplinas_do_aluno[escolha - 1]
                    if disciplina == "Matéria vaga":
                        print("Não é possível adicionar nota para 'Matéria vaga'.")
                        return  # Volta ao menu

                    while True:
                        try:
                            nota = float(input(f"Digite a nota para a disciplina '{disciplina}': "))
                            aprovacao = 'Aprovado' if nota >= 7 else 'Reprovado'
                            nova_nota = pd.DataFrame([{
                                'Matrícula': matricula, 
                                'Disciplina': disciplina, 
                                'Nota': nota,
                                'Aprovação': aprovacao
                            }])

                            nova_nota = nova_nota.dropna(how='all')

                            if not nova_nota.empty:
                                df_notas = pd.concat([df_notas, nova_nota], ignore_index=True)
                                print(f"Nota adicionada para {disciplina}. {aprovacao}.")
                                notas_preenchidas += 1
                                notas.append((disciplina, nota, aprovacao))

                                salvar_dados(df_alunos, df_disciplinas, df_notas)

                            if notas_preenchidas == 5:
                                # Montar a mensagem para o e-mail
                                mensagem = f"""
Faculdade IBMEC

Prezado(a) {aluno_nome},

Segue abaixo o resumo das suas notas nas disciplinas cursadas:

Matérias e Notas:
"""
                                for disciplina, nota, aprovacao in notas:
                                    mensagem += f"{disciplina}: Nota {nota} - {aprovacao}\n"

                                mensagem += "\nAbaixo, você pode visualizar um gráfico com suas notas:\n"

                                # Gerar o gráfico usando a função existente
                                grafico_path = f'grafico_{matricula}.png'
                                visualizar_notas(matricula, salvar_grafico=True, caminho_grafico=grafico_path)

                                # Enviar o e-mail com o gráfico em anexo
                                enviar_email(YAHOO_USER, YAHOO_PASSWORD, email_aluno, 
                                             'Notas do Aluno', mensagem, anexo=grafico_path)
                                print(f"E-mail enviado com sucesso para {email_aluno}.")

                                # Remover o gráfico salvo após o envio do e-mail
                                os.remove(grafico_path)

                            return  # Volta para o menu principal após adicionar a nota
                        except ValueError:
                            print("Nota inválida. Por favor, insira um número.")
                else:
                    print(f"Escolha inválida. Por favor, selecione um número entre 1 e {len(disciplinas_do_aluno)}.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
