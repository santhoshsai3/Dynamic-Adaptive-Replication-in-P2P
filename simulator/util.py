from datetime import datetime
import numpy as np
import random


def generate_timestamps(start, end, date_format, distribution_size, scale_ratio, max_peaks, min_samples):
    # Converting to timestamp
    start = datetime.strptime(start, date_format).timestamp()
    end = datetime.strptime(end, date_format).timestamp()
    d = distribution_size
    peaks = 0
    while max_peaks != 0 and d > 0:
        print(d, min_samples)
        if d < min_samples:
            sample_size = d
        else:
            sample_size = random.randint(min_samples, d)
        d -= sample_size
        max_peaks -= 1
        peaks += 1

    # X =
    # Generate Normal Distribution
    mu = datetime.strptime('2023-02-27T02:00:00', date_format).timestamp()
    sigma = (end - start) * scale_ratio
    total_distribution = np.random.gumbel(loc=random.uniform(start, end), scale=sigma, size=distribution_size)

    return sorted(total_distribution.tolist())


