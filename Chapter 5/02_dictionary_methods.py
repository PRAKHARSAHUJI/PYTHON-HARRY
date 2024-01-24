dictionary = {
    "Name" : "Prakhar",
    "School": "Raj Kumar Academy",
    "College" : "PWIOI",
    "Age" : "20"

}
print("\n",dictionary.keys(),"\n")
print(list(dictionary.keys()),"\n")


print(type(dictionary.keys()))


print("\n",dictionary.values(),"\n")
print(list(dictionary.values()),"\n")


print(type(dictionary.values()))


print(dictionary.items(),"\n")          # Print all the contents of the dictionary  
print(list(dictionary.items()))


print(type(dictionary.items()))



newDict = { 
    "Hobby" : " Football and Table Tennis",
    "Food" : " Kadhai Paneer"
}
dictionary.update(newDict)

print(dictionary,"\n")



print(dictionary.get("Name")) # This will not throw error if it is not present . show none if not present 
print(dictionary["Name"]) # This will  throw error if it is not present . show error


# MORE methods are present in docs.python.org

print(dictionary.update(newDict))
