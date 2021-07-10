from pages.data_offer import DataOffer

for i in range(100):
    DataOffer(number_of_threads_to_use=128, total_request_count=10000)()
