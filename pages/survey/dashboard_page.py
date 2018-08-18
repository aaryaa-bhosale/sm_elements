from base.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _create_survey_link = "//a[contains(@class,'create-survey')]"
    _create_from_scratch_button= "scratch"
    _survey_title = "surveyTitle"

    _survey_category_dropdown = "//div[@class='Select-placeholder']"
    _select_survey_category = "react-select-2--option-4"
    _modal_create_survey_button = "//button[text()='CREATE SURVEY']"

    def click_create_survey_button(self):
        self.element_click(self._create_survey_link, locator_type="xpath")

    def click_create_from_scratch_button(self):
        self.element_click(self._create_from_scratch_button, locator_type="id")

    def enter_survey_name(self, survey_title):
        self.wait_for_element(locator=self._survey_title,locator_type="id", pollFrequency=1)
        self.send_keys(survey_title, self._survey_title)

    def select_survey_category(self):
        self.element_click(self._survey_category_dropdown,locator_type="xpath")
        self.element_click(self._select_survey_category, locator_type="id")


    def survey_modal_window(self,survey_title):
        self.enter_survey_name(survey_title)
        self.select_survey_category()
        self.wait_for_element(locator=self._modal_create_survey_button, locator_type="xpath", pollFrequency=1)
        self.element_click(self._modal_create_survey_button, locator_type="xpath")


    def nav_to_create_survey(self):
        self.click_create_survey_button()
        self.click_create_from_scratch_button()
        self.survey_modal_window("My First Survey")

