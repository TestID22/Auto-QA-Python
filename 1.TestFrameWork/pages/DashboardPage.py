import allure

from config.links import Links
from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE
    MY_INFO_Button = ("xpath", "//span[text()='My Info']")
    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_Button)).click()
        