import math
import os
import re
import sys
import itertools
from random import choice
from random import randint
import numpy as np

def probability(N):
    result = 0
    dice = range(1,7)
    for i in range(N):
        loop_time = 0
        #the state variable characterizes the current position 
        state = 0        
        while loop_time < 10:
            point = choice(dice)+choice(dice)
            if (state + point) % 40 < state:
                loop_time +=1
            state = (state + point) % 40
        #print(state)
        while state<40:
            point = choice(dice)+choice(dice)
            if (state+point) == 39:
                result +=1
                break
            state += point
        #print((loop_time,state))
    return N, result, 20*result/N
if __name__ == '__main__':
    print(probability(100000))
    print(probability(1000000))
    print(probability(500000))
    
