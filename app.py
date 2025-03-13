from flask import Flask, jsonify, request

meuApp = Flask(__name__)

alunos = {}
professores = {}
turmas = {}

@meuApp.route('/alunos', method=['POST'])
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

@meuApp.route('/professor', method=['POST'])
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

@meuApp.route('/turma', method=['POST'])
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
    




if __name__ == '__main__':
    meuApp.run(debug=True)