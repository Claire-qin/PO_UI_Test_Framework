# pageobject设计模块：把页面设计成一个类，页面中的控件作为属性，控件的操作作为方法。
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')

class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/zentao/user-login.html')
        self.username_inputbox = self.driver.find_element(By.XPATH,'//input[@name="account"]') #属性：控件
        self.password_inputbox = self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.login_button = self.driver.find_element(By.XPATH,'//button[@id="submit"]')
        self.keeplogin_checkbox = self.driver.find_element(By.XPATH,'//input[@name="keepLogin[]"]')
        self.forgetpassword_link = None

    def input_username(self,username): #方法：操作
        self.username_inputbox.send_keys(username)
    def input_password(self,password):
        self.password_inputbox.send_keys(password)
    def click_login(self):
        self.login_button.click()

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
