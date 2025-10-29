from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

def test_navegacion(login_in_driver):
    try:
        driver = login_in_driver
        
        #Validacion titulos
        assert driver.title == "Swag Labs"


        #Encontrar elementos
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(productos)>0, "No hay productos"
        
        #verificar botones/elementos
        EC.presence_of_element_located((By.ID,"react-burger-menu-btn"))
        EC.presence_of_element_located((By.CLASS_NAME,"product-sort-container"))

        print("TEST OK") 

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise 
    finally:
        driver.quit()#indep de si falla o no la prueba 
