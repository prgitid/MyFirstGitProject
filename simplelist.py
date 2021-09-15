n = [ 2,5,8,10.13,141.1,22,39,739]
list2=n[1:10]
print(list2)
list1= n[::2]
print(list1)
#Reversing the list with slicing
list3 = n[::-1]
print(list3)
#Reversing the list with step index of 2
list4 = n[10::-2]
print(list4)
#Reversing the list with reverse
list5=list4.reverse()
print(list5)
#Accessing the elements of reversed list
for k in reversed(n):
    print(k)
for o in dir(n):
    print(o)