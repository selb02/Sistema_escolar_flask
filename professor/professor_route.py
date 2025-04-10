from flask import Blueprint, request, jsonify
from .professor_model import ProfessorNaoEncontrado, CampoVazio, NenhumDado, get_professor,update_professor,create_professor, delete_professor, listar_professor

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professor/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    try:
        professor = get_professor(professor_id)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404

@professor_blueprint.route('/professor', methods=['GET'])
def get_professores():
    return jsonify({'professores': listar_professor()})

@professor_blueprint.route('/professor', methods=['POST'])
def create_professor():
    data = request.json
    try:
        professor = create_professor(data)
        return jsonify(professor), 201
    except CampoVazio:
        professor = create_professor(data)
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(professor)}'}), 400


@professor_blueprint.route('/professor/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    data = request.json
    try:
        professor_atualizado = update_professor(professor_id, data)
        return jsonify(professor_atualizado), 200
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor nã encontrado'}), 404
    except NenhumDado:
        return jsonify({'mensagem': 'Nnhum dado enviado'}), 400
    except CampoVazio:
        professor_atualizado = update_professor(professor_id, data)
        return jsonify({'mensagem': f'O campo "{professor_atualizado}" não pode estar vazio'}), 400


@professor_blueprint.route('/professor/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    try:
        delete_professor(professor_id)
        return jsonify({'mensagem': 'Professor removido'}), 204
    except ProfessorNaoEncontrado:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404
