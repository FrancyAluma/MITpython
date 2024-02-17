# Datatype

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool

#A variable with multiple values
languages = ["python","php","java","kotlin"] # List
fruits = ("apple","banana","pineapple") # Tuple
countries = {"Kenya", "Ghana","China"} # Set

#Dictionary
details = {
    "firstname" : "Ashley",
    "course" : "MIT",
    "age" : 18 ,
    "nationality" : "USA"
}

print(number)
print(num)
print(greeting)
print(isPythonInteresting)
print(countries)
print(fruits)
print(languages)
print(details)
print(details["firstname"])
print(details["nationality"])

# Determining the data type of variable
print(type(details))
print(type(countries))
print(type(greeting))
print(type(fruits))

# Typecasting is the process of converting a float to int and an int to a float
print(float(number))
print(int(num))