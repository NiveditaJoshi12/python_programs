def plusminus(arr):
    # Write your code here
    pos, nig, zero = 0, 0, 0

    for a in range(0,n):
        if arr[a] < 0:
            nig +=1
        elif arr[a]>0:
            pos +=1
        elif arr[a]==0:
            zero += 1
    nig1 = nig/n
    pos1 = pos/n
    zero1 = zero/n
    print("{0:.6f}\n {1:.6f}\n {2:.6f}\n".format(nig1, pos1, zero1))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusminus(arr)