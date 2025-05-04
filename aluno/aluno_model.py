from datetime import datetime, date
from config import db
from turma import Turma


class Aluno(db.model):
    __tablename__ = "alunos"

    id = db.Column(db.interger, primary_key =True)
    nome = db.Column(db.String(100), nullable= False)
    idade= db.Column(db.Interger, nullable= False)
    turma_id= db.Column(db.interger, nullable= False)
    data_nascimento = db.Column(db.String(10), nullable= False) 
    primeira_nota = db.Column(db.Float, nullable= False)
    segunda_nota = db.Column(db.Float, nullable= False)

    turma = db.relationship("Turma", back_populates="alunos")
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)


    def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id, media_final):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.turma_id = turma_id
        self.media_final = media_final
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
    
    def to_dict(self):
        return {'id': self.id, 'nome' : self.nome, 'idade': self.idade, 'data_nascimento' : self.data_nascimento.isoformat(), "primeira_nota": self.primeira_nota, "segunda_nota": self.segunda_nota, "turma_id": self.turma_id, "media_final": self.media_final }
class alunoNaoEncontrado():
    pass

def aluno_id(id_aluno):
    aluno= Aluno.query.get(id_aluno)

    if not aluno:
        raise alunoNaoEncontrado()
    return aluno.to_dict()

def Listar_Alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]
    
def adicionar_aluno(novos_dados):
    turma= Turma.query.get(novos_dados['turma-id'])
    if(turma is None):
        return {"message": "Turma não existe"}, 404
    
    novo_aluno = Aluno(
         nome=novos_dados['nome'],
            data_nascimento=datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date(),
            nota_primeiro_semestre=float(novos_dados['nota_primeiro_semestre']),
            nota_segundo_semestre=float(novos_dados['nota_segundo_semestre']),
            turma_id=int(novos_dados['turma_id']),
            media_final=(
                float(novos_dados['nota_primeiro_semestre']) + float(novos_dados['nota_segundo_semestre'])
            ) / 2,
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return{
        "message": "O Aluno foi adicionado!"
    }, 201



def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise alunoNaoEncontrado
    
    aluno.nome = novos_dados['nome']
    aluno.data_nascimento = novos_dados['data_nascimento']
    aluno.primeira_nota = novos_dados ['Primeira Nota']
    aluno.segunda_nota = novos_dados ['segunda nota']
    aluno.media_final = novos_dados (aluno.nota_primeiro_semestre + aluno.nota_segundo_semestre) / 2
    aluno.turma_id = novos_dados ['turma_id']
    aluno.idade = aluno.calcular_idade()

    db.session.commit()

def deletar_aluno(id_aluno):
    aluno = aluno.query.get(id_aluno)
    if not aluno:
        raise alunoNaoEncontrado()
    db.session.delete(aluno)
    db.session.commit()
