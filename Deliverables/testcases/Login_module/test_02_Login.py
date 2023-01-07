import time
import pytest

from Deliverables.pages.trutesta_login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestCredential_2():
    def test_userLogin_withCorrectUsernameAndInCorrectPass(self):
        lp = LoginPage(self.driver)
        lp.username_clear()
        lp.password_clear()
        lp.username("robyn.hills@sematree.com")
        lp.password("*Welcome&Tech202")
        lp.login()
        time.sleep(3)
        if self.driver.title != "TruTesta™ Deliverables":
           print("incorrect password passed successfully")
        else:
           print("testcase failed!!!")