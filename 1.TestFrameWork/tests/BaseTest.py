import pytest

from pages import LoginPage
from pages import DashboardPage
from pages import PersonalPage


class BaseTest:

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_Page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard = DashboardPage(driver)
        request.cls.login_page = PersonalPage(driver)

