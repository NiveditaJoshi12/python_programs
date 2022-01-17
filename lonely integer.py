'''Given an array of integers, where all elements but one occur twice, find the unique element.
Example: a=[1,2,3,4,3,2,1]
The unique element is 4.'''

def lonelyinteger(a):
    for i in a:
        x = a.count(i)
        if x <= 1:
            return i


a = list(map(int,input().rstrip().split()))
print(lonelyinteger(a))