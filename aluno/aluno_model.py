from datetime import datetime, date
from config import db
from turma.turma_model import Turma

class AlunoNaoEncontrado(Exception):
    pass

class CampoVazio(Exception):
    pass

class NenhumDado(Exception):
    pass

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key =True)
    nome = db.Column(db.String(100), nullable= False)
    idade= db.Column(db.Integer, nullable= False)
    data_nascimento = db.Column(db.Date, nullable= False) 
    primeira_nota = db.Column(db.Float, nullable= False)
    segunda_nota = db.Column(db.Float, nullable= False)
    media_final = db.Column(db.Float, nullable = False)

    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)
    turma = db.relationship("Turma", back_populates="alunos")



    def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.primeira_nota = nota_primeiro_semestre
        self.segunda_nota = nota_segundo_semestre
        self.turma_id = turma_id
        self.media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2
        self.idade = self.calcular_idade()


    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
    
    def to_dict(self):
        return {'id': self.id, 'nome' : self.nome, 'idade': self.idade, 'data_nascimento' : self.data_nascimento.isoformat(), "primeira_nota": self.primeira_nota, "segunda_nota": self.segunda_nota, "turma_id": self.turma_id, "media_final": self.media_final }


def buscar_aluno_id(id_aluno):
    aluno= Aluno.query.get(id_aluno)

    if not aluno:
        raise AlunoNaoEncontrado()
    return aluno.to_dict()

def Listar_Alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]
    
def adicionar_aluno(novos_dados):
    turma= Turma.query.get(novos_dados['turma_id'])
    if(turma is None):
        return {"message": "Turma não existe"}, 404
    
    novo_aluno = Aluno(
         nome=novos_dados['nome'],
            data_nascimento=datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date(),
            nota_primeiro_semestre=float(novos_dados['nota_primeiro_semestre']),
            nota_segundo_semestre=float(novos_dados['nota_segundo_semestre']),
            turma_id=int(novos_dados['turma_id']),
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return{
        "message": "O Aluno foi adicionado!"
    }, 201



def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado()
    
    aluno.nome = novos_dados['nome']
    aluno.data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date()
    aluno.primeira_nota = novos_dados ['nota_primeiro_semestre']
    aluno.segunda_nota = novos_dados ['nota_segundo_semestre']
    aluno.media_final = (aluno.primeira_nota + aluno.segunda_nota) / 2
    aluno.turma_id = novos_dados ['turma_id']
    aluno.idade = aluno.calcular_idade()

    db.session.commit()

def deletar_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado()
    db.session.delete(aluno)
    db.session.commit()
