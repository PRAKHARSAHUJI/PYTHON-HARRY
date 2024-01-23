# STRING FUNCIONS

# 1. len


name = "Prakhar" 

x = len(name)
print(x)
print(len(name))



y = "Prakhar is a Good Boy"

print(len(y))



# 2. string.endswith

y = "Prakhar is a Good Boy"

print(y.endswith("Boy"))                   # If it is True It returns true else return False
print(name.endswith("Khar"))               # case sensitive
print(name.endswith("har"))              



# 3. string.count

y = "Prakhar is a Good Boy"
  
a = y.count("a")                         
print(a)                                 # Output --------->        3
print(y.count("r"))                      # Output --------->        2    


z = "Prakhar is a Good Boy very very very very  Good Boy "

print(z.count("Good"))                      # Output --------->     2    This can count words also letters also 
print(z.count("very"))                      # Output --------->     4       


# 4. string.capitalize

p="prakhar"
print(p.capitalize())                      # Output --------->     Prakhar


# 5. string.find

y = "Prakhar is a Good Boy"

print(y.find("Good"))                      # Output --------->     13 means present at just after 13 place value  number. also 13 tells at 14 Good is starting
print(y.find("good"))                      # Output --------->     -1  means this is not present
print(y.find("Prakhar"))                   # Output --------->     0  means this is present at 1 place value because 0 signifies that is starting just after 0 

# Find  function tell the first occurence means where it is present first time 



# 6. string.replace

y = "Prakhar is a 19 years old"
y=y.replace("19","20")
print(y)
print(y.replace("19","20"))                   # replace function replace in all occurence means where it is present everywhere it replace all

# 7. string.split('r')
a = "working"
print(a.split('r'))

#  string.split()
b = "Prakhar Sahu is a good    boy"
print(b.split())

# 8. string.title()
# capital each word 


# 9. string.swapcase()

# lower to upper upper to lower

# 10. string.join
a="Prakhar" 
b= "sahu"
print(a.join(b))


# 6. string.lstrip
# 6. string.rstrip
# 6. string.strip

