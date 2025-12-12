from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        inventory_page = InventoryPage(driver)

        #verificar que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "Inventario vacio"

        #verificar carrito vacio al inicio
        assert inventory_page.obtener_conteo_carrito() == 0

        #Agregar el primer producto
        inventory_page.agregar_primer_producto()
        
        #verificar el contador del carrito
        assert inventory_page.obtener_conteo_carrito()==1 

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise 
    finally:
        driver.quit()#indep de si falla o no la prueba 