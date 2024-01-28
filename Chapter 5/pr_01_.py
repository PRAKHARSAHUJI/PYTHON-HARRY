myDict = {
    "Achha" : "Good",
    "Kharab" : " Bad",
    "Karo" : "Try",
    "Kab" : "When"
}
print("Which meaning From list you want")
print("Optons Are: ",myDict.keys())
a = input("Enter the word: ")

print("Meaning of the Word is :",myDict.get(a))
