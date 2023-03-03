from datetime import datetime
import numpy as np
import random
import time


def generate_timestamps(start, end, date_format, distribution_size, max_peaks, min_sample_size, max_sample_size):
    # Converting to timestamp
    start = datetime.strptime(start, date_format).timestamp()
    end = datetime.strptime(end, date_format).timestamp()
    d = distribution_size
    peaks = 0
    samples = []
    while max_peaks != 0 and d > 0:
        if d < min_sample_size or max_peaks == 1:
            sample_size = d
        else:
            sample_size = random.randint(min_sample_size, max_sample_size)
        d -= sample_size
        max_peaks -= 1
        peaks += 1

        sigma = random.uniform(min_sample_size, max_sample_size)
        loc = random.uniform(start, end)
        print('loc = ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(loc)), ' sample size = ', sample_size)
        sample = np.random.gumbel(loc=loc, scale=sigma, size=sample_size)
        # print(sample.tolist())
        samples = samples + sample.tolist()

    return sorted(samples)
