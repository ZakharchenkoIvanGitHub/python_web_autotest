import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def selector_input_login():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def selector_input_password():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def selector_button():
    return "button"

@pytest.fixture()
def selector_error():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def selector_blog():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.close_dr()



