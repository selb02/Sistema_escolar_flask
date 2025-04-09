turmas = []
class Turmanaoencontrada (Exception):
    pass

class CamposVazio (Exception):
    pass

class NenhumDado (Exception):
    pass

def create_turma(data):
    campos = [
        'descricao', 'professor_id', 'ativo'
    ]
    
    campos_vazio = [ campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        return campos_vazio
    
    turma = {'id': len(turmas) +1, **{campo: data[campo] for campo in campos }}
    turmas.append(turma)
    return turma

def Listar_turma():
    return turmas

def turma_por_id(turma_id):
    lista_turmas = turmas
    for turma in lista_turmas:
        if turma["id"] == turma_id:
            return turma
        raise Turmanaoencontrada
    
def delete_turma(turma_id):
        for turma in turmas:
            if turma ['id'] == turma_id:
                turmas.remove(turma)


def update_turma(turma_id, novos_dados):
    for turma in turmas:
        if turma['id']== turma_id:
            dados = novos_dados
            if not dados:
                raise NenhumDado
            campos = [ 
                 'descricao', 'professor_id', 'ativo'
            ]
            campos_vazio = []
            for campo in campos: 
                if campo in dados and (dados[campo]is None or dados[campo]== ""):
                    campos_vazio.append(campo)
                    return campos_vazio
                
                for campo in campos:
                    if campo in dados:
                        turma[campo]= dados[campo]
                        return turma
                    else: Turmanaoencontrada