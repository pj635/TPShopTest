from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()  # 实例化driver，打开一个浏览器
            self.driver.get("http://tpshop-test.itheima.net/")
            self.driver.maximize_window()
            self.driver.implicitly_wait(15)
