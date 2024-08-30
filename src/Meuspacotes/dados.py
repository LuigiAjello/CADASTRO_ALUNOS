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
