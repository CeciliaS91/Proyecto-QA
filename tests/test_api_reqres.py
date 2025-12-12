import requests
import pytest
from utils.logger import logger

#obtener usuario
def test_get_user(url_base,header_request):
    logger.info(f"Realizando solicitud GET a {url_base}")
    response = requests.get(f"{url_base}/2",headers=header_request)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200

    data = response.json()

    logger.info("Validando el id dentro del usuario")
    assert data["data"]["id"] == 2 #me aseguro que al usuario que estoy accediendo es el 2

#crear usuario
def test_create_user(url_base,header_request):
    payload={
        "name": "Jose",
        "job": "profesor"
    } 
    response = requests.post(url_base,headers=header_request,json=payload)

    assert response.status_code == 201

    data = response.json()

    #verificar que el nombre de la rta sea el mismo que el enviado
    assert data["name"] == payload["name"]

    #verificar que la rta tenga un id
    assert "id" in data 

#eliminar usuario
def test_delete_user(url_base,header_request):
    response = requests.delete(f"{url_base}/2",headers=header_request)

    assert response.status_code == 204 