# it is how to handle errors we encounter- Exceptions = Errors

try:
    print(x)
except:
    print(" Cesco ")
finally:
    print("Success")

num = 20
num2 = 0

try:
    print(num / num2)
except:
    print("Impossible de diviser par Zero")




# User-defined functions
try:
    def multiply(number1,number2):
         print(number1 * number2)

except:
     print("An error occurred")

finally:
    print("Success")


multiply (6,5)


