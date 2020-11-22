import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
  h_no = 0
  highest = scores[0]
  lowest = scores[0]
  l_no = 0
  for i in scores:
    if i > highest:
      h_no = h_no + 1
      highest = i 
    if i < lowest:
      l_no = l_no + 1
      lowest = i
  
  return h_no,l_no
  
      
      
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
