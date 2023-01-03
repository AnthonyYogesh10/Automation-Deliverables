import time

from selenium.webdriver.common.by import By
from  selenium import webdriver

class HomePage():
    def __init__(self,driver):
        self.driver = driver
#to select menu bar in header
    def menu_bar(self):
       menu =  self.driver.find_element(By.XPATH,"//i[@class='fas fa-bars fa-2x']")
       menu.click()
# to select home_button in header
    def home_button(self):
        home =  self.driver.find_element(By.XPATH,"//i[@class='fa fa-home fa-lg']")
        home.click()
# to select report_inspector_button in header
    def report_inspector_button(self):
        report_Inspector =  self.driver.find_element(By.XPATH,"//i[@class='fa fa-clipboard-check fa-lg']")
        report_Inspector.click()
# to select upload_button in header
    def upload_button(self):
        upload =  self.driver.find_element(By.XPATH,"//i[@class='fas fa-leaf']")
        upload.click()
# to select deliverable_alerts_button in header
    def deliverable_alerts_button(self):
        deliverable_alerts =  self.driver.find_element(By.XPATH,"//i[@class='fa fa-exclamation-triangle fa-lg']")
        deliverable_alerts.click()
# to select help_button in header
    def help_button(self):
        help =  self.driver.find_element(By.XPATH,"//i[@class='fa fa-question-circle fa-lg']")
        help.click()
# to select user_button in header
    def user_button(self):
        user =  self.driver.find_element(By.XPATH, "//div[@class='dropdown ng-tns-c35-0 ng-star-inserted']//button[@id='dropdownMenuButton']")
        user.click()
# to select notification_button in header
    def notification_button(self):
        notification =  self.driver.find_element(By.XPATH, "//i[@class='fas fa-bell']")
        notification.click()
#to click select input box
    def search_inputBox(self,search_values):
        searchBox = self.driver.find_element(By.XPATH,"//input[@id='quick-search']")
        searchBox.click()
        searchBox.send_keys(search_values)
#used to click search button
    def search_button(self):
        search_buttons = self.driver.find_element(By.XPATH,"//i[@class='fa fa-search']")
        search_buttons.click()
#to click show_drop_down
    def show_filter_button(self):
        show = self.driver.find_element(By.XPATH,"//div[@class='dropdown ng-tns-c35-1 ng-star-inserted']//button[@id='dropdownMenuButton']")
        show.click()
    def show_drop_downs(self,filter_per_page_value):
        drop_downs = self.driver.find_elements(By.XPATH,"//ul[@class='dropdown-menu ng-tns-c35-1']/li/a")
        for drop_down in drop_downs:
            if drop_down.text == filter_per_page_value:
                drop_down.click()
                break
    def all_data(self,no_of_datas):
        datas = self.driver.find_elements(By.XPATH,"//div[@id='mid-list']/a")
        length_of_datas = len(datas)
        #print(length_of_datas)
        if length_of_datas == no_of_datas:
            print("All datas are arrived successfully!!!")
        else:
             print("Datas are not arrived")

