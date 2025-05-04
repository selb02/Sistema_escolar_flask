from flask_restx import Namespace, Resource, fields
from professor.professor_model import listar_professores, professor_por_id, adicionar_professor, atualizar_professor, excluir_professor

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "observacoes": fields.String(required=True, description="Observações sobre o professor"),
    "materia": fields.String(required=True, description="Matéria dada pelo professor")

})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "materia": fields.String(description="Matéria dada pelo professor"),
    "observacoes": fields.Float(description="Observações sobre o professor")
})

@professores_ns.route("/")
class AlunosResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        return listar_professores()

    @professores_ns.expect(professor_model)
    def post(self):
        data = professores_ns.payload
        response, status_code = adicionar_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_aluno):
        return professor_por_id(id_aluno)

    @professores_ns.expect(professor_model)
    def put(self, id_aluno):
        data = professores_ns.payload
        atualizar_professor(id_aluno, data)
        return data, 200

    def delete(self, id_aluno):
        excluir_professor(id_aluno)
        return {"message": "Aluno excluído com sucesso"}, 200