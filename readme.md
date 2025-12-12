# Proyecto de Talento Tech

## Proposito del proyecto
El proyecto tiene como objetivo automatizar pruebas de UI y de API para el sitio **SauceDemo**, aplicando practicas como Page Object Model, manejo de datos externos, generacion de reportes HTML, logging, hooks y captura automatica de pantalla.

## Tecnologias utilizadas
- Python 3.x
- Pytest
- Selenium WebDriver
- Logging
- Faker
- CSV / JSON
- Request
Para iniciar la ejecucion de las pruebas con todas las dependencias a instalar se debe ejecutar la siguiente linea:

```bash
py -m pip install -r requirements.txt
```

## Reportes y Logs

El proyecto genera tres tipos principales de resultados durante la ejecucion de las prubas: **reporte HTML**, **capturas de pantalla**, **archivo de log**

### Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```reporte.hmtl``` en la **carpeta raiz** del proyecto

### Logs de ejecución
Tambien se genera un log con informacion detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/suite.log```

### Capturas de pantalla

Se realizan capturas de pantalla por cada test que haya fallado.
Se coloca un error forzado en la prueba ```tests/test_carrito.py``` para mostrar el uso de las mismas. En caso de querer ver la prueba correspondiente a verificar que se agreguen productos al carrito se debe descomentar esa parte del código, junto con el try y el exception. 
El error se muestra en ```reporte.hmtl```.

## Ejecutar todas las pruebas
Para iniciar la ejecucion de las pruebas debes ejecutar la siguiente linea:

```bash
python -m run_test.py
```

## ¿Como interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la pagina de inventario
- Comportamiento de la pagina del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios validos o invalidos
    - `productos.json` -> datos de productos para validacion

### Conclusion
El proyecto permite integrar conocimientos del lenguaje Python junto con la automatización de pruebas a partir de una página demo. Incluye el flujo de ejecución `run_test.py` para la generación automática de reporte HTML.
Presenta los primeros pasos para la generación de distintos tipos de pruebas junto con sus respectivas capturas y logs para llevar un registro claro de los posibles errores, y los pasos ya ejecutados.
El archivo definitivo de la entrega es el commit llamado "commit final" que incluye las ultimas lineas de este readMe.