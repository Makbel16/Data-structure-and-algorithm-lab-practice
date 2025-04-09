# array = [5, 4, 1, 2, 3]#4,1,5,
# for i in range(1, len(array)):
#     key = array[i]
#     j = i - 1
#     while j >= 0 and array[j] > key:
#         array[j + 1] = array[j]
#         j -= 1
#     array[j + 1] = key
# print("Sorted array:", array)
array=[3,6,8,9,4,1,2,10]
for i in range (1,len(array)):
    key=array[i]
    j=i-1
    while j>=0 and array[j]>=key:
        array[j+1]=array[j]
        j-=1
    array[j+1] = key
print('the sorted list will become',array)