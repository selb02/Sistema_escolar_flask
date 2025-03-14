from flask import Flask, jsonify, request

meuApp = Flask(__name__)

alunos = []
professores = []
turmas = []

@meuApp.route('/aluno', methods=['POST'])
def create_alunos():
    data = request.json
    aluno = {
        'id': len(alunos) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'turma_id': data['turma'],
        'data_nascimento': data['data_nascimento'],
        'nota_primeiro_semestre': data['nota_primeiro_semestre'],
        'nota_segundo_semestre': data['nota_segundo_semestre'],
        'media_final': data['media_final']
    }
    alunos.append(aluno)
    return jsonify(aluno), 201

@meuApp.route('/professor', methods=['POST'])
def create_professor():
    data = request.json
    professor = {
        'id': len(professores) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacoes': data['observacoes']
    }
    professores.append(professor)
    return jsonify(professor), 201

@meuApp.route('/turma', methods=['POST'])
def create_turma():
    data = request.json
    turma = {
        'id': len(turmas) + 1,
        'descricao': data['descricao'],
        'professor_id': data['professor_id'],
        'ativo': data['ativo']
    }
    turmas.append(turma)
    return jsonify(turma), 201




@meuApp.route('/aluno', methods=['GET'])
def get_alunos():
    return jsonify({'alunos': alunos})

@meuApp.route('/professor', methods=['GET'])
def get_professores():
    return jsonify({'professores': professores})

@meuApp.route('/turma', methods=['GET'])
def get_turmas():
    return jsonify({'turmas': turmas})





@meuApp.route('/aluno/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return jsonify(aluno)
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/professor/<int:professor_id>', methods=['GET'])
def get_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            return jsonify(professor)
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@meuApp.route('/turma/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            return jsonify(turma)
    return jsonify({'mensagem': 'Turma não encontrada'}), 404



@meuApp.route('/aluno/<int:user_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/professor/<int:user_id>', methods=['DELETE'])
def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@meuApp.route('/turma/<int:user_id>', methods=['DELETE'])
def delete_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma removida'})
    return jsonify({'mensagem': 'Turma não encontrada'}), 404




@meuApp.route('/aluno/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            dados = request.json
            campos = [
                'nome', 'idade', 'turma_id', 'data_nascimento',
                'nota_primeiro_semestre', 'nota_segundo_semestre', 'media_final'
            ]
            for campo in campos:
                novo_valor = dados.get(campo)
                if novo_valor: 
                    aluno[campo] = novo_valor
            return jsonify(aluno)
    
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/professor/<int:aluno_id>', methods=['PUT'])
def update_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            dados = request.json
            campos = [
                    'nome', 'idade', 'materia', 'observacoes'
            ]
            for campo in campos:
                novo_valor = dados.get(campo)
                if novo_valor: 
                    professor[campo] = novo_valor
            return jsonify(professor)
    
    return jsonify({'mensagem': 'professor não encontrado'}), 404

@meuApp.route('/turma/<int:aluno_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            dados = request.json
            campos = [
                    'descricao', 'professor_id', 'ativo'
            ]
            for campo in campos:
                novo_valor = dados.get(campo)
                if novo_valor: 
                    turma[campo] = novo_valor
            return jsonify(turma)
    
    return jsonify({'mensagem': 'turma não encontrada'}), 404



if __name__ == '__main__':
    meuApp.run(debug=True)