import requests
import unittest
import time

URL_Base = "http://127.0.0.1:8000"

class TesteAPI(unittest.TestCase):
    def setUp(self):
        time.sleep(1) 
    # Teste Alunos
    def test_get_alunos(self):
        resposta = requests.get(f"{URL_Base}/api/aluno")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json()['alunos'], list)

    def test_get_alunos_id(self):
        dados = {
            "nome": "Joao", "idade": "18", "turma_id": "2",
            "data_nascimento": "23/02/2006", "nota_primeiro_semestre": "9",
            "nota_segundo_semestre": "9"
        }
        requests.post(f"{URL_Base}/api/aluno", json=dados)
        resposta = requests.get(f"{URL_Base}/api/aluno/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), dict)

    def test_post_aluno(self):
        dados = {
            "nome": "jonathan", "idade": "19", "turma_id": "2",
            "data_nascimento": "25/08/1992", "nota_primeiro_semestre": "9",
            "nota_segundo_semestre": "9"
        }
        resposta = requests.post(f"{URL_Base}/api/aluno", json=dados)
        self.assertEqual(resposta.status_code, 201)
        self.assertIn(resposta.json(), requests.get(f"{URL_Base}/api/aluno").json()['alunos'])

    def test_delete_aluno(self):
        dados = {
            "nome": "jonathan", "idade": "19", "turma_id": "2",
            "data_nascimento": "25/08/1992", "nota_primeiro_semestre": "9",
            "nota_segundo_semestre": "9"
        }
        requests.post(f"{URL_Base}/api/aluno", json=dados)
        resposta = requests.delete(f"{URL_Base}/api/aluno/1")
        self.assertEqual(resposta.status_code, 200)
        resposta_lista = requests.get(f"{URL_Base}/api/aluno").json()['alunos']
        self.assertFalse(any(aluno['nome'] == 'jonathan' for aluno in resposta_lista))

    def test_edita_aluno(self):
        dados = {
            "nome": "jonathan", "idade": "19", "turma_id": "2",
            "data_nascimento": "25/08/1992", "nota_primeiro_semestre": "9",
            "nota_segundo_semestre": "9"
        }
        dados_editados = {
            "nome": "joão", "idade": "19", "turma_id": "1",
            "data_nascimento": "22/04/1202", "nota_primeiro_semestre": "8",
            "nota_segundo_semestre": "10"
        }
        requests.post(f"{URL_Base}/api/aluno", json=dados)
        resposta = requests.put(f"{URL_Base}/api/aluno/1", json=dados_editados)
        self.assertEqual(resposta.status_code, 200)
        resposta_get = requests.get(f"{URL_Base}/api/aluno/1")
        self.assertEqual(resposta_get.json()['nome'], 'joão')

    def test_get_aluno_inexistente(self):
        resposta = requests.get(f"{URL_Base}/api/aluno/99")
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json(), {"mensagem": "Aluno não encontrado"})

    def test_post_aluno_sem_nome(self):
        dados = {
            "nome": "", "idade": "19", "turma_id": "2",
            "data_nascimento": "25/08/1992", "nota_primeiro_semestre": "9",
            "nota_segundo_semestre": "9"
        }
        resposta = requests.post(f"{URL_Base}/api/aluno", json=dados)
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("nome", resposta.json()['mensagem'])
        
    # Teste professores
    def test_100_get_lista_professores(self):
        resposta = requests.get(f"{URL_Base}/api/professor")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json()['professores'], list)

    def test_102_get_professor_por_id(self):
        dados = {
            "nome": "ortega", "idade": "54", "materia": "sql",
            "observacoes": "legal"
        }
        requests.post(f"{URL_Base}/api/professor", json=dados)
        resposta = requests.get(f"{URL_Base}/api/professor/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), dict)

    def test_101_post_cria_professor(self):
        dados = {
            "nome": "ortega", "idade": "54", "materia": "sql",
            "observacoes": "legal"
        }
        resposta = requests.post(f"{URL_Base}/api/professor", json=dados)
        self.assertEqual(resposta.status_code, 201)
        self.assertIn(resposta.json(), requests.get(f"{URL_Base}/api/professor").json()['professores'])

    def test_103_delete_professor(self):
        dados = {
            "nome": "ortega", "idade": "54", "materia": "sql",
            "observacoes": "legal"
        }
        requests.post(f"{URL_Base}/api/professor", json=dados)
        resposta = requests.delete(f"{URL_Base}/api/professor/1")
        self.assertEqual(resposta.status_code, 200)
        resposta_lista = requests.get(f"{URL_Base}/api/professor").json()['professores']
        self.assertTrue(all(professor['nome'] == 'ortega' for professor in resposta_lista))

    def test_104_put_edita_professor(self):
        dados = {
            "nome": "ortega", "idade": "54", "materia": "sql",
            "observacoes": "legal"
        }
        dados_alterados = {
            "nome": "ortega", "idade": "62", "materia": "sql",
            "observacoes": "legal"
        }
        requests.post(f"{URL_Base}/api/professor", json=dados)
        resposta = requests.put(f"{URL_Base}/api/professor/2", json=dados_alterados)
        self.assertEqual(resposta.status_code, 200)
        resposta_get = requests.get(f"{URL_Base}/api/professor/2")
        self.assertEqual(resposta_get.json()['idade'], '62')

    def test_106_get_professor_inexistente(self):
        resposta = requests.get(f"{URL_Base}/api/professor/99")
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json(), {"mensagem": "Professor não encontrado"})

    def test_107a_post_professor_sem_nome(self):
        dados = {
            "nome": "", "idade": "54", "materia": "sql",
            "observacoes": "legal"
        }
        resposta = requests.post(f"{URL_Base}/api/professor", json=dados)
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("nome", resposta.json()['mensagem'])
    # Teste turma
    def test_200_get_lista_turmas(self):
        resposta = requests.get(f"{URL_Base}/api/turma")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json()['turmas'], list)

    def test_202_get_turma_por_id(self):
        dados = {
            "descricao": "Turma A", "professor_id": "1",
            "ativo": "true"
        }
        requests.post(f"{URL_Base}/api/turma", json=dados)
        resposta = requests.get(f"{URL_Base}/api/turma/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), dict)

    def test_201_post_cria_turma(self):
        dados = {
            "descricao": "Turma A", "professor_id": "1",
            "ativo": "true"
        }
        resposta = requests.post(f"{URL_Base}/api/turma", json=dados)
        self.assertEqual(resposta.status_code, 201)
        self.assertIn(resposta.json(), requests.get(f"{URL_Base}/api/turma").json()['turmas'])

    def test_203_delete_turma(self):
        dados = {
            "descricao": "Turma A", "professor_id": "1",
            "ativo": "true"
        }
        requests.post(f"{URL_Base}/api/turma", json=dados)
        resposta = requests.delete(f"{URL_Base}/api/turma/1")
        self.assertEqual(resposta.status_code, 200)
        resposta_lista = requests.get(f"{URL_Base}/api/turma").json()['turmas']
        self.assertTrue(all(turma['descricao'] == 'Turma A' for turma in resposta_lista))

    def test_204_put_edita_turma(self):
        dados = {
            "descricao": "Turma A",
            "professor_id": "1",
            "ativo": "ativo"
        }
        dados_alterados = {
            "descricao": "Turma B", "professor_id": "2",
            "ativo": "false"
        }
        resposta1 = requests.post(f"{URL_Base}/api/turma", json = dados)
        self.assertEqual(resposta1.status_code, 201)
        resposta = requests.put(f"{URL_Base}/api/turma/2", json=dados_alterados)
        self.assertEqual(resposta.status_code, 200)
        resposta_get = requests.get(f"{URL_Base}/api/turma/2")
        self.assertEqual(resposta_get.json(), {'ativo': 'false', 'descricao': 'Turma B', 'id': 2, 'professor_id': '2'})

    def test_206_get_turma_inexistente(self):
        resposta = requests.get(f"{URL_Base}/api/turma/99")
        self.assertEqual(resposta.status_code, 404)
        self.assertEqual(resposta.json(), {"mensagem": "Turma não encontrada"})

    def test_207a_post_turma_sem_descricao(self):
        dados = {
            "descricao": "", "professor_id": "1",
            "ativo": "true"
        }
        resposta = requests.post(f"{URL_Base}/api/turma", json=dados)
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("descricao", resposta.json()['mensagem'])
 
 


if __name__ == "__main__":
    unittest.main()