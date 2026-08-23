import pytest
from app import app, livros

@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    livros.clear()
    livros.append({
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "disponivel": True
    })
    with app.test_client() as cliente:
        yield cliente

def test_pagina_inicial(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200

def test_listar_livros(cliente):
    resposta = cliente.get("/livros")
    assert resposta.status_code == 200
    assert len(resposta.get_json()) == 1

def test_cadastrar_livro(cliente):
    resposta = cliente.post("/livros", json={
        "titulo": "O Cortiço",
        "autor": "Aluísio Azevedo"
    })
    assert resposta.status_code == 201
    assert resposta.get_json()["titulo"] == "O Cortiço"

def test_cadastro_sem_dados_obrigatorios(cliente):
    resposta = cliente.post("/livros", json={"titulo": "Livro sem autor"})
    assert resposta.status_code == 400

def test_emprestar_livro(cliente):
    resposta = cliente.put("/livros/1/emprestar")
    assert resposta.status_code == 200
    assert resposta.get_json()["disponivel"] is False

def test_nao_permitir_emprestimo_duplo(cliente):
    cliente.put("/livros/1/emprestar")
    resposta = cliente.put("/livros/1/emprestar")
    assert resposta.status_code == 400

def test_devolver_livro(cliente):
    cliente.put("/livros/1/emprestar")
    resposta = cliente.put("/livros/1/devolver")
    assert resposta.status_code == 200
    assert resposta.get_json()["disponivel"] is True

def test_livro_inexistente(cliente):
    resposta = cliente.put("/livros/999/emprestar")
    assert resposta.status_code == 404
