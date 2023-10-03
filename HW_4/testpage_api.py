import logging
import requests
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)


def get_data_posts(token, params=None):
    if token:
        try:
            response = requests.get(data["url_posts"],
                                    headers={"X-Auth-Token": token},
                                    params=params)
        except:
            logging.exception("Exception request get data posts")
        else:
            if response.status_code == 200:
                logging.debug("Data posts successfully received")
                return response.json()
            else:
                logging.error(f"Status code {response.status_code} get data posts")
    else:
        logging.error(f"Token not received")


def test_create_post(login, title, description, content):
    try:
        response = requests.post(data["url_posts"],
                                 headers={"X-Auth-Token": login},
                                 data={'title': title,
                                       'description': description,
                                       'content': content})
    except:
        logging.exception("Exception create post")
    else:
        if response.status_code == 200:
            logging.debug(f"Post {title} was successfully published")
            return True
        else:
            logging.error(f"Post not created. Status code {response.status_code} ")
