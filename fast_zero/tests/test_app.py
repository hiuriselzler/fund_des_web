#Por convenção, todos os arquivos de teste do pytest devem iniciar com um prefixo test_.py

from fastapi.testclient import TestClient
from fast_zero.app import app
from http import HTTPStatus

def test_deve_retornar_ok_e_olá_mundo():
    Client = TestClient(app)

    response = Client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message":"Olá Mundo!"}