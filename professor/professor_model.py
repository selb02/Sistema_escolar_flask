from datetime import datetime, date
from config import db

class ProfessorNaoEncontrado(Exception):
    pass

class CampoVazio(Exception):
    pass

class NenhumDado(Exception):
    pass

class Professor (db.Model): 
    __tablename__ = "professores"
    
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(100), nullable= False)
    idade = db.Column(db.Date, nullable= False)
    materia = db.Column(db.String(100), nullable = False)
    observacoes = db.Column(db.Text)

    def __init__(self, nome, idade, materia, observacoes=None):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )


    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes        
        }
    


def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado ()
    return professor.to_dict()


def listar_professores():
    professores = Professor.query.all()
    return [prof.to_dict() for prof in professores]


def adicionar_professor(dados):
    campos_obrigatorios = ['nome', 'idade', 'materia', 'observacoes']
    for campo in campos_obrigatorios:
        if campo not in dados or dados[campo] == '':
            return{"message": f"campo' {campo}' é obrigatório e nao pode estar vazio."}, 400
        

        novo_professor = Professor(
            nome = dados ['nome'],
            idade = int (dados['idade']),
            materia = dados['materia'],
            observacoes=dados.get('observaçoes')
            
        )

        db.session.add(novo_professor)
        db.session.commit()

        return{"message": "Professor foi adicionado com sucesso! "}, 201


def atualizar_professor(id_professor, dados):
    professor = Professor.query.get(id_professor)
    if not professor:   
     raise ProfessorNaoEncontrado()
    
    if 'nome' not in dados or dados['nome'] == '':
        return {"message": "Campo 'nome' é obrigatório."}, 400
    if 'idade' not in dados or dados['idade'] == '':
        return {"message": "Campo 'idade' é obrigatório."}, 400
    if 'materia' not in dados or dados['materia'] == '':
        return {"message": "Campo 'materia' é obrigatório."}, 400
    

    professor.nome = dados['nome']
    professor.idade = int(dados['idade'])
    professor.materia = dados ['materia']
    professor.observacoes = dados.get('observacoes')

    db.session.commit()
    return{"message": "Informações Atualizadas com sucesso! "}, 200

def delete_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado()

    db.session.delete(professor)
    db.session.commit()
    return   {"message": "Professor foi retirado da lista! "}, 200
    