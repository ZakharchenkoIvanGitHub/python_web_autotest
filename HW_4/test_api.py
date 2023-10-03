import logging

import yaml

from testpage_api import get_data_posts, test_create_post

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)


def test_1(login):
    logging.info("Test_api_1 Starting")
    res = get_data_posts(login, {"owner": "notMe"})
    lst = res["data"] if res else []
    assert data["find_id"] in [el["id"] for el in lst]


def test_2(login):
    logging.info("Test_api_2 Starting")
    if test_create_post(login, data["title"], data["description"], data["content"]):
        lst_description = [el["description"] for el in get_data_posts(login)["data"]]
    else:
        lst_description = []
    assert data["description"] in lst_description
