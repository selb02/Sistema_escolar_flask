from flask import Blueprint, request, jsonify
from .aluno_model import AlunoNaoEncontrado, create_aluno, listar_alunos, aluno_por_id, delete_aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/aluno', methods=['POST'])
def create_alunos():
    data = request.json
    aluno = create_aluno(data)
    return jsonify(aluno), 201


@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify({'alunos':listar_alunos()})


@alunos_blueprint.route('/aluno/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    try:
        aluno = aluno_por_id(aluno_id)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'messagem': 'Aluno não encontrado'}), 404


@alunos_blueprint.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    try:
        delete_aluno(aluno_id)
        return jsonify({'mensagem': 'Professor removido'}), 204
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    