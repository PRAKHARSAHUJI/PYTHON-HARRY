# Tuples() and List[] are same . But in List we can update the value and tuple we cant update the value

t = (1,2,3,4)
print(t)                                    # Output --------->     (1, 2, 3, 4)
print(t[0])                                 # Output --------->     1
print(t[1])                                 # Output --------->     2

# this is not possible -----> t[0]=5   throws an Error

# Creating a Empty Tuple
t = ()
print(t)                                   # Output --------->     ()

# Creating a Single Tuple, we should use comma otherwise it can be used as tuple 
t = (1,)
print(t)                                   # Output --------->     (1,)

# Wrong way to declare single tuple , it will not be used as tuple 
t = (1) 
 