import pytest
import time

from pages.trutesta_login_page import LoginPage

# 03 log in with incorrect username and correct password
@pytest.mark.usefixtures("setup")
class TestCredential_03():
   def test_userLogin_withInCorrectUsernameAndCorectPass(self):
     lp = LoginPage(self.driver)
     lp.username_clear()
     lp.password_clear()
     lp.username("robyn.hills@sematree") #incorrect username
     lp.password("*Welcome&Tech2022")
     lp.login()
     time.sleep(3)
     if self.driver.title !="TruTesta™ Deliverables":
      print("incorrect username passed successfully")
     else:
       print("testcase failed!!!")