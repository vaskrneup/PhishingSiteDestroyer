import sys
import traceback
from concurrent.futures import ThreadPoolExecutor

import requests

from utils.config import useragent, data_manager


class RequestManager:
    def __init__(self, total_request_count=32, number_of_threads_to_use=32):
        self.total_request_count = total_request_count
        self.number_of_threads_to_use = number_of_threads_to_use
        self.useragent = useragent
        self.data_manager = data_manager

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
