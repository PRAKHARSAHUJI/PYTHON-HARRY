a= "Prakhar"
b= "Good Morning"


print(b+a)       # Output ---------> Good MorningPrakhar

print(b + a)    # Output ---------> Good MorningPrakhar

print(b,a)      # Output ----------> Good Morning Prakhar

c= b + a        # Concatenating

d= b,a
print(c)        # Output ---------> Good MorningPrakhar
print(d)        # Output ---------> ('Good Morning', 'Prakhar')

a= "Prakhar"
b= "Good Morning, "

print(b+a)       # Output ---------> Good Morning, Prakhar

print(b + a)    # Output ---------> Good Morning, Prakhar

print(b,a)      # Output ----------> Good Morning,  Prakhar


x= "Prakhar"
y = "Sahu"

z=x,y

print(z)         # Output ---------->('Prakhar', 'Sahu')


b="Prakhar Sahu "
a= "prakhar"*5
print(a)
print(b*5)