def findMinMax(arr):
    arr.sort()
    return arr[0], arr[-1]

arr = [10, 4, 8, 2, 9, 5]

print(findMinMax(arr))