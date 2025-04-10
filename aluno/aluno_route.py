from flask import Blueprint, request, jsonify
from .aluno_model import AlunoNaoEncontrado, CampoVazio, NenhumDado, create_aluno, listar_alunos, aluno_por_id, delete_aluno, update_aluno


alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/aluno', methods=['POST'])
def create_alunos():
    data = request.json
    try:
        aluno = create_aluno(data)
        return jsonify(aluno), 201
    except CampoVazio as e:
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(e.args[0])}'}), 400





@alunos_blueprint.route('/aluno', methods=['GET'])
def get_alunos():
    return jsonify({'alunos':listar_alunos()}), 200


@alunos_blueprint.route('/aluno/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    try:
        aluno = aluno_por_id(aluno_id)
        return jsonify(aluno), 200
    except AlunoNaoEncontrado:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404


@alunos_blueprint.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    try:
        delete_aluno(aluno_id)
        return jsonify({'mensagem': 'Aluno removido'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404


@alunos_blueprint.route('/aluno/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    data = request.json
    try:
        aluno_atualizado = update_aluno(aluno_id, data)
        return jsonify (aluno_atualizado), 200
    except AlunoNaoEncontrado:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404
    except NenhumDado:
        return jsonify({'mensagem': 'Nenhum dado enviado'}), 400
    except CampoVazio as e:
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(e.args[0])}'}), 400
