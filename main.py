import sys

from pages.messenger_features import MessengerFeatures, MoreAdvanceMessengerFeatures

print(sys.version, "=====", sys.version_info)

for i in range(1000):
    print("====" * 10)
    print(f"START: {i}")
    MoreAdvanceMessengerFeatures(number_of_threads_to_use=64, total_request_count=10000).run(use_threads=True)
    print(f"END: {i}")
    print("====" * 10)
