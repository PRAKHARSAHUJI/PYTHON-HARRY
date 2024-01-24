# EMPTY SET IN PYTHON 

a = set()             # set is a collection of non repetative elements therefore elements cant repeate

 
b = {1,2,4,5,3,6}


# SET METHODS

# 01 : string.add
a.add(5)
a.add(6)
a.add(9)
a.add(1)
a.add(2)
a.add(1)

print(a)
# we can add tuple in set as that is hashable , it cant be changed
# we cant add list because it is unhashable , it can be changed
# we cant add dictionary because it is unhashable , it can be changed

a.add((1,2,3))  # tuple



# a.union({2,3,4})
print(a.union({2,3,4}))

print(a.intersection({2,3,4,5,6}))





print(len(a))
print(a)

a.remove(1)
print(a)


print(a.pop()) # print the element that has been removed by the pop command  

print(a)


print(a.clear())
print(a)


