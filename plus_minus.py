#!/bin/python3

"Challenge https://www.hackerrank.com/challenges/plus-minus/problem"

def plusMinus():
    negative = positive = zero = 0
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for nb in arr:
        if nb < 0:
            negative += 1
        elif nb > 0:
            positive += 1
        else:
            zero += 1
    negative_ratio = negative / n
    positive_ratio = positive / n
    zero_ratio = zero / n
    return "{0:.6f}".format(positive_ratio) +'\n' + "{0:.6f}".format(negative_ratio) + '\n' + "{0:.6f}".format(zero_ratio)       



print(plusMinus())

