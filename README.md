# Enhancing the Dynamic Adaptive Replication Strategy for P2P Systems using the Time-Based Decaying Function

## CMPE 295 Fall 2022 Wang Group 2 (Research)

## Background:
Availability is one of the most important aspects of a peer-to-peer (P2P) system. In order to maintain the high availability of data, replication strategies are used to create multiple copies of the data file. As the number of replicas increases, the availability and performance of the system also increases, but it also increases the cost of maintaining the replicas. Below are the factors that influence data replication:
Which file to replicate?
When to replicate?
Where to place the replicated file?
We have studied many research papers to find a solution to the above critical aspects. One such replication strategy is DARS - Dynamic Adaptive Replication Strategy. It addresses the problem of when to replicate the file based on the opportune moment [1] and finds the optimal placement node using fuzzy clustering analysis [2]. However, the algorithm uses a simplistic approach to decide which file to replicate.

## Problem Statement:
When deciding the set of files that need replica, DARS gets the access amount of files from an array that stores them in descending order. Their assumption is that the files with the highest number of requests are more likely to cause an overloaded (i.e., exceed the node’s available bandwidth) node without considering the timestamps of their requests. However, we found that this is not the optimal solution, as timing information also plays a critical role in determining the future access pattern. P2P data replication algorithms that do not use timestamps information could lead to sub-optimal system performance.  

## Tentative Solution:
In order to overcome the problem, we propose that instead of maintaining the array of files based on the descending access rate, we use a Time-Based Decaying Function (TBDF) [3] to assign weights to the files. The idea of temporal locality is used, according to which a data file that has recently been accessed is more likely to be accessed again in the future. Based on this idea, TBDF gives more weight to recent accesses to a data file than to older ones. TBDF can reduce the weight and relevance of data file accesses as time passes.
