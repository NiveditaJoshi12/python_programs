# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
import  functools
def diagonalDifference(arr):
    sum1 = 0
    sum2 =0
    # i=0
    # j =0
    # while i<= n-1 and j <= n-1:
    #      sum = sum + arr[i][j]
    #      i += 1
    #      j +=1
    # i =n-1
    # j = 0
    # while i >= 0 and j<=n-1:
    #     sum1 = sum1 + arr[i][j]
    #     i -= 1
    #     j +=1
    sum1 = sum([arr[x][x] for x in range(n)])
    sum2 = sum([arr[x][n - 1 - x] for x in range(n)])
    diff = abs(sum1-sum2)
    return diff


n = int(input("Enter the no. of rows: "))
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(diagonalDifference(arr))
print(arr)