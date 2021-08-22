from pages.messenger_features import MessengerFeatures, MoreAdvanceMessengerFeatures

for i in range(1000):
    MoreAdvanceMessengerFeatures(number_of_threads_to_use=1, total_request_count=10000)()
