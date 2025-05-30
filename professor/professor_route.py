from flask import Blueprint, request, jsonify
from .professor_model import ProfessorNaoEncontrado, CampoVazio , NenhumDado, professor_por_id, atualizar_professor, adicionar_professor, delete_professor, listar_professores

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professor/<int:professor_id>', methods=['GET'])
def pegar_professor(professor_id):
    try:
        professor = professor_por_id(professor_id)
        return jsonify(professor), 200
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404

@professor_blueprint.route('/professor', methods=['GET'])
def get_professores():
    return jsonify({'professores': listar_professores()}), 200

@professor_blueprint.route('/professor', methods=['POST'])
def criando_professor():
    data = request.json
    try:
        professor = adicionar_professor(data)
        return jsonify(professor), 201
    except CampoVazio as e:
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(e.args[0])}'}), 400



@professor_blueprint.route('/professor/<int:professor_id>', methods=['PUT'])
def Atualizar_professor(professor_id):
    data = request.json
    try:
        professor_atualizado = atualizar_professor(professor_id, data)
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
