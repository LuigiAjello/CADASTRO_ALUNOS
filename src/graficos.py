import matplotlib.pyplot as plt
import pandas as pd
from meupacote import carregar_dados

def visualizar_notas(matricula):
    df_alunos, df_disciplinas, df_notas = carregar_dados()
    
    notas_do_aluno = df_notas[df_notas['Matrícula'] == matricula]
    
    if notas_do_aluno.empty:
        print(f"O aluno de matrícula {matricula} não possui notas cadastradas.")
        return
    
    disciplinas = notas_do_aluno['Disciplina']
    notas = notas_do_aluno['Nota']
    
    plt.figure(figsize=(10, 6))
    plt.bar(disciplinas, notas, color='skyblue')
    plt.xlabel('Disciplinas')
    plt.ylabel('Notas')
    plt.title(f'Notas do aluno de matrícula {matricula}')
    plt.xticks(rotation=45)
    plt.ylim(0, 10)  # Ajustar o limite do eixo Y para a escala de notas
    plt.tight_layout()
    plt.show()

def visualizar_notas_por_materia():
    df_alunos, df_disciplinas, df_notas = carregar_dados()

    if df_alunos.empty:
        print("Nenhum aluno cadastrado.")
        return

    while True:
        print("\nMatérias disponíveis:")
        disciplinas_unicas = df_disciplinas['Disciplina'].unique()
        disciplinas_unicas = [disciplina for disciplina in disciplinas_unicas if disciplina != 'Matéria vaga']
        
        for i, disciplina in enumerate(disciplinas_unicas, 1):
            print(f"{i}. {disciplina}")

        try:
            escolha = int(input(f"Escolha a matéria para visualizar as notas (1-{len(disciplinas_unicas)}): "))
            if 1 <= escolha <= len(disciplinas_unicas):
                disciplina = disciplinas_unicas[escolha - 1]
                notas_por_disciplina = df_notas[df_notas['Disciplina'] == disciplina]
                
                if notas_por_disciplina.empty:
                    print(f"Nenhum aluno tem nota cadastrada para a matéria '{disciplina}'.")
                    return
                
                plt.figure(figsize=(12, 6))
                cores = ['green' if nota >= 7 else 'red' for nota in notas_por_disciplina['Nota']]
                plt.bar(notas_por_disciplina['Matrícula'], notas_por_disciplina['Nota'], color=cores)
                plt.xlabel('Nome do Aluno')
                plt.ylabel('Nota')
                plt.title(f'Notas dos alunos para a matéria {disciplina}')
                plt.xticks(rotation=90)
                plt.ylim(0, 10)  # Ajustar o limite do eixo Y para a escala de notas
                plt.tight_layout()
                plt.show()
                
                break
            else:
                print(f"Escolha inválida. Por favor, selecione um número entre 1 e {len(disciplinas_unicas)}.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

