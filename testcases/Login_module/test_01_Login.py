import time
import pytest

from pages.trutesta_login_page import LoginPage

@pytest.mark.usefixtures("setup") # i wasted time here without using the @ symbol
class TestCredentials():
# 01 log in with correct username and correct password
     def test_userLogin_withCorrectUsernameAndCorrectPass(self):
        lp = LoginPage(self.driver)
        lp.username("robyn.hills@sematree.com")
        lp.password("*Welcome&Tech2022")
        lp.login()
        time.sleep(10)
        if self.driver.title == "TruTesta™ Deliverables":
          print("Correct username and password passed successfully")
        else:
          print("testcase failed!!!")











