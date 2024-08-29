from meupacote import cadastrar_alunos, adicionar_notas
from graficos import visualizar_notas as visualizar_notas_graficos, visualizar_notas_por_materia

def main():
    while True:
        print("\nMenu IBMEC")
        print("1. Cadastrar aluno")
        print("2. Adicionar nota")
        print("3. Visualizar nota")
        print("4. Ver notas dos alunos por matéria")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_alunos()
        elif escolha == '2':
            adicionar_notas()
        elif escolha == '3':
            matricula = input("Digite a matrícula do aluno para visualizar as notas: ")
            visualizar_notas_graficos(matricula)
        elif escolha == '4':
            visualizar_notas_por_materia()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
