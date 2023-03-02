# Time based decay function algorithm
The value of the function decays continuously as the time passes. TBDF is a function of time and number of requests in the time period

## Requirements:

### Assumptions:
1. The TBDF will assign exponential decay factor to requests only till a limited period of time as only a limited number of requests can be stored. (A period of 10 days will be chosen and evaluated). All the requests before the time will be given the same weight (0).
2. The input timestamp sequence is grouped into set time-period (can be arbitrarily chosen like 5 mins or 10 mins).
3. Decay factor is defined as below: 
<p align="center">
  $\ W = F(1 - r)^T$ <br/>
  where W is the adjusted weight <br/>
  F is the initial frequency of requests in the time-window <br/>
  r is the decay factor <br/>
  T is the difference between lower bound of the current time-window and current time <br/>
</p>


### Algorithm
1. Group the timestamp series based on the fixed time-period.
2. Multiply the decay factor with the frequency of time-period to it's adjusted weight.
3. Sum up all the weights of the series to get cumulative weight.
