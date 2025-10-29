import pytest

#Lista de archivos de pruebas
test_files = [
    "tests/test_login.py",
    "tests/test_navegacion.py",
    "tests/test_carrito.py"
]
#Argumentos para ejecutar las pruebas: archivos + reportes
pytest_args = test_files + ["--html=reporte.html","--self-contained-html", "-v"]
pytest.main(pytest_args)