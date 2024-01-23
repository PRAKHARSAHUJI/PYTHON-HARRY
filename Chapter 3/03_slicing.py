name = "Prakhar"


# 0 or -7 = P;       
# 1 or -6 = r;       
# 2 or -5 = a;      
# 3 or -4 = k;   
# 4 or -3 = h;     
# 5 or -2 = a;    
# 6 or -1 = r 



 

print(name[0])                 # Output --------->            P               
print(name[1])                 # Output --------->            r
print(name[2])                 # Output --------->            a
print(name[3])                 # Output --------->            k
print(name[4])                 # Output --------->            h
print(name[5])                 # Output --------->            a
print(name[6])                 # Output --------->            r


# SLICING ------------>     print( ...........[ Starting place value  : Ending place value+1 ] )     
# Last number Entered is not included First Number Entered is Included 

print(name[0:1])               # Output --------->            P                    This means 0                 
print(name[0:2])               # Output --------->            Pr                   This means 0 1  
print(name[0:3])               # Output --------->            Pra                  This means 0 1 2 
print(name[0:4])               # Output --------->            Prak                 This means 0 1 2 3 
print(name[0:5])               # Output --------->            Prakh                This means 0 1 2 3 4 
print(name[0:6])               # Output --------->            Prakha               This means 0 1 2 3 4 5 
print(name[0:7])               # Output --------->            Prakhar              This means 0 1 2 3 4 5 6 


print(name[:7])                # Output --------->            Prakhar              This means 0 1 2 3 4 5 6          This Is same as name[0:7]           
print(name[:])                 # Output --------->            Prakhar              This means 0 1 2 3 4 5 6          This Is same as name[0:7] 
print(name[0:])                # Output --------->            Prakhar              This means 0 1 2 3 4 5 6           It takes as the length of the string  
 
print(name[3:7])               # Output --------->            khar                 This means 0 1 2 3 4 5 6 



# SLICING  SKIP ------------> name[0 : 6 : 2 ]  This means starting From 0 till 6 and skippping 2


a = "amazingshopyouhave"               
b = a[0 : 6 : 1]                       # Output --------->            amazin               If 1 is taken that mean 0 words skip
c = a[0 : 6 : 2]                       # Output --------->            aai                  If 2 is taken that mean 1 words skip
d = a[0 : 10 : 3]                      # Output --------->            azgo                 If 3 is taken that mean 2 words skip
e = a[0 : 10 : 2]                      # Output --------->            aaigh                If 2 is taken that mean 1 words skip
f = a[0 : 18 : 1]                      # Output --------->            amazingshopyouhave   If 1 is taken that mean 0 words skip
g = a[0 : 18 : 2]                      # Output --------->            aaighpohv            If 2 is taken that mean 1 words skip
h = a[0 :  : 2]                        # Output --------->            aaighpohv            If 2 is taken that mean 1 words skip

print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

