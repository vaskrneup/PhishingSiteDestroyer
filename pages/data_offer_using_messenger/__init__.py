import requests
from bs4 import BeautifulSoup
from faker import Faker

from utils.config import useragent
from utils.request import RequestManager

fake = Faker()


class DataOffer(RequestManager):
    def get(self, session: requests.Session) -> requests.Response:
        response = session.get(
            "https://kfbmss.xyz/messenger/60cb22a68b43a",
            headers={
                "User-Agent": useragent.random,
                "referer": "https://kfbmss.xyz/messenger/60cb22a68b43a",
                "origin": "https://kfbmss.xyz",
            }
        )
        return response

    def post(self, get_response: requests.Response, session: requests.Session) -> (dict, None):
        token = BeautifulSoup(get_response.text, "lxml").select("input[name=_token]")[0].attrs.get("value")

        name = self.data_manager.random_name
        cast = self.data_manager.random_name
        phone_number = self.data_manager.random_name

        payload = {
            "password": self.data_manager.get_random_password(name, cast, phone_number),
            "email": self.data_manager.get_random_email(name, cast, phone_number)
        }

        resp = session.post(
            "https://kfbmss.xyz/save_data/60cb22a68b43a",
            cookies=session.cookies,
            headers={
                "referer": "https://kfbmss.xyz/messenger/60cb22a68b43a",
                "origin": "https://kfbmss.xyz",
                "content-type": "application/x-www-form-urlencoded",
                "User-Agent": self.useragent.random
            },
            data={
                "_token": token,
                "type": "messenger",
                **payload
            }
        )

        print(resp)
        return payload

    def save_data(self, data: (dict, None)) -> None:
        print(data)
