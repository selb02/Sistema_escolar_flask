
professores= []


class ProfessorNaoEncontrado(Exception):
    pass

class NenhumDado(Exception):
    pass

class CampoVazio(Exception):
    pass

def listar_professor():
    return professores

def get_professor(professor_id):
    lista_professores = professores
    for professor in lista_professores:
        if professor['id'] == professor_id:
            return professor
    raise ProfessorNaoEncontrado


def create_professor(data):

    campos = [
        'nome', 'idade', 'materia', 'observacoes'
    ]

    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return campos_vazio
    professor = {'id': len(professores) + 1, **{campo: data[campo] for campo in campos}}
    professores.append(professor)
    return professor



def update_professor(professor_id, novos_dados):
    for professor in professores:
        if professor['id'] == professor_id:
            dados = novos_dados
            if not dados:
                raise NenhumDado
            campos = [
                'nome', 'idade', 'materia', 'observacoes'
            ]

            campos_vazios = []
            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    campos_vazios.append(campo)
                    return campos_vazios
        
            for campo in campos:
                if campo in dados:
                    professor[campo] = dados[campo]
            return professor


def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professores.remove(professor)


