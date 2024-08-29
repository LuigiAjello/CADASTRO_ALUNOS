import pandas as pd

arquivo_excel = 'data/cadastroalunos.xlsx'

def carregar_dados():
    try:
        df_alunos = pd.read_excel(arquivo_excel, sheet_name='alunos', engine='openpyxl')
        df_disciplinas = pd.read_excel(arquivo_excel, sheet_name='disciplina', engine='openpyxl')
        df_notas = pd.read_excel(arquivo_excel, sheet_name='nota', engine='openpyxl')

        df_alunos['Matrícula'] = df_alunos['Matrícula'].astype(str).str.strip()
        df_disciplinas['Matrícula'] = df_disciplinas['Matrícula'].astype(str).str.strip()
        df_notas['Matrícula'] = df_notas['Matrícula'].astype(str).str.strip()

    except FileNotFoundError:
        raise FileNotFoundError("Arquivo Excel não encontrado. Certifique-se de que o arquivo está no caminho correto.")
    
    return df_alunos, df_disciplinas, df_notas

def salvar_dados(df_alunos, df_disciplinas, df_notas):
    with pd.ExcelWriter(arquivo_excel, engine='openpyxl') as writer:
        df_alunos.to_excel(writer, sheet_name='alunos', index=False)
        df_disciplinas.to_excel(writer, sheet_name='disciplina', index=False)
        df_notas.to_excel(writer, sheet_name='nota', index=False)

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
            continue
        
        nome = input("Digite o nome: ")
        semestre = input("Digite o semestre: ")

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
        
        novo_aluno = pd.DataFrame([{'Matrícula': matricula, 'Nome': nome, 'Semestre': semestre}])
        df_alunos = pd.concat([df_alunos, novo_aluno], ignore_index=True)
        
        for materia in materias_selecionadas:
            nova_disciplina = pd.DataFrame([{'Matrícula': matricula, 'Disciplina': materia}])
            df_disciplinas = pd.concat([df_disciplinas, nova_disciplina], ignore_index=True)
        
        salvar_dados(df_alunos, df_disciplinas, df_notas)
        
        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

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

        disciplinas_do_aluno = df_disciplinas[df_disciplinas['Matrícula'] == matricula]['Disciplina'].tolist()
        
        if not disciplinas_do_aluno:
            print("O aluno não está matriculado em nenhuma disciplina.")
            return

        for i, disciplina in enumerate(disciplinas_do_aluno, 1):
            print(f"{i}. {disciplina}")

        while True:
            try:
                escolha = int(input(f"Escolha a disciplina para adicionar a nota (1-{len(disciplinas_do_aluno)}): "))
                if 1 <= escolha <= len(disciplinas_do_aluno):
                    disciplina = disciplinas_do_aluno[escolha - 1]
                    if disciplina == "Matéria vaga":
                        print("Não é possível adicionar nota para 'Matéria vaga'.")
                        break
                    while True:
                        try:
                            nota = float(input(f"Digite a nota para a disciplina '{disciplina}': "))
                            nova_nota = pd.DataFrame([{'Matrícula': matricula, 'Disciplina': disciplina, 'Nota': nota}])

                            # Filtrar entradas vazias
                            nova_nota = nova_nota.dropna(how='all')

                            df_notas = pd.concat([df_notas, nova_nota], ignore_index=True)
                            print(f"Nota adicionada para {disciplina}.")
                            salvar_dados(df_alunos, df_disciplinas, df_notas)
                            break
                        except ValueError:
                            print("Nota inválida. Por favor, insira um número.")
                    break
                else:
                    print(f"Escolha inválida. Por favor, selecione um número entre 1 e {len(disciplinas_do_aluno)}.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

