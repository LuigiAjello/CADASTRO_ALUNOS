def cadastrar_alunos():
    cadastros = []

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
        matricula = input("Digite a matrícula: ")
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

        cadastro_aluno = {
            "Matrícula": matricula,
            "Nome": nome,
            "Semestre": semestre,
            "Matérias": materias_selecionadas,
            "Notas": {}  # Inicializa a chave 'Notas' como um dicionário vazio
        }

        cadastros.append(cadastro_aluno)

        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

    return cadastros

def listar_alunos(cadastros):
    print("\nAlunos cadastrados:")
    for aluno in cadastros:
        print(f"Matrícula: {aluno['Matrícula']}, Nome: {aluno['Nome']}")

def adicionar_notas(cadastros):
    if not cadastros:
        print("Nenhum aluno cadastrado.")
        return

    listar_alunos(cadastros)  # Mostrar a lista de alunos
    matricula = input("Digite a matrícula do aluno para adicionar nota: ")
    aluno = next((a for a in cadastros if a["Matrícula"] == matricula), None)

    if aluno is None:
        print("Matrícula não encontrada.")
        return

    print(f"Matérias do aluno {aluno['Nome']}:")
    for i, materia in enumerate(aluno["Matérias"], 1):
        print(f"{i}. {materia}")

    while True:
        try:
            escolha = int(input("Escolha a matéria para adicionar a nota (1-{len(aluno['Matérias'])}): "))
            if 1 <= escolha <= len(aluno["Matérias"]):
                materia = aluno["Matérias"][escolha - 1]
                nota = input(f"Digite a nota para a matéria '{materia}': ")
                aluno["Notas"][materia] = nota
                print(f"Nota adicionada para {materia}.")
                break
            else:
                print(f"Escolha inválida. Por favor, selecione um número entre 1 e {len(aluno['Matérias'])}.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def visualizar_notas(cadastros):
    if not cadastros:
        print("Nenhum aluno cadastrado.")
        return

    listar_alunos(cadastros)  # Mostrar a lista de alunos
    matricula = input("Digite a matrícula do aluno para visualizar as notas: ")
    aluno = next((a for a in cadastros if a["Matrícula"] == matricula), None)

    if aluno is None:
        print("Matrícula não encontrada.")
        return

    print(f"Notas do aluno {aluno['Nome']}:")
    for materia, nota in aluno.get("Notas", {}).items():
        print(f"{materia}: {nota}")
