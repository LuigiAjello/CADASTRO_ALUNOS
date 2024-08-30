# Sistema de Cadastro e Notas de Alunos - IBMEC

Este projeto consiste em um sistema para gerenciar o cadastro de alunos, disciplinas e notas, com funcionalidades adicionais de visualização de gráficos e envio de emails com relatórios de notas.

## Funcionalidades

### Cadastro de Alunos:
- Permite o cadastro de novos alunos, incluindo informações como matrícula, nome, semestre e email.
- Verifica se a matrícula já está cadastrada.

### Cadastro de Disciplinas:
- Permite a escolha de até 5 disciplinas para cada aluno.

### Registro de Notas:
- Permite o registro das notas para as disciplinas cadastradas para cada aluno.
- Atualiza o status de aprovação baseado na nota (Aprovado/Reprovado).

### Visualização de Notas:
- Gera gráficos de barras das notas de um aluno específico.
- Gera gráficos com as notas de todos os alunos em uma disciplina específica.

### Envio de Emails:
- Envia um email para o aluno com um relatório das suas notas e um gráfico de desempenho em anexo.

## Estrutura do Projeto
- **main.py**: Arquivo principal que contém o menu interativo e a lógica principal do programa.
- **alunos.py**: Contém as funções relacionadas ao cadastro e gerenciamento de alunos.
- **notas.py**: Contém as funções para adicionar e gerenciar notas.
- **visualizacao.py**: Contém as funções para gerar e exibir gráficos das notas.
- **dados.py**: Contém as funções para carregar e salvar os dados no arquivo Excel.
- **cadastroalunos.xlsx**: Arquivo Excel utilizado como "banco de dados" para armazenar as informações dos alunos, disciplinas e notas.

## Requisitos
- Python 3.x
- Bibliotecas Python:
  - pandas
  - openpyxl
  - matplotlib
  - smtplib (para envio de emails)
  - os e dotenv (para gerenciar variáveis de ambiente)

## Como Usar

### Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositori

#Instalar as Dependências
pip install -r requirements.txt


###Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
YAHOO_USER="seu_email@yahoo.com"
YAHOO_PASSWORD="sua_senha_de_aplicativo"


#Nota: No Yahoo, é necessário gerar uma senha de aplicativo para permitir que o script envie emails

