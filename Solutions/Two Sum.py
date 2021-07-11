def twoSum(arr,target):
    res=[]
    arr=set(arr)
    for i in arr:
        want=target-i
        if want!=i and want in arr:res.append([i,want])
    return res
print(twoSum([2,4,3,3,9,-3,5,1],6))