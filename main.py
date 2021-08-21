from pages.messenger_features import MessengerFeatures

for i in range(1000):
    MessengerFeatures(number_of_threads_to_use=128, total_request_count=10000)()
