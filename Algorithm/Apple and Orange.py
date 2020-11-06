
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
  apples_drop = list(map(lambda x:x + a,apples))
  oranges_drop = list(map(lambda x:x + b,oranges))
  no_apples = 0
  no_oranges = 0
  #print(apples_drop)
  #print(oranges_drop)
  for i in range(max(len(apples_drop),len(oranges_drop))):
    #print(x,y)
    #print(apples_drop[i],oranges_drop[i])
    if (len(apples_drop) > i) and (apples_drop[i] in range(s,t+1)):
      #print(apples_drop[i])
      no_apples = no_apples + 1
    if (len(oranges_drop) > i) and (oranges_drop[i] in range(s,t+1)):
      #print(oranges_drop[i])
      no_oranges = no_oranges + 1
  print(no_apples)
  print(no_oranges)
      

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)