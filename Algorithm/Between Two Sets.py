#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy

# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    
    lcm = a[0]
    
    for i in a[1:]:
        lcm = lcm*i//math.gcd(lcm, i)
    
    def find_gcd(l):
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        n =1
        f = l[0]
        while n != len(l):
            f = gcd(f,l[n])
            if  f == 1:
                return 1
            else:
                n = n + 1          
        return f 
    
    gcd = find_gcd(b)
    i = 1
    counter = 0
    while lcm*i <= gcd:
        f = gcd / (lcm*i)
        if f.is_integer():
            counter = counter + 1
        i = i + 1
    return counter
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
