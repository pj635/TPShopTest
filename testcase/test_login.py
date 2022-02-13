import pytest
import yaml

from page.mainPage import MainPage


class TestLogin:

    def setup(self):
        self.loginPage = MainPage().goto_login()


    def teardown(self):
        self.loginPage.driver.quit()   # 用例执行完成，退出浏览器

    # 登录成功的测试用例
    @pytest.mark.parametrize('login_dic', yaml.safe_load(open("./login.yaml", "r", encoding='utf-8'))['login_success'])
    def test_login_success(self, login_dic):

        res = self.loginPage.login_success(login_dic['username'], login_dic['passwd'], login_dic['verifycode'])
        assert res == True

    # 登录失败的测试用例
    @pytest.mark.parametrize('login_dic', yaml.safe_load(open("./login.yaml", "r", encoding='utf-8'))['login_fail'])
    def test_login_fail(self, login_dic):
        res = self.loginPage.login_fail(login_dic['username'], login_dic['passwd'], login_dic['verifycode'])
        assert res == login_dic['result']