import fake_useragent

from utils.data import DataManager

useragent = fake_useragent.UserAgent(
    fallback=""
)
data_manager = DataManager()
