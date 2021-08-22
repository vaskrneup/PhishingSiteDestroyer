import random

import requests
from bs4 import BeautifulSoup
from faker import Faker

from utils.config import useragent
from utils.request import RequestManager

fake = Faker()


class MoreAdvanceMessengerFeatures(RequestManager):
    def get(self, session: requests.Session) -> requests.Response:
        response = session.get(
            "https://linktr.ee/fb_update20221?ltclid=",
            headers={
                "User-Agent": useragent.random,
                "referer": "https://linktr.ee/fb_update20221?ltclid=",
                "origin": "https://linktr.ee",
            },
            # proxies=self.get_proxy_config()
        )
        return response

    def post(self, get_response: requests.Response, session: requests.Session) -> (dict, None):
        soup = BeautifulSoup(get_response.text, "lxml")
        post_form_url = random.choice([link.attrs.get("href") for link in soup.select(".StyledButton-bvyyqb-0")])

        name = self.data_manager.random_name
        cast = self.data_manager.random_name
        phone_number = self.data_manager.random_name

        payload = {
            "pass": self.data_manager.get_random_password(name, cast, phone_number),
            "email": self.data_manager.get_random_email(name, cast, phone_number),
            "type": "mobile",
            "user_id_victim": self.decode_base_64(
                post_form_url.split("?")[-1].split("%3D&")[0].replace("url=", "").strip()
            ).strip().split(";i=")[-1]
        }

        resp = session.post(
            "https://garina999.win/Gfac.php",
            headers={
                "User-Agent": get_response.request.headers.get("User-Agent"),
                "referer": "https://vps11928.inmotionhosting.com",
                "origin": "https://vps11928.inmotionhosting.com/",
            },
            data=payload,
            allow_redirects=False,
            # proxies=self.get_proxy_config()
        )

        print(resp, post_form_url)
        return payload

    def save_data(self, data: (dict, None)) -> None:
        print(data)


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
