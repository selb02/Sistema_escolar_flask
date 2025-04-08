from flask import jsonify, request

alunos = []

class AlunoNaoEncontrado(Exception):
    pass

def create_aluno(data):

    campos = [
        'nome', 'idade', 'turma_id', 'data_nascimento',
        'nota_primeiro_semestre', 'nota_segundo_semestre'
    ]

    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return jsonify({'mensagem': f'Esses campos são obrigatórios e não podem estar vazios: {", ".join(campos_vazio)}'}), 400
    aluno = {'id': len(alunos) + 1, 'media_final': (float(data['nota_primeiro_semestre']) + float(data['nota_segundo_semestre'])) / 2, **{campo: data[campo] for campo in campos}}
    alunos.append(aluno)
    return aluno

def listar_alunos():
    return alunos

def aluno_por_id(id_aluno):
    lista_alunos = alunos
    for aluno in lista_alunos:
        if aluno['id'] == id_aluno:
            return aluno
    raise AlunoNaoEncontrado

def delete_aluno(id_aluno):
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            alunos.remove(aluno)