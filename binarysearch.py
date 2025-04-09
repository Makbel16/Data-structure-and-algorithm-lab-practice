datalist=[1,2,3,4,5,6,7,8,9,10]
target=3
low=0
high=len(datalist)-1 
while low<=high:
    mid=(low+high)//2
    if datalist[mid]==target:
        print(list[mid])
    elif datalist[mid]<target:
        low=mid+1
    else:
        high=mid-1
    return -1
        

    
    