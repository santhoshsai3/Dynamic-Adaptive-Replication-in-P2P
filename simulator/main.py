import numpy as np
import math
import time
import queue
import pandas as pd
from util import generate_timestamps
import matplotlib.pyplot as plt


class FileAccessData:
    total_requests = 0
    request_timestamps = None

    def __init__(self):
        self.request_timestamps = queue.Queue(maxsize=1024)

    def add_request(self, timestamp):
        if self.request_timestamps.qsize() >= self.request_timestamps.maxsize:
            print('limit reached')
            return -1
        self.request_timestamps.put(timestamp)
        self.total_requests = self.request_timestamps.qsize()
        return 0


def normalize_array(arr):
    arr = np.array(arr)
    arr_normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    # print((time.time() - 1677624321) / 3600)
    return arr_normalized


def test(arr):
    exp_time_diff = []
    sum = 0
    normalized_input = normalize_array(arr)
    print(normalized_input)
    for i in range(len(arr)):
        weight = math.exp(-arr[i])
        exp_time_diff.append(weight)

    for i in range(len(exp_time_diff)):
        sum += exp_time_diff[i]

    print(arr)
    print(exp_time_diff)
    # print(exp_time_diff_normalized)
    print("importance = {:.10f}".format(sum))

    return sum


def generate_access_pattern():
    start = '2023-02-27T00:00:00'
    end = '2023-02-28T00:00:00'
    date_format = '%Y-%m-%dT%H:%M:%S'

    t = generate_timestamps(start=start, end=end, date_format=date_format, distribution_size=10000
                            , max_peaks=10, min_sample_size=1000, max_sample_size=2500)

    f = [1 for x in range(len(t))]
    data = {"timestamps": t, "freq": f}

    # Create DataFrame
    df = pd.DataFrame(data)
    df["timestamps"] = pd.to_datetime(df["timestamps"], unit='s')
    df = df.resample('6H', on='timestamps').sum()

    print(df)
    df.plot()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_access_pattern()
