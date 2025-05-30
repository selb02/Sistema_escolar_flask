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
    data_nascimento = db.Column(db.Date, nullable= False)
    idade = db.Column(db.Integer, nullable = False)
    materia = db.Column(db.String(100), nullable = False)
    observacoes = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime('%Y-%m-%d'),
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes
    }


    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - (
            (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )


def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado ()
    return professor.to_dict()


def listar_professores():
    professores = Professor.query.all()
    return [prof.to_dict() for prof in professores]


def calcular_idade(data_nascimento):
    today = date.today()
    return today.year - data_nascimento.year - (
        (today.month, today.day) < (data_nascimento.month, data_nascimento.day)
    )

def adicionar_professor(dados):
    campos_obrigatorios = ['nome', 'data_nascimento', 'materia']
    for campo in campos_obrigatorios:
        if campo not in dados or dados[campo] == '':
            return {"message": f"Campo '{campo}' é obrigatório e não pode estar vazio."}, 400

    data_nascimento = datetime.strptime(dados['data_nascimento'], "%Y-%m-%d").date()
    idade = calcular_idade(data_nascimento)  # Calcula idade corretamente

    novo_professor = Professor(
        nome=dados['nome'],
        data_nascimento=data_nascimento,
        idade=idade,  # importante atribuir
        materia=dados['materia'],
        observacoes=dados.get('observacoes')
    )

    db.session.add(novo_professor)
    db.session.commit()

    return {"message": "Professor foi adicionado com sucesso!"}, 201

def atualizar_professor(id_professor, dados):
    professor = Professor.query.get(id_professor)
    if not professor:   
     raise ProfessorNaoEncontrado()
    
    if 'nome' not in dados or dados['nome'] == '':
        return {"message": "Campo 'nome' é obrigatório."}, 400
    if 'data_nascimento' not in dados or dados['data_nascimento'] == '':
        return {"message": "Campo 'data_nascimento' é obrigatório."}, 400
    if 'materia' not in dados or dados['materia'] == '':
        return {"message": "Campo 'materia' é obrigatório."}, 400
    

    professor.nome = dados['nome']
    professor.data_nascimento = datetime.strptime(dados['data_nascimento'], "%Y-%m-%d").date()
    professor.materia = dados['materia']
    professor.observacoes = dados.get('observacoes')
    professor.idade = professor.calcular_idade()

    db.session.commit()
    return{"message": "Informações Atualizadas com sucesso! "}, 200

def delete_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado()

    db.session.delete(professor)
    db.session.commit()
    return   {"message": "Professor foi retirado da lista! "}, 200