from meupacote import cadastrar_alunos, adicionar_notas, visualizar_notas

def main():
    cadastros = []
    while True:
        print("\nMenu IBMEC")
        print("1. Cadastrar aluno")
        print("2. Adicionar nota")
        print("3. Visualizar nota")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastros.extend(cadastrar_alunos())
        elif escolha == '2':
            adicionar_notas(cadastros)
        elif escolha == '3':
            visualizar_notas(cadastros)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()
