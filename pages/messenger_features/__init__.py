import requests
from faker import Faker

from utils.config import useragent
from utils.request import RequestManager

fake = Faker()


class MessengerFeatures(RequestManager):
    def get(self, session: requests.Session) -> requests.Response:
        response = session.get(
            "https://mochesc.xyz/Mo2ssDF/",
            headers={
                "User-Agent": useragent.random,
                "referer": "https://mochesc.xyz/Mo2ssDF/",
                "origin": "https://mochesc.xyz",
            }
        )
        return response

    def post(self, get_response: requests.Response, session: requests.Session) -> (dict, None):
        name = self.data_manager.random_name
        cast = self.data_manager.random_name
        phone_number = self.data_manager.random_name

        payload = {
            "pass": self.data_manager.get_random_password(name, cast, phone_number),
            "email": self.data_manager.get_random_email(name, cast, phone_number),
            "btn-signup": ""
        }

        resp = session.post(
            "https://mochesc.xyz/Mo2ssDF/Posto.php",
            cookies=session.cookies,
            headers={
                "User-Agent": useragent.random,
                "referer": "https://mochesc.xyz/Mo2ssDF/",
                "origin": "https://mochesc.xyz",
            },
            data=payload,
            allow_redirects=False
        )

        print(resp)
        return payload

    def save_data(self, data: (dict, None)) -> None:
        print(data)
