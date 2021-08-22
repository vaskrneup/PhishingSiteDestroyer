import sys
import traceback
from concurrent.futures import ThreadPoolExecutor
import base64

import requests

from utils.config import useragent, data_manager


class RequestManager:
    def __init__(self, total_request_count=32, number_of_threads_to_use=32):
        self.total_request_count = total_request_count
        self.number_of_threads_to_use = number_of_threads_to_use
        self.useragent = useragent
        self.data_manager = data_manager

        self._use_proxy = False
        self._proxy = None

    def use_proxy(self, use, proxy=None):
        self._use_proxy = use

        if use is True:
            self._proxy = proxy

    @staticmethod
    def get_proxy_config():
        return {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }

    @staticmethod
    def decode_base_64(s: str):
        if s.endswith("=") and not s.endswith("=="):
            s = f"{s}="
        elif not s.endswith("=="):
            s = f"{s}=="

        try:
            return base64.urlsafe_b64decode(s).decode("utf-8")
        except Exception as _:  # NOQA
            return ""

    def get(self, session: requests.Session) -> requests.Response:
        raise NotImplementedError

    def post(self, get_response: requests.Response, session: requests.Session) -> (dict, None):
        raise NotImplementedError

    def save_data(self, data: (dict, None)) -> None:
        pass

    def __manager(self, session: requests.Session):
        try:
            self.save_data(self.post(self.get(session), session))
        except Exception as e:
            print(f"ERROR: '{e}'")
            traceback.print_exc()
            sys.exit()

    def run(self):
        with ThreadPoolExecutor(max_workers=self.number_of_threads_to_use) as e:
            for _ in range(self.total_request_count):
                e.submit(lambda: self.__manager(requests.Session()))

    def __call__(self, *args, **kwargs):
        self.run()
