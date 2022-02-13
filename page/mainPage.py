from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.loginPage import LoginPage


class MainPage(BasePage):
    def __init__(self, driver = None):
        super().__init__(driver)

    # def goto_calendar(self):
    #     self.driver.find_element_by_xpath('//*[@class="_pp-product-container"]').click()
    #     self.driver.find_element_by_xpath('//*[@title="日历"]').click()
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     return CalendarPage(self.driver)

    # 进入登录页面
    def goto_login(self):
        self.driver.find_element(By.XPATH, '//*[text()="登录"]').click()
        return LoginPage(self.driver)

    # # 验证是否已经登录
    # def is_login(self):
    #     ele = self.driver.find_element('//*[text()="安全退出"]')
    #     if ele:
    #         return True
    #     return False