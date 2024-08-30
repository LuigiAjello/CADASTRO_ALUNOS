from Meuspacotes.dados import carregar_dados, salvar_dados
import pandas as pd

def verificar_matricula_existente(df_alunos, matricula):
    matricula = str(matricula).strip()
    return not df_alunos[df_alunos['Matrícula'] == matricula].empty

def listar_matriculas(df_alunos):
    print("\nMatrículas cadastradas:")
    for _, row in df_alunos.iterrows():
        print(f"Matrícula: {row['Matrícula']}, Nome: {row['Nome']}, Semestre: {row['Semestre']}")

def cadastrar_alunos():
    df_alunos, df_disciplinas, df_notas = carregar_dados()

    materias_disponiveis = [
        "Pensamento Computacional",
        "Programação Estruturada",
        "Matemática Discreta",
        "Álgebra Linear",
        "Cálculo 1",
        "Cálculo 2",
        "Métodos Ágeis de Desenvolvimento de Software",
        "Desenvolvimento Web",
        "Projeto Aplicado de Ciências de Dados",
        "Design",
        "Matéria vaga"
    ]

    while True:
        listar_matriculas(df_alunos)
        matricula = input("Digite a matrícula: ")
        
        if verificar_matricula_existente(df_alunos, matricula):
            print("Matrícula já cadastrada. Tente novamente.")
            resposta = input("Deseja tentar novamente? (s/n): ").lower()
            if resposta != 's':
                return  # Volta ao menu principal
            continue
        
        nome = input("Digite o nome: ")
        semestre = input("Digite o semestre: ")
        email = input("Digite o e-mail: ")  # Solicita o e-mail do aluno

        materias_selecionadas = []

        print("\nMatérias disponíveis:")
        for i, materia in enumerate(materias_disponiveis, 1):
            print(f"{i}. {materia}")

        for i in range(5):
            while True:
                try:
                    escolha = input(f"\nEscolha a matéria {i+1} (1-{len(materias_disponiveis)}, ou 0 para pular): ")
                    if escolha == '0':
                        materias_selecionadas.append("Matéria vaga")
                        break
                    escolha = int(escolha)
                    if 1 <= escolha <= len(materias_disponiveis):
                        materia_selecionada = materias_disponiveis[escolha - 1]
                        materias_selecionadas.append(materia_selecionada)
                        break
                    else:
                        print(f"Escolha inválida. Por favor, selecione um número entre 1 e {len(materias_disponiveis)}.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")
        
        # Inclui o e-mail no cadastro do aluno
        novo_aluno = pd.DataFrame([{'Matrícula': matricula, 'Nome': nome, 'Semestre': semestre, 'email': email}])
        df_alunos = pd.concat([df_alunos, novo_aluno], ignore_index=True)
        
        for materia in materias_selecionadas:
            nova_disciplina = pd.DataFrame([{'Matrícula': matricula, 'Disciplina': materia}])
            df_disciplinas = pd.concat([df_disciplinas, nova_disciplina], ignore_index=True)
        
        salvar_dados(df_alunos, df_disciplinas, df_notas)
        
        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

def editar_aluno():
    df_alunos, df_disciplinas, df_notas = carregar_dados()

    if df_alunos.empty:
        print("Nenhum aluno cadastrado.")
        return

    listar_matriculas(df_alunos)
    matricula = input("Digite a matrícula do aluno que deseja editar: ")

    if not verificar_matricula_existente(df_alunos, matricula):
        print("Matrícula não encontrada.")
        return
    
    aluno_index = df_alunos[df_alunos['Matrícula'] == matricula].index[0]
    aluno_nome = df_alunos.at[aluno_index, 'Nome']
    aluno_semestre = df_alunos.at[aluno_index, 'Semestre']
    aluno_email = df_alunos.at[aluno_index, 'email']

    print(f"\nEditando informações do aluno: {aluno_nome} (Matrícula: {matricula})")
    
    nome = input(f"Digite o novo nome (ou pressione Enter para manter '{aluno_nome}'): ")
    semestre = input(f"Digite o novo semestre (ou pressione Enter para manter '{aluno_semestre}'): ")
    email = input(f"Digite o novo e-mail (ou pressione Enter para manter '{aluno_email}'): ")

    if nome:
        df_alunos.at[aluno_index, 'Nome'] = nome
    if semestre:
        df_alunos.at[aluno_index, 'Semestre'] = semestre
    if email:
        df_alunos.at[aluno_index, 'email'] = email

    salvar_dados(df_alunos, df_disciplinas, df_notas)

    print(f"As informações do aluno {matricula} foram atualizadas com sucesso.")
