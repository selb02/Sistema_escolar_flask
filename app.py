from swagger.swagger_config import configure_swagger
from config import app, db
from aluno.aluno_route import alunos_blueprint
from professor.professor_route import professor_blueprint
from turma.turma_route import turma_blueprint

app.register_blueprint(alunos_blueprint, url_prefix='/api')
app.register_blueprint(professor_blueprint, url_prefix='/api')
app.register_blueprint(turma_blueprint, url_prefix='/api')

configure_swagger(app)

with app.app_context():
    db.create_all()
    db.create_all()
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
