import requests
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)


class OperationsHelper():
    def get_not_me(token):
        resource = requests.get(data["url_posts"],
                                headers={"X-Auth-Token": token},
                                params={"owner": "notMe"})
        return resource.json()

    def get_me(token):
        resource = requests.get(data["url_posts"],
                                headers={"X-Auth-Token": token},
                                )
        return resource.json()
