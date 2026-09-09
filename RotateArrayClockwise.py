def rotateArrayClockwise(arr):
    n = len(arr)
    lastElement = arr[n-1]
    for i in range(n-1, 0 , -1):
        #Start, Stop, Step (Increment or Decrement)
        arr[i] = arr[i-1]
    arr[0] = lastElement
    return arr

arr = [1, 2, 3, 4, 5]
print(rotateArrayClockwise(arr))
#Rotate array right by k steps using shifting or reversal (O(1) space)
def rotateArrayKtimes(arr , k):
    n = len(arr)
    k = k % n
    for i in range(k):
        rotateArrayClockwise(arr)
    return arr

arr = [1, 2, 3, 4, 5]
k = 6
print(rotateArrayKtimes(arr, k))
