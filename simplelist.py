mylist = [2]*5
print(mylist)
mylist2=[4,6,8,10,12]
newlist = mylist + mylist2
print(newlist)
print(len(newlist))
newlist.remove(2)
print(newlist)
print(id(newlist))