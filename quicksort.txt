def partition(arr,l,h):
    i=l-1
    p=h
    for j in range(l,h):
        if(arr[j]<=arr[p]):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return (i+1)
def quicksort(arr,l,h):
    if(l<h):
        pi=partition(arr,l,h)               #placing pivot element in its correct index by calling partition
        quicksort(arr,l,pi-1)               #calling quick sort for elements in range(l,pi-1)
        quicksort(arr,pi+1,h)
    return arr
l=list(map(int,input().split()))
k=quicksort(l,0,len(l)-1)
for i in k:
    print(i,end=" ")
