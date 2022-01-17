# Given five positive integers, find the minimum and maximum values
# that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single
# line of two space-separated long integers.
import math
from _functools import reduce

# def miniMaxSum(arr):
#     # Write your code here
#     a1 = sorted(arr)
#     print(sum(a1[:-1]), sum(a1[1:]))


def minmax_sum(arr):
    a1 = sorted(arr)
    a1.pop()
    print(a1)
    max_sum = sum(a1)
    a2 = sorted(arr, reverse= True)
    a2.pop()
    print(a2)
    min_sum = sum(a2)
    return f"Sum of max numbers is {max_sum} and sum of min numbers is {min_sum}"

if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    print(arr)
    print(minmax_sum(arr))