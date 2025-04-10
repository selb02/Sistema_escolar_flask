from flask import Blueprint, request, jsonify
from .professor_model import ProfessorNaoEncontrado, CampoVazio, NenhumDado, get_professor,update_professor,create_professor, delete_professor, listar_professor

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professor/<int:professor_id>', methods=['GET'])
def pegar_professor(professor_id):
    try:
        professor = get_professor(professor_id)
        return jsonify(professor), 200
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404

@professor_blueprint.route('/professor', methods=['GET'])
def get_professores():
    return jsonify({'professores': listar_professor()}), 200

@professor_blueprint.route('/professor', methods=['POST'])
def criando_professor():
    data = request.json
    try:
        professor = create_professor(data)
        return jsonify(professor), 201
    except CampoVazio as e:
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(e.args[0])}'}), 400



@professor_blueprint.route('/professor/<int:professor_id>', methods=['PUT'])
def atualizar_professor(professor_id):
    data = request.json
    try:
        professor_atualizado = update_professor(professor_id, data)
        return jsonify(professor_atualizado), 200
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404
    except NenhumDado:
        return jsonify({'mensagem': 'Nenhum dado enviado'}), 400
    except CampoVazio as e:
        return jsonify({'mensagem': f'Os seguintes campos não podem estar vazios: {", ".join(e.args[0])}'}), 400



@professor_blueprint.route('/professor/<int:professor_id>', methods=['DELETE'])
def deletar_professor(professor_id):
    try:
        delete_professor(professor_id)
        return jsonify({'mensagem': 'Professor removido'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404
