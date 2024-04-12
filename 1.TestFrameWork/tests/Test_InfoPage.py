import allure
import pytest

from BaseTest import BaseTest
@allure.feature("My infor tests")
class TestInfoPage(BaseTest):
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_logining(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.change_name("Vitalii test")
        self.personal_page.save_changes()
        self.personal_page.make_screenshot("Success")
        #self.personal_page.is_changes_saved()


