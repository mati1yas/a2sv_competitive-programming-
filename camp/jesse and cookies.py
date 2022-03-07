#!/bin/python3

import math
import os
import random
import re
import sys
import heapq as h

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    times=0
    h.heapify(A)
    
    while A[0]<k:
        if len(A)<2:
            return -1
        e1=h.heappop(A)
        e2=h.heappop(A)
        
        h.heappush(A,e1+2*e2)
        times+=1
       
    return times
    
  

