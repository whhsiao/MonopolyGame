import math
import os
import re
import sys
import itertools
from random import choice
from random import randint
import numpy as np

def probability(N):
    probs = [0,0,1,2,3,4,5,6,5,4,3,2,1]
    probs = [prob/36 for prob in probs]
    Markov_chain = [1]
    while len(Markov_chain)<N:
        tmp = 0.0
        lag = 1
        while lag < 13:
            try:
                tmp += probs[lag]*Markov_chain[-lag]
                lag +=1
            except:
                break
        Markov_chain.append(tmp)
    return Markov_chain[-1]*20

if __name__ == '__main__':
    for itr in range(1,11):
        print("20*the probability landing on the last box after {} rounds is {}".format(itr,probability(40*itr)))

    
