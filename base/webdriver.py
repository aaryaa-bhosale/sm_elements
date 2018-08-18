"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import traceback
from traceback import print_stack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from base.config_reader import ConfigReader


class WebDriver():

    def __init__(self):
        """Initializes WebDriverFactory class

        :returns None:
        """
        self.config = ConfigReader(filename = "test_environment.ini")
        self.config.config_read()


    def get_web_driver_instance(self):
        """Get WebDriver Instance based on the browser configuration

        :rtype: driver
        :return: WebDriver Instance
        """


        browser = self.get_browser()
        site_url = self.get_site_url()

        if browser == 'iexplorer':
            self.driver = webdriver.Ie()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver_location = "/Users/aaryabhosale/Selenium/lib/chromedriver"
            os.environ["webdriver.chrome.driver"] = driver_location
            self.driver = webdriver.Chrome(driver_location)
        else:
            self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(site_url)
        return self.driver

    def get_site_url(self):
        """Get the app url

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        site_url =  self.config.get_configuration("SiteConfiguration", "url")
        return site_url

    def get_browser(self):
        """Get the browser name

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        browser =  self.config.get_configuration("Platform", "browser")
        return browser


    def get_username(self):
        """Get the username

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        username =  self.config.get_configuration("SiteConfiguration", "user")
        return username

    def get_password(self):
        """Get the password

        Required Parameters:
            None

        Optional Parameters:
            None

        Returns:
            None
        """
        password =  self.config.get_configuration("SiteConfiguration", "password")
        return password


    def get_by_type(self, locator_type):

        locator_type = locator_type.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
           return By.NAME
        elif locator_type == "xpath":
           return By.XPATH
        elif locator_type == "css":
           return By.CSS_SELECTOR
        elif locator_type == "class":
           return By.CLASS_NAME
        elif locator_type == "link":
           return By.LINK_TEXT
        else:
           print("Locator type " + locator_type + " not correct/supported")
           return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locatorType = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            print("Element not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            print("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            print("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locator_type)
            print_stack()

    def clear_field(self, locator="", locator_type="id"):
        """
        Clear an element field
        """
        element = self.get_element(locator, locator_type)
        element.clear()
        print("Clear field with locator: " + locator +
        " locatorType: " + locator_type)

    def wait_for_element(self, locator, locator_type="id",
                               timeout=60, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element