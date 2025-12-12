from selenium import webdriver
from selenium.webdriver.common.by import By 
import pytest


from pages.login_page import LoginPage
#importamos faker
from faker import Faker
#inicializamos
fake = Faker()

@pytest.mark.parametrize("usuario,password,debe_funcionar",[
     (fake.user_name(),fake.password(length=8),False),
     (fake.user_name(),fake.password(),False),
])
def test_login_vali(login_in_driver,usuario,password,debe_funcionar):
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        if debe_funcionar == True:
            assert '/inventory.html' in driver.current_url, "No se redirigió." 
        elif debe_funcionar == False: 
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "el mensaje no se está ejecutando"