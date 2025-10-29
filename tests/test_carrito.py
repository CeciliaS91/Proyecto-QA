from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time 

def test_carrito(login_in_driver):
    
    try:
        driver = login_in_driver

        #Vuelvo a controlar que haya elementos
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(productos)>0, "No hay productos"

        #Verificar carrito
        productos[0].find_element(By.TAG_NAME,"button").click()
        time.sleep(3)
        carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link").text

        print("TEST OK") 

    except Exception as e:
        print(f"Error en test_carrito: {e}")
        raise 
    finally:
        driver.quit()#indep de si falla o no la prueba 