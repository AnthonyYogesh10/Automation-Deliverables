import time

import pytest

from pages.trutesta_home_page import HomePage
from pages.trutesta_login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestClick():
    def test(self):
      lp = LoginPage(self.driver)
      lp.username("robyn.hills@sematree.com")
      lp.password("*Welcome&Tech2022")
      lp.login()
      time.sleep(12)
      click = HomePage(self.driver)
      click.search_inputBox("test")
      click.search_button()
      time.sleep(10)
      click.show_filter_button()
      time.sleep(5)
      click.show_drop_downs("10 per Page")
      time.sleep(15)
      click.all_data(10)
      time.sleep(5)






