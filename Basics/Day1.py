import keyword

# Hello Word
print("Hello World")

# Data Types
integer = 1
character = "D"
string = "Devansh"
boolean = True
float = 5.5

# Handling Output
print(integer)
print(character)
print(string)
print(boolean)
print(float)
print(f"Hello my name is {string}, My name starts with {character}, my age is {integer}, my height is {float} & am I studing ? {boolean}")

# Handling Input
name = input("Your Name ? ")
age = input("Your Age ?")
isStudying = input("Are You Studying Yes Or No ? ")
print(f"Helloww, My name is {name}, My Age is {age}, Am I Studying ? {isStudying}")

# Handling Indentetion
if 5>2:
    print("True")

# Printing Keyword
list = keyword.kwlist
print(list)

# Handling Identifier
class Employee_Info:
    def ask_the_department():
        dept = input("What's your department ? ")
        print(f"The Employee's department is : {dept}")

employeerInfo = Employee_Info
employeerInfo.ask_the_department()        
