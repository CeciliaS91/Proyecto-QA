import pytest

#Lista de archivos de pruebas
test_files = [
    "tests/test_login.py",
    "tests/test_carrito.py",
    "tests/test_inventory.py",
    "tests/test_cart_json.py",
    "tests/test_api_reqres.py"
]
#Argumentos para ejecutar las pruebas: archivos + reportes
pytest_args = test_files + ["--html=reporte.html","--self-contained-html", "-v"]
pytest.main(pytest_args)