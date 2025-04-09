
professores= []


class ProfessorNaoEncontrado(Exception):
    pass


def get_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
           
            def listar_professores():
                return professores

def create_professor(data):

    campos = [
        'nome', 'idade', 'materia', 'observacoes'
    ]

    campos_vazio = [campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        
        professor = {'id': len(professores) + 1, **{campo: data[campo] for campo in campos}}
    professores.append(professor)
    return (professor), 



def update_professor(professor_id, novos_dados):
    for professor in professores:
        if professor['id'] == professor_id:
            dados = novos_dados
            if not dados:

                campos = [
                'nome', 'idade', 'materia', 'observacoes'
            ]

            for campo in campos:
                if campo in dados and (dados[campo] is None or dados[campo] == ""):
                    for campo in campos:
                        if campo in dados:
                            professor[campo] = dados[campo]


def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professores.remove(professor)


