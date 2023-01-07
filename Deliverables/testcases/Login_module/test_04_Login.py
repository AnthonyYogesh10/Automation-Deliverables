import time
import pytest

from Deliverables.pages.trutesta_login_page import LoginPage

# 04 log in with incorrect username and incorrect password
@pytest.mark.usefixtures("setup")
class TestCredential_04():
   def test_userLogin_withInCorrectUsernameAndInCorrectPass(self):
     lp = LoginPage(self.driver)
     lp.username_clear()
     lp.password_clear()
     lp.username("robyn.hills@sematree")
     lp.password("*Welcome&Tech202")
     lp.login()
     time.sleep(3)
     if self.driver.title != "TruTesta™ Deliverables":
       print("incorrect username and password passed successfully")
     else:
       print("testcase failed!!!")


