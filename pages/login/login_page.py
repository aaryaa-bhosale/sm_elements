from base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "LOG IN"
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[contains(@type,'submit')]"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    def do_login(self, email="", password=""):
        self.click_login_link()
        self.clear_field(locator=self._email_field)
        self.enter_email(email)
        self.clear_field(locator=self._password_field)
        self.enter_password(password)
        self.click_login_button()
