from selenium import webdriver
from selenium.webdriver.common.by import By 
import pytest

#Validacion de login con credenciales
def test_login_vali(login_in_driver):
    try:
        driver = login_in_driver

        #Validacion de la redirección de la página
        assert '/inventory.html' in driver.current_url, "No se redirigió." 
    
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    
    finally:
        driver.quit()
    