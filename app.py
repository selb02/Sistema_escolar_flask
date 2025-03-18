from flask import Flask, jsonify, request

meuApp = Flask(__name__)

alunos = []
professores = []
turmas = []

@meuApp.route('/aluno', methods=['POST'])
def create_alunos():
    data = request.json
    
    campos = [
        'nome', 'idade', 'turma_id', 'data_nascimento',
        'nota_primeiro_semestre', 'nota_segundo_semestre', 'media_final'
    ]
    
    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return jsonify({'mensagem': f'Esse/s campo/s sao obrigatorios e nao podem estar vazios: {",".join(campos_vazio)}'}),400
    
    aluno = {'id': len(alunos) + 1, **{campo: data[campo] for campo in campos}}
    alunos.append(aluno)
    return jsonify(aluno), 201

@meuApp.route('/professor', methods=['POST'])
def create_professor():
    data = request.json
    
    campos = [
        'nome', 'idade', 'materia', 'observacoes'
    ]
    
    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return jsonify({'mensagem': f'Esse(s) campo(s) sao obrigatorios e nao podem estar vazios: {",".join(campos_vazio)}'}),400
    
    professor = {'id': len(professores) + 1, **{campo: data[campo] for campo in campos}}
    professores.append(professor)
    return jsonify(professor), 201

@meuApp.route('/turma', methods=['POST'])
def create_turma():
    data = request.json
    
    campos = [
        'descricao', 'professor_id', 'ativo'
    ]
    
    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return jsonify({'mensagem': f'Esse/s campo/s sao obrigatorios e nao podem estar vazios: {",".join(campos_vazio)}'}),400
    
    turma = {'id': len(turmas) + 1, **{campo: data[campo] for campo in campos}}
    professores.append(turma)
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



@meuApp.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/professor/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@meuApp.route('/turma/<int:turma_id>', methods=['DELETE'])
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
            if not dados:
                return jsonify({'mensagem': 'Nenhum dado enviado'}), 400 
            
            campos = [
                'nome', 'idade', 'turma_id', 'data_nascimento',
                'nota_primeiro_semestre', 'nota_segundo_semestre', 'media_final'
            ]
            
            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    return jsonify({'mensagem': f'O campo "{campo}" não pode estar vazio'}), 400
                
            for campo in campos:
                if campo in dados:
                    aluno[campo] = dados[campo]
            return jsonify(aluno), 200
        
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/professor/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            dados = request.json
            if not dados:
                return jsonify({'mensagem': 'Nenhum dado enviado'}), 400  

            campos = [
                'nome', 'idade', 'materia', 'obeservacoes'
            ]

            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    return jsonify({'mensagem': f'O campo "{campo}" não pode estar vazio'}), 400

            for campo in campos:
                if campo in dados:
                    professor[campo] = dados[campo]
            return jsonify(professor), 200
    
    return jsonify({'mensagem': 'professor não encontrado'}), 404

@meuApp.route('/turma/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            dados = request.json
            if not dados:
                return jsonify({'mensagem': 'Nenhum dado enviado'}), 400 

            campos = [
                'descricao', 'professor_id', 'ativo'
            ]

            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    return jsonify({'mensagem': f'O campo "{campo}" não pode estar vazio'}), 400

            for campo in campos:
                if campo in dados:
                    turma[campo] = dados[campo]
            return jsonify(turma), 200
    
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404






if __name__ == '__main__':
    meuApp.run(debug=True)