from base.base_page import BasePage
from base.sample_data_reader import SampleDataReader
import time


class CreateSurveyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.sample_data = SampleDataReader(filename = "test_data.ini")
        self.sample_data.sample_data_read()

    #Locators
    _logo=""
    _question_title = '//div[@id="questionTitleWrap"]//div[@id="editTitle"]'
    _change_question_type='changeQType'
    _single_textbox = "//li[@class='add-q-menu-container']//a[text()='Single Textbox']"
    _multi_textbox = "//li[@class='add-q-menu-container']//a[text()='Comment Box']"
    _rating_scale = "//li[@class='add-q-menu-container']//a[text()='Star Rating']"
    _date_picker = "//li[@class='add-q-menu-container']//a[text()='Date / Time']"

    _save_question_button='//div[@id="editQuestion"]//section[@class="t1"]//div[@class="buttons"]//a[text()="SAVE"]'

    _new_question_link='//a[.="NEW QUESTION"]'

    def add_logo(self):
        print("add logo")

    def add_page_title(self):
        print("add page title")

    def add_question_type(self,question_type='textbox'):
        self.element_click(self._change_question_type, locator_type="id")

        if question_type == "textbox":
            self.element_click(self._single_textbox, locator_type="xpath")
            print("textbox question type selected")
        elif question_type == "multi_textbox":
            self.element_click(self._multi_textbox, locator_type="xpath")
            print("multi_textbox question type selected")
        elif question_type == "rating_scale":
            self.element_click(self._rating_scale, locator_type="xpath")
            print("rating_scale question type selected")
        elif question_type == "date_picker":
            self.element_click(self._date_picker, locator_type="xpath")
            print("date_picker question type selected")
        else:
            print("invalid question_type given")

    def add_new_question(self):
        time.sleep(5)
        self.element_click(self._new_question_link, locator_type="xpath")
        time.sleep(5)


    def add_que_1(self):
        print("Add question 1")
        question_title_data = self.sample_data.get_sample_data('Question_1', 'text')
        question_title_input_box = self.wait_for_element(locator=self._question_title, locator_type="xpath", pollFrequency=0.5)
        question_title_input_box.send_keys(question_title_data)

        self.add_question_type("textbox")
        self.element_click(self._save_question_button, locator_type="xpath")

    def add_que_2(self):
        print("Add question 2")


    def add_que_3(self):
        print("Add question 3")

        question_title_data = self.sample_data.get_sample_data('Question_3', 'text')
        question_title_input_box = self.wait_for_element(locator=self._question_title, locator_type="xpath",
                                                         pollFrequency=0.5)
        question_title_input_box.send_keys(question_title_data)

        self.add_question_type("date_picker")
        self.element_click(self._save_question_button, locator_type="xpath")

    def add_que_4(self):
        print("Add question 4")

        question_title_data = self.sample_data.get_sample_data('Question_4', 'text')
        question_title_input_box = self.wait_for_element(locator=self._question_title, locator_type="xpath",
                                                         pollFrequency=0.5)
        question_title_input_box.send_keys(question_title_data)

        self.add_question_type("rating_scale")
        self.element_click(self._save_question_button, locator_type="xpath")

    def add_que_5(self):
        print("Add question 5")


    def add_que_6(self):
        print("Add question 6")


    def add_que_7(self):
        print("Add question 7")


    def add_que_8(self):
        print("Add question 8")
        question_title_data = self.sample_data.get_sample_data('Question_8', 'text')
        question_title_input_box = self.wait_for_element(locator=self._question_title, locator_type="xpath", pollFrequency=0.5)
        question_title_input_box.send_keys(question_title_data)

        self.add_question_type("multi_textbox")
        self.element_click(self._save_question_button, locator_type="xpath")

    def add_que_9(self):
        print("Add question 9")

    def add_que_10(self):
        print("Add question 10")

    def create_survey(self):
        print("I am at create survey")
        self.add_que_1()
        self.add_new_question()

        self.add_que_3()
        self.add_new_question()

        self.add_que_4()
        self.add_new_question()

        self.add_que_8()
