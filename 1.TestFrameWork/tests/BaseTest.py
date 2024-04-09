import pytest

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.PersonalPage import PesrsonalPage
from config.Data import Data

class BaseTest:

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_Page: PesrsonalPage
    data: Data
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard = DashboardPage(driver)
        request.cls.personal_page = PesrsonalPage(driver)
        request.cls.data = Data()
