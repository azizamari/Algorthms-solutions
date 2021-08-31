l=input().split(" ")
l=[int(n) for n in l]

# sort
n=len(l)
def merge(elements,left,middle,right):
    n1= middle-left+1
    n2= right-middle

    l=[0]*(n1)
    r=[0]*(n2)
    for i in range(0,n1):
        l[i]=elements[left+i]
    for j in range(0,n2):
        r[j]=elements[middle+j+1]
    i=0
    j=0
    k=left
    while i < n1 and j<n2:
        if l[i]<=r[j]:
            elements[k]=l[i]
            i+=1
        else:
            elements[k]=r[j]
            j+=1
        k+=1

    while i<n1:
        elements[k]=l[i]
        i+=1
        k+=1

    while j<n2:
        elements[k]=r[j]
        j+=1
        k+=1

def mergeSort(elements,l,r):
    if l<r:
        m=(l+r-1)//2
        mergeSort(elements,l,m)
        mergeSort(elements,m+1,r)
        merge(elements,l,m,r)
    return elements 

 
print(mergeSort(l,0,n-1))