# Sistema de Biblioteca - DevOps na Prática

Projeto da Fase 1 e Fase 2 da disciplina DevOps na Prática.

## Objetivo

Criar uma aplicação simples de biblioteca e aplicar práticas de DevOps:
- Integração contínua com GitHub Actions;
- Testes automatizados com pytest;
- Infraestrutura como código com Terraform;
- Containerização da aplicação com Docker;
- Orquestração local de containers com Docker Compose;
- Entrega Contínua (CD) automatizando o build da imagem Docker.

## Funcionalidades

- Listar livros;
- Cadastrar livros;
- Emprestar livros;
- Devolver livros;
- Validar dados obrigatórios.

## Executar com Docker

Certifique-se de que o Docker Desktop está em execução e digite no terminal:

```bash
docker-compose up -d --build
```

A aplicação ficará disponível em `http://localhost:5000`. 
Para parar a aplicação e remover o container, execute: `docker-compose down`

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

## CI/CD Pipeline

O workflow `.github/workflows/ci.yml` executa os testes automaticamente em pushes e pull requests para a branch `main`. 

Para a Fase 2, o pipeline foi expandido (CD), realizando o build automático da imagem Docker logo após a aprovação nos testes, garantindo que o artefato final seja gerado a cada nova atualização do código.

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
