from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_INPUT_LOGIN = (By.XPATH, """//span[text() = 'Username']/following::input[@type= 'text'][1]""")
    LOCATOR_INPUT_PASSWORD = (By.XPATH, """//span[text() = 'Password']/following::input[@type= 'password'][1]""")
    LOCATOR_BUTTON = (By.XPATH, """//button[@type= 'submit']""")
    LOCATOR_ERROR = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_BLOG = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE = (By.XPATH, """//button[@id="create-btn"]""")
    LOCATOR_TITLE_CREATE = (By.XPATH, """//span[text() = 'Title']/following::input[@type= 'text'][1]""")
    LOCATOR_DESCRIPTION_CREATE = (By.XPATH, """//span[text() = 'Description']//following::textarea[1]""")
    LOCATOR_CONTENT_CREATE = (By.XPATH, """//span[text() = 'Content']//following::textarea[1]""")
    LOCATOR_TITLE_PUBLIC = (By.XPATH, """//h1[@class ='svelte-tv8alb']""")
    LOCATOR_CONTENT_PUBLIC = (By.XPATH, """//div[@class = 'content svelte-tv8alb']""")
    LOCATOR_INPUT_FILE = (By.XPATH, """// input[ @type = 'file']""")
    LOCATOR_CONTACT = (By.XPATH, """// a[text() = 'Contact']""")
    LOCATOR_DESCRIPTION_NAME = (By.XPATH, """// span[text() = 'Your name'] // following::input[1]""")
    LOCATOR_DESCRIPTION_EMAIL = (By.XPATH, """// span[text() = 'Your email'] // following::input[1]""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_LOGIN[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_LOGIN)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_PASSWORD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_PASSWORD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_NAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_EMAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_EMAIL)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_CREATE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CREATE)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR[1]}")
        return text

    def get_blog(self):
        blog = self.find_element(TestSearchLocators.LOCATOR_BLOG)
        text = blog.text
        logging.info(f"Нашли текст *{text}* локатор Блог  ")
        return text

    def click_create_button(self):
        logging.info("Click create button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE).click()

    def click_input_file(self):
        logging.info("Click input file button")
        self.find_element(TestSearchLocators.LOCATOR_INPUT_FILE).click()

    def click_contact(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def click_button_contact_as(self):
        logging.info("Click button contact as")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON).click()

    def go_alert(self):
        logging.info("Go_alert")
        alert = self.get_alert()
        text = alert.text
        logging.info(f"Alert text '{text}'")
        alert.accept()
        return text
