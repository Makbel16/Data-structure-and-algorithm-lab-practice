list = [7, 4, 9, 5, 1, 2, 3]

i=0
for i in range(0,6):
    for j in range(0,6-i):
        if list[j] > list[j + 1]:
            temp=list[j+1]
            list[j+1]=list[j]
            list[j]=temp
print(list)
 