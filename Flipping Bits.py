#You will be given a list of 32 bit unsigned integers. Flip all the bits ( 0->1 and 1->0 )
# and return the result as an unsigned integer.

def flippingBits(n):
        return (2**32 - 1)^n



if __name__ == '__main__':
    q = int(input().strip())
    for qr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(result)