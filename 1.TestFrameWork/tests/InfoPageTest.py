from BaseTest import BaseTest
class Test_InfoPage(BaseTest):


    def test_logining(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
