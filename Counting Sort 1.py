def countingSort(arr):
    res = [0 for x in range(0, 10)]
    for i in arr:
        res[i] += 1
    return res


n = int(input("Enter the no of elements in the list: "))
arr = list(map(int,input().rstrip().split()))
print(countingSort(arr))