from flask import Flask, request, jsonify

app = Flask(__name__)

#dados
livros = [
    {id: 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'},
    {id: 2, 'titulo': 'Harry Potter e a Pedra Filosofal', 'autor': 'J.K. Rowling'},
    {id: 3, 'titulo': 'O Código Da Vinci', 'autor': 'Dan Brown'}
]

#rota para obter todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    return jsonify(livro[0])

#rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# rota para atualizar um livro existente
@app.route('/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    livro[0]['titulo'] = request.get_json().get('titulo', livro[0]['titulo'])
    livro[0]['autor'] = request.get_json().get('autor', livro[0]['autor'])
    return jsonify({'mensagem': 'Livro atualizado com sucesso'})

#rota para deletar um livro
@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    livros.remove(livro[0])
    return jsonify({'mensagem': 'Livro deletado com sucesso'})