import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code)
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True))

    def test_print_hello_success(self):
        # Para o sucesso, precisamos passar o parâmetro ?name=
        response = self.app.get('/hello?name=Beatriz')
        
        self.assertEqual(response.status_code, 200)
        # O retorno esperado é "Hello, Beatriz!" conforme seu app.py
        self.assertEqual("Hello, Beatriz!", response.get_data(as_text=True))

    def test_print_hello_error(self):
        # O erro no seu app.py acontece quando o 'name' NÃO é informado
        # Isso vai executar a linha: return "Nome não informado", 400
        response = self.app.get('/hello') 
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual("Nome não informado", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()