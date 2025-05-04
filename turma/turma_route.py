from flask import Blueprint, request, jsonify
from .turma_model import Turmanaoencontrada, CamposVazio, NenhumDado, Listar_turma, turma_por_id, delete_turma, update_turma, create_turma
turma_blueprint = Blueprint ('turmas', __name__)

@turma_blueprint.route('/turma', methods=['POST'])
def criar_turma():
    data = request.json
    try:    
        turma = create_turma(data)
        return jsonify(turma), 201
    except CamposVazio as e:
            campos_vazios = e.campos_vazios
            return jsonify ({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(campos_vazios)} '}), 400



@turma_blueprint.route('/turma', methods=['GET'])
def get_turmas():
    return jsonify({'turmas': Listar_turma()}), 200



@turma_blueprint.route('/turma/<int:turma_id>',  methods=['GET'])
def get_turma(turma_id):
    try:
        turma = turma_por_id(turma_id)
        return jsonify(turma), 200
    except Turmanaoencontrada:
        return jsonify({'mensagem': 'Turma não encontrada'}), 404
    

    
@turma_blueprint.route('/turma/<int:turma_id>', methods=['DELETE'])
def deletar_turma(turma_id):
    try:
        delete_turma(turma_id)
        return jsonify({'mensagem': 'Turma foi removida'}), 200
    except Turmanaoencontrada:
        return jsonify({'mensagem': 'Turma não encontrada'}), 404
    

@turma_blueprint.route('/turma/<int:turma_id>', methods=['PUT'])
def atualizar_turma(turma_id):
    data = request.json
    try:
        turma_atualizada = update_turma(turma_id, data)
        return jsonify(turma_atualizada), 200
    except Turmanaoencontrada:
        return jsonify({'mensagem': 'Turma não encontrada'}), 404
    except NenhumDado:
        return jsonify({'mensagem': 'Nenhum Dado enviado'}), 400
    except CamposVazio as e:
        campos_vazios = e.campos_vazios
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(campos_vazios)}'}), 400

    
    