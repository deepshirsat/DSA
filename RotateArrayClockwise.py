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
