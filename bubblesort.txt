def bubblesort(arr):
    for i in range(len(arr)):
        swaps=0                                    #define no.of swaps
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):                  #comparing aray elements and checking with consecutive elements
                arr[j],arr[j+1]=arr[j+1],arr[j]   #swapping elements
                swaps+=1                          #increment swaps
        if(swaps==0):
            return arr
l=list(map(int,input().split()))                  #taking input
f=bubblesort(l)                                       
for i in f:
    print(i,end=" ")                              #printing list of sorted elements     