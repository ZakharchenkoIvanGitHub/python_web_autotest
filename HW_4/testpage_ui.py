from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


#    for locator in locators["css"].keys():
#        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):

    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception witch click")
        logging.debug(f"Click to element {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"Ew find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_INPUT_LOGIN"], word, description="INPUT_LOGIN")

    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_INPUT_PASSWORD"], word, description="INPUT_PASSWORD")

    def enter_name(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_NAME"], word, description="INPUT_NAME")

    def enter_email(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_EMAIL"], word, description="INPUT_EMAIL")

    def enter_content(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTENT_CREATE"], word, description="INPUT_CREATE")

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BUTTON"], description="login")

    def click_create_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE"], description="create")

    def click_input_file(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_INPUT_FILE"], description="input file")

    def click_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT"], description="contact")

    def click_button_contact_as(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BUTTON"], description="contact as")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR"], description="error_text")

    def get_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_BLOG"], description="text_blog")

    def go_alert(self):
        logging.info("Go_alert")
        alert = self.get_alert()
        text = alert.text
        logging.info(f"Alert text '{text}'")
        alert.accept()
        return text
