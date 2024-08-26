# GetServices

Projeto Django que facilita a busca e o contrato de serviços de profissionais autônomos

## Requisitos do projeto

### Requisitos funcionais

#### Visitante

- [ ] Deve ser possível listar os funcionários;
- [ ] Deve ser possível visualizar a profissão do funcionário;
- [ ] Deve ser possível visualizar a pontuação do funcionário;
- [ ] Deve ser possível se cadastrar como um cliente;
- [ ] Deve ser possível listar os horários disponíveis de um funcionário;

#### Cliente

- [ ] Deve ser possível fazer um agendamento;
- [ ] Deve ser possível visualizar os agendamentos feitos;

#### Funcionário

- [ ] Deve ser possível cadastrar um horário;
- [ ] Deve ser possível listar os horários cadastrados;
- [ ] Deve ser possível ver o histórico de agendamentos;
- [ ] Deve ser possível marcar um agendamento como concluído;
- [ ] Deve ser possível marcar um agendamento como cancelado;

## Requisitos

- Python 3.*
- Docker e Docker Compose
- Git

## Instalação

- Clone o repositório; ```git clone https://github.com/JoaoManoelFontes/getServices.git```
- Crie um arquivo .env com o mesmo conteúdo do arquivo .env.example e modifique as variáveis de acordo com suas informações; ```cp .env.example .env```
- Execute o comando; ```docker-compose up -d```
- Crie uma virtualenv; ```python -m venv venv``` e ative-a; ```source venv/bin/activate```
- Instale as dependências; ```pip install -r requirements.txt```
- Execute as migrações; ```python manage.py migrate```
- Rode o servidor; ```python manage.py runserver```

## Ambiente de desenvolvimento

- Usar o [Git Flow](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow) para o versionamento do código.
- Usar o [Ruff](https://docs.astral.sh/ruff/) para a linter e formatter do código. (```ruff check``` e ```ruff format```)
- Usar a extensão do ruff no VSCode para facilitar o uso.
