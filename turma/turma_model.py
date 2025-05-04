from professor.professor_model import Professor
from config import db

class Turma(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable = False)
    Professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    professor = db.relationship('professores', backref='turmas', lazy=True) 
    ativo = db.Column(db.Boolean, default=True, nullable =False)

    alunos = db.relationship('Aluno', back_populates='turma', lazy=True)

    def __init__(self, descricao, professor_id, ativo):
        self.descricao = descricao
        self.Professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao, 'Professor_id': self.Professor_id, 'ativo': self.ativo}

class Turmanaoencontrada (Exception):
    pass

class CamposVazio(Exception):
    pass

class NenhumDado (Exception):
    pass

def create_turma(data):
    campos = [
        'descricao', 'professor_id', 'ativo'
    ]
    
    campos_vazio = [ campo for campo in campos if not data.get(campo)]
    if campos_vazio:
        raise CamposVazio(campos_vazio)
    
    nova_turma = Turma(
        descricao = data ['descricao'],
        professor_id = int (data ['professor_id']),
        ativo = bool (data ['ativo'])
    )

    db.session.add(nova_turma)
    db.session.commit()

    return nova_turma.to_dict(), 201

    

def Listar_turma():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def turma_por_id(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise Turmanaoencontrada
    return turma.to_dict()
    
def delete_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise Turmanaoencontrada
    
    db.session.delete(turma)
    db.session.commit()
    return

def update_turma(turma_id, novos_dados):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise Turmanaoencontrada
    
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
            raise CamposVazio(campos_vazio)
    
    turma.descricao = dados['descricao']
    turma.professor_id = int(dados['professor_id'])
    turma.ativo = bool(dados['ativo'])

    db.session.commit()
    return turma
    
    







    # for turma in turmas:
    #     if turma['id']== turma_id:
    #         dados = novos_dados
    #         if not dados:
    #             raise NenhumDado
    #         campos = [ 
    #              'descricao', 'professor_id', 'ativo'
    #         ]
    #         campos_vazio = []
    #         for campo in campos: 
    #             if campo in dados and (dados[campo]is None or dados[campo]== ""):
    #                 campos_vazio.append(campo)
    #                 raise CamposVazio(campos_vazio)
                
    #             for campo in campos:
    #                 if campo in dados:
    #                     turma[campo]= dados[campo]
    #             return turma
    # raise Turmanaoencontrada