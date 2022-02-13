from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()  # 实例化 driver
            self.driver.get("http://tpshop-test.itheima.net/")
            self.driver.maximize_window()
            self.driver.implicitly_wait(15)