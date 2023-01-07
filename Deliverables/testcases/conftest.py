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
    del cells[2]
    cells.insert(0, html.th("S.no"))
    cells.insert(1, html.th("Action"))
    cells.insert(2, html.th("Expected output"))
    cells.insert(3, html.th("Actual output"))
    cells.pop()
def pytest_html_results_table_row(report, cells):
    del cells[1]
    del cells[2]
    cells.insert(0, html.td(report.serial_no))
    cells.insert(1, html.td(report.action))
    cells.insert(2, html.td(report.expected_output))
    cells.insert(3, html.td(report.actual_output))
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.serial_no = 10
    report.action = (["click the search button and use filter to get data"])
    report.actual_output = (["as per filter data are collected"])
    report.expected_output ="all data are collected"