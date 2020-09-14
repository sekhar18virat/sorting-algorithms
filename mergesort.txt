def merge(arr,l,m,h):
    n1=m-l+1              #intializing o. of elemnts in lower array
    n2=h-m                #intializing no. of elements in higher array
    a=[0]*n1              #lower array
    b=[0]*n2              #higher array
    for i in range(n1):
        a[i]=arr[l+i]     #storing all lower elements in an array a
    for j in range(n2):
        b[j]=arr[m+j+1]   #storing all higher elements in an array b
    i=0
    j=0
    k=l
    while(i<n1 and j<n2): #checking for i values and j values
        if(a[i]<=b[j]):   #comparing lower and higher array elements
            arr[k]=a[i]   
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while(i<n1):
        arr[k]=a[i]   #if elements of array a are left over
        i+=1
        k+=1
    while(j<n2):
        arr[k]=b[j]   #if elements of b are leftover
        j+=1
        k+=1
    return(arr)
def mergesort(arr,l,h):
    if(l<h):
        m=(l+(h-1))//2              #calculating mid values and making subarrays
        mergesort(arr,l,m)  
        mergesort(arr,m+1,h)
        merge(arr,l,m,h)            #merge procedure for arr
    return(arr)
l=list(map(int,input().split()))
f=mergesort(l,0,len(l)-1)
for i in f:
    print(i,end=" ")

    