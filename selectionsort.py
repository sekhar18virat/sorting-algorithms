def selectionsort(arr):
    for i in range(len(arr)):                
        min=i                                #assuming that element at index i is minimum 
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):             #comparing jth element with minimum element 
                min=j                        #changing the min value to jth index
        arr[min],arr[i]=arr[i],arr[min]      #swapping element at min index and element at ith index
    return arr
l=list(map(int,input().split()))             #taking array input
f=selectionsort(l)
for i in f:
    print(i,end=" ")                         #printing array