import matplotlib.pyplot as plt
from Meuspacotes.dados import carregar_dados

def visualizar_notas(matricula, salvar_grafico=False, caminho_grafico=None):
    df_alunos, df_disciplinas, df_notas = carregar_dados()
    
    notas_do_aluno = df_notas[df_notas['Matrícula'] == matricula]
    
    if notas_do_aluno.empty:
        print(f"O aluno de matrícula {matricula} não possui notas cadastradas.")
        return
    
    aluno_nome = df_alunos[df_alunos['Matrícula'] == matricula]['Nome'].values[0]
    
    disciplinas = notas_do_aluno['Disciplina']
    notas = notas_do_aluno['Nota']
    aprovacoes = notas_do_aluno['Aprovação']
    
    print(f"\nNotas do aluno {aluno_nome} (Matrícula {matricula}):")
    for disciplina, nota, aprovacao in zip(disciplinas, notas, aprovacoes):
        print(f"{aluno_nome} ({disciplina}) NOTA: {nota} - {aprovacao}")
    
    plt.figure(figsize=(max(10, len(disciplinas) * 1.5), 7))
    
    bar_width = 0.5
    colors = ['#4CAF50' if nota >= 7 else '#F44336' for nota in notas]
    
    plt.bar(disciplinas, notas, color=colors, width=bar_width)
    
    plt.xlabel('Disciplinas', fontsize=12)
    plt.ylabel('Notas', fontsize=12)
    plt.title(f'Notas do aluno de matrícula {matricula}', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylim(0, 11)
    
    for i, v in enumerate(notas):
        plt.text(i, v + 0.1, f'{v:.1f}', ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    if salvar_grafico and caminho_grafico:
        plt.savefig(caminho_grafico)
        plt.close()
    else:
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
                
                print(f"\nNotas dos alunos para a matéria {disciplina}:")
                for matricula in notas_por_disciplina['Matrícula']:
                    aluno_nome = df_alunos[df_alunos['Matrícula'] == matricula]['Nome'].values[0]
                    nota = notas_por_disciplina[notas_por_disciplina['Matrícula'] == matricula]['Nota'].values[0]
                    print(f"{aluno_nome} ({disciplina}) NOTA: {nota}")
                
                plt.figure(figsize=(14, 8))
                
                bar_width = max(0.2, 0.8 / len(notas_por_disciplina))
                colors = ['#4CAF50' if nota >= 7 else '#F44336' for nota in notas_por_disciplina['Nota']]
                
                plt.bar(notas_por_disciplina['Matrícula'], notas_por_disciplina['Nota'], 
                        color=colors, width=bar_width)
                
                plt.xlabel('Matrícula do Aluno', fontsize=12)
                plt.ylabel('Nota', fontsize=12)
                plt.title(f'Notas dos alunos para a matéria {disciplina}', fontsize=14)
                plt.xticks(rotation=90, fontsize=10)
                plt.yticks(fontsize=10)
                plt.ylim(0, 11)  # Ajusta o limite do eixo Y para 11
                
                for i, v in enumerate(notas_por_disciplina['Nota']):
                    plt.text(i, v + 0.1, f'{v:.1f}', ha='center', va='bottom', fontsize=10)
                
                plt.tight_layout()
                plt.grid(axis='y', linestyle='--', alpha=0.7)
                plt.show()
                
                break
            else:
                print(f"Escolha inválida. Por favor, selecione um número entre 1 e {len(disciplinas_unicas)}.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
