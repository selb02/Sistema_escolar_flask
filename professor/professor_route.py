from flask import Blueprint, request, jsonify
from .professor_model import ProfessorNaoEncontrado, get_professor, create_professor, update_professor, delete_professor

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professor/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    for professor in professor:
        if professor['id'] == professor_id:
            return jsonify(professor)
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@professor_blueprint.route('/professor', methods=['POST'])
def create_professor():
    data = request.json

    campos = [
        'nome', 'idade', 'materia', 'observacoes'
    ]

    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(campos_vazio)}'}), 400

    professor = {'id': len(professor) + 1, **{campo: data[campo] for campo in campos}}
    professor.append(professor)
    return jsonify(professor), 201

@professor_blueprint.route('/professor/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    for professor in professor:
        if professor['id'] == professor_id:
            dados = request.json
            if not dados:
                return jsonify({'mensagem': 'Nenhum dado enviado'}), 400

            campos = [
                'nome', 'idade', 'materia', 'observacoes'
            ]

            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    return jsonify({'mensagem': f'O campo "{campo}" não pode estar vazio'}), 400

            for campo in campos:
                if campo in dados:
                    professor[campo] = dados[campo]
            return jsonify(professor), 200

    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@professor_blueprint.route('/professor/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    for professor in professor:
        if professor['id'] == professor_id:
            professor.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404
