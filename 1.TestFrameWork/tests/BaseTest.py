import pytest

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.PersonalPage import PesrsonalPage
from config.Data import Data

class BaseTest:
    #todo: add allure
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PesrsonalPage
    data: Data
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PesrsonalPage(driver)
        request.cls.data = Data()
