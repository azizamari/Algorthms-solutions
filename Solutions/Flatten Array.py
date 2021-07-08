def flatten(arr):
    res=[]
    for i in range(len(arr)):
        e=arr[i]
        if type(e) is list:
            arr.pop(i)
            res+=flatten(e)
        else:
            res.append(e)
    return res
print(flatten([15,26,9,[15,2,[1,2]]]))