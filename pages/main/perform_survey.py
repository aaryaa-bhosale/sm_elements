from base.webdriver import WebDriver
from base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.survey.dashboard_page import DashboardPage
from pages.survey.create_survey_page import CreateSurveyPage
import time

class PerformSurvey():

    def __init__(self):
        web_driver = WebDriver()
        self.driver = web_driver.get_web_driver_instance()


    def add_survey(self):
        # Do login to survey monkey
        lp = LoginPage(self.driver)
        lp.do_login("mangesh.khude","infoserver123")
        db = DashboardPage(self.driver)
        db.nav_to_create_survey()
        time.sleep(5)
        cs = CreateSurveyPage(self.driver)
        cs.create_survey()


ps = PerformSurvey()
ps.add_survey()