def insertionsort(arr):
    for i in range(len(arr)):
        j=i                                     #initializing j 
        while(j>0 and arr[j-1]>arr[j]):         #checking element at j-1 th index and jth index
            arr[j],arr[j-1]=arr[j-1],arr[j]     #swapping arr[j] and arr[j-1]
            j-=1
            
    return arr
l=list(map(int,input().split()))                #taking array input          
f=insertionsort(l)
for i in f:
    print(i,end=" ")                            #printing array