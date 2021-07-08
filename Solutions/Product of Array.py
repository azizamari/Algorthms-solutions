def pofarr(arr):
    if len(arr)==1:return arr[0]
    return arr[0]*pofarr(arr[1:])
print(pofarr([1, 2, 3, 4, 5]))