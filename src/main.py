from Meuspacotes.alunos import cadastrar_alunos, listar_matriculas, editar_aluno
from Meuspacotes.notas import adicionar_notas
from Meuspacotes.visualizacao import visualizar_notas, visualizar_notas_por_materia
from Meuspacotes.dados import carregar_dados

def main():
    while True:
        print("\nMenu IBMEC")
        print("1. Cadastrar aluno")
        print("2. Adicionar nota")
        print("3. Editar aluno")
        print("4. Visualizar nota")
        print("5. Ver notas da turma por matéria")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_alunos()
        elif escolha == '2':
            adicionar_notas()
        elif escolha == '3':
            editar_aluno()  # Chama a função para editar aluno
        elif escolha == '4':
            df_alunos, _, _ = carregar_dados()
            listar_matriculas(df_alunos)
            matricula = input("Digite a matrícula do aluno para visualizar as notas: ")
            visualizar_notas(matricula)
        elif escolha == '5':
            visualizar_notas_por_materia()
        elif escolha == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
