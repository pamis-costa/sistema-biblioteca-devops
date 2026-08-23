from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "disponivel": True}
]

@app.get("/")
def inicio():
    return jsonify({"mensagem": "Sistema de Biblioteca funcionando!"})

@app.get("/livros")
def listar_livros():
    return jsonify(livros)

@app.post("/livros")
def cadastrar_livro():
    dados = request.get_json(silent=True) or {}
    titulo = dados.get("titulo")
    autor = dados.get("autor")

    if not titulo or not autor:
        return jsonify({"erro": "titulo e autor são obrigatórios"}), 400

    novo_id = max([livro["id"] for livro in livros], default=0) + 1
    livro = {
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    }
    livros.append(livro)
    return jsonify(livro), 201

@app.put("/livros/<int:livro_id>/emprestar")
def emprestar_livro(livro_id):
    livro = next((l for l in livros if l["id"] == livro_id), None)

    if not livro:
        return jsonify({"erro": "livro não encontrado"}), 404

    if not livro["disponivel"]:
        return jsonify({"erro": "livro já está emprestado"}), 400

    livro["disponivel"] = False
    return jsonify(livro)

@app.put("/livros/<int:livro_id>/devolver")
def devolver_livro(livro_id):
    livro = next((l for l in livros if l["id"] == livro_id), None)

    if not livro:
        return jsonify({"erro": "livro não encontrado"}), 404

    livro["disponivel"] = True
    return jsonify(livro)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
