from flask import jsonify, request

alunos = []

class AlunoNaoEncontrado(Exception):
    pass

class CampoVazio(Exception):
    pass

class NenhumDado(Exception):
    pass

def create_aluno(data):

    campos = [
        'nome', 'idade', 'turma_id', 'data_nascimento',
        'nota_primeiro_semestre', 'nota_segundo_semestre'
    ]

    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        raise CampoVazio(campos_vazio)
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
        else:
            raise AlunoNaoEncontrado

def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
        else:
            raise AlunoNaoEncontrado

def update_aluno(id_aluno, novos_dados):
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            dados = novos_dados
            if not dados:
                raise NenhumDado

            campos = [
                'nome', 'idade', 'turma_id', 'data_nascimento',
                'nota_primeiro_semestre', 'nota_segundo_semestre', 'media_final'
            ]

            campos_vazios = []
            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    campos_vazios.append(campo)


            if campos_vazios:
                raise CampoVazio(campos_vazios)

            for campo in campos:
                if campo in dados:
                    aluno[campo] = dados[campo]
            
            if 'nota_primeiro_semestre' in aluno and 'nota_segundo_semestre' in aluno:
                try:
                    aluno['media_final'] = (float(aluno['nota_primeiro_semestre']) + float(aluno['nota_segundo_semestre'])) / 2
                except ValueError:
                    pass  

            return aluno
    raise AlunoNaoEncontrado
