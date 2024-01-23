letter = ''' Dear <|NAME|>
You are Selected!
<|DATE|>'''
name = input("Enter your Name: ")
date = input("Enter Today's Date: ")
 
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)