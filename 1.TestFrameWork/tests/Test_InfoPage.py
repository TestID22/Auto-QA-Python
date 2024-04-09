import random

from BaseTest import BaseTest
class Test_InfoPage(BaseTest):


    def test_logining(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.change_name(f"Vitalii was here {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()