import time

from testpage import OperationsHelper
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# def test_step1(browser):
#    logging.info("Test1 Starting")
#    test_page = OperationsHelper(browser)
#    test_page.go_to_site()
#    test_page.enter_login("test")
#    test_page.enter_pass("test")
#    test_page.click_login_button()
#
#    assert test_page.get_error_text() == "401"
#
#
# def test_step2(browser):
#    logging.info("Test2 Starting")
#    test_page = OperationsHelper(browser)
#    test_page.go_to_site()
#    test_page.enter_login(testdata["login"])
#    test_page.enter_pass(testdata["password"])
#    test_page.click_login_button()
#    test_page.get_blog()
#    assert test_page.get_blog() == "Blog"

def test_step3(browser):
    logging.info("Test3 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()
    test_page.click_contact()
    test_page.enter_name("IVAN")
    test_page.enter_email("sqasasa@sedswd.ru")
    test_page.enter_content("ddasdasdsdewerfw4erewrerwe")
    test_page.click_button_contact_as()
    assert test_page.go_alert() == 'Form successfully submitted'
