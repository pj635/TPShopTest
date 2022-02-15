from selenium.webdriver.common.by import By
from page.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver = None):
        super().__init__(driver)

    def _login(self, username, passwd, verifycode):
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passwd)
        self.driver.find_element(By.XPATH, '//*[@id="verify_code"]').send_keys(verifycode)
        self.driver.find_element(By.XPATH, '//*[@name="sbtbutton"]').click()

    def login_success(self, username, passwd, verifycode):
        self._login(username, passwd, verifycode)
        ele = self.driver.find_element(By.XPATH, '//*[text()="安全退出"]') # 如果登录成功，页面上会显示有“安全退出”控件,返回True；否则返回False
        if ele:
            return True
        return False

    def login_fail(self, username, passwd, verifycode):
        self._login(username, passwd, verifycode)
        return self.driver.find_element(By.XPATH, '//*[@class="layui-layer-content layui-layer-padding"]').text  # 返回登录失败后的提示信息

    def login_out(self):
        ele = self.driver.find_element(By.XPATH, '//*[text()="安全退出"]')
        if ele:
            ele.click()