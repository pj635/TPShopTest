from selenium.webdriver.common.by import By
from page.basePage import BasePage
from page.loginPage import LoginPage


class MainPage(BasePage):
    def __init__(self, driver = None):
        super().__init__(driver)

    # 进入登录页面
    def goto_login(self):
        self.driver.find_element(By.XPATH, '//*[text()="登录"]').click()
        return LoginPage(self.driver)