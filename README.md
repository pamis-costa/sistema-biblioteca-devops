# Sistema de Biblioteca - DevOps na Prática

Projeto da Fase 1 da disciplina DevOps na Prática.

## Objetivo

Criar uma aplicação simples de biblioteca e aplicar práticas de DevOps:
- Integração contínua com GitHub Actions;
- Testes automatizados com pytest;
- Infraestrutura como código com Terraform.

## Funcionalidades

- Listar livros;
- Cadastrar livros;
- Emprestar livros;
- Devolver livros;
- Validar dados obrigatórios.

## Executar localmente

```bash
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
pytest -q
```

Execute a aplicação:

```bash
python app.py
```

A aplicação ficará disponível em `http://localhost:5000`.

## CI

O workflow `.github/workflows/ci.yml` executa os testes automaticamente em pushes e pull requests para a branch `main`.

## IaC

A pasta `terraform/` contém os arquivos para provisionar um bucket S3 destinado ao armazenamento de artefatos do projeto.

Antes de aplicar a infraestrutura, configure suas credenciais AWS e copie `terraform.tfvars.example` para `terraform.tfvars`, informando um nome de bucket único.

Comandos:

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

Não é necessário executar `terraform apply` para a entrega se você não tiver uma conta AWS configurada.
