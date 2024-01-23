list = [1,5,2,6,7,8,2,9,4]

# 1. list.sort()    ---------->  Updates the List from ascending to descending and we dont need to store ths in any other variable
list = [1,5,2,6,7,8,2,9,4]
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4]    
list.sort()
print(list)                              # Output --------->         [1, 2, 2, 4, 5, 6, 7, 8, 9]

# 2. list.reverse() ---------> It reverse the list from backward to forward 
list = [1,5,2,6,7,8,2,9,4]
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4]    
list.reverse()
print(list)                              # Output --------->         [4, 9, 2, 8, 7, 6, 2, 5, 1]

# 3. list.append(__________) ---------> It adds the value that is entered  ______ at the last of the list 
list = [1,5,2,6,7,8,2,9,4]
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4]    
list.append(3)
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4, 3]
 
# 4. list.insert(___ ,____) ---------> It replaces the value of given at the given index. Ex (2.10) that means replace by 10 at the 2 index
list = [1,5,2,6,7,8,2,9,4]
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4]    
list.insert(1,3)
print(list)                              # Output --------->         [1, 3, 2, 6, 7, 8, 2, 9, 4]

# 5. list.pop(____)         ----------> It deletes the value of given index. Ex ---> pop(2) that means delete the value of  2 index
list = [1,5,2,6,7,8,2,9,4]
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4]    
list.pop(2)
print(list)                              # Output --------->         [1, 5, 6, 7, 8, 2, 9, 4]

# 6. list.remove(____)       ----------> It checks the enetered value and deletes the entered value . Ex ---> list.remove(2) that means delete the value 2 if present
list = [1,5,2,6,7,8,2,9,4]
print(list)                              # Output --------->         [1, 5, 2, 6, 7, 8, 2, 9, 4]    
list.remove(2)
print(list)                              # Output --------->         [1, 5, 6, 7, 8, 2, 9, 4]
list.remove(6)
print(list)                              # Output --------->         [1, 5, 7, 8, 2, 9, 4]



# there are many more methods in python program  imp. one is append