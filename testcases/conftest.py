import time

import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    serv_obj = Service("/home/cb/Downloads/webdrivers/chromedriver")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://keycloak-gbs-dev.trutesta.io/auth/realms/Intertek/protocol/openid-connect/auth?client_id=trutesta&redirect_uri=https%3A%2F%2Fintertek-dev.trutesta.io%2Fclient-deliverables%2F&state=5f2ac612-591b-4093-8da6-0bfa588e6394&response_mode=fragment&response_type=code&scope=openid&nonce=36286562-79b4-4a0c-8aef-2d25648363e9")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

#this used to change the title of html test report
def pytest_html_report_title(report):
    report.title = "Truetesta Test report"
# this is used to modify the test result of html report
def pytest_html_results_table_header(cells):
    del cells[1]
    cells.insert(0, html.th("S.NO"))
    cells.insert(1, html.th("ACTION"))
    cells.insert(2, html.th("EXPECTED OUTPUT"))
    cells.insert(3, html.th("ACTUAL OUTPUT"))
    cells.insert(4, html.th("TEST RESULT"))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(0, html.td())
    cells.insert(1, html.td())
    cells.pop()


