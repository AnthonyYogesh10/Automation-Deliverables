import time
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):  #in sugestion this shows int so careful to write init
      self.driver = driver

# input field of username and
    def username(self,username_value):
      username = self.driver.find_element(By.ID,"username")
      username.send_keys(username_value)

# input field of password
    def password(self,password_value):
      password = self.driver.find_element(By.ID,"password")
      password.send_keys(password_value)

# login button
    def login(self):
      login_button = self.driver.find_element(By.ID,"kc-login").click()

# logout button
    def logout_button(self):
      self.driver.find_element(By.XPATH,"//div[@class='dropdown ng-tns-c35-0 ng-star-inserted']//button[@id='dropdownMenuButton']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
      time.sleep(2)

 # clear the input of username
    def username_clear(self):
      username = self.driver.find_element(By.ID,"username")
      username.clear()

 # clear the input of password
    def password_clear(self):
      password = self.driver.find_element(By.ID,"password")
      password.clear()

