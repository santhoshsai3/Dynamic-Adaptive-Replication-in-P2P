# Access pattern algorithm

The idea is to create an access pattern for a file which can be used for evaluation. The access pattern must be randomly generated and must resemble real-world data. Gumbel distribution is used to generate a unimodal and assymetric distribution of timestamps.

## Requirements:

### Inputs
1. Start time
2. End time
3. Distribution size
4. Max number of peaks
5. Minimum and maximum size of each sample set


## Algorithm for generating timestamp series
1. Based on max number of peaks(max_peaks) and total distribution size(dist_size), randomly distribute data such that actual number of peaks (n) is less than max_peaks and size of each distribution (sample_size) is in between minimum and maximum value supplied. This step will give 'n' samples with each distributions.
2. In each distribution, randomly choose a value for mean (center/peak of distribution). 
3. Choose a random value between min and max sample size as the standard deviation.
4. Supply the start date and end date values to the gumble distribution generator to output the random samples that follow the gumble curve.
5. Perform steps 2 to 4 for all 'n' samples.
6. Concatenate all the distributions.
