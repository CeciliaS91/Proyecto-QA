import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime 

target = pathlib.Path("reports/screens")
target.mkdir(parents=True,exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

#Page object model: una forma más modular 

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return  {"x-api-key": "reqres_7afc5d0be0884015807a069636068898"}

#creación de hook 

@pytest.hookimpl(hookwrapper=True) 
def pytest_runtest_makereport(item,call):
    outcome = yield

    report = outcome.get_result()

    if report.when in ("setup","call") and report.failed: 
        driver = item.funcargs.get("driver",None)

        if driver:
            timestamp_comun = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = target / f"{report.when}_{item.name}_{timestamp_comun}.png" 
            driver.save_screenshot(str(file_name))