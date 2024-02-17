temperature = 32

if temperature > 37 :
    print(" It is hot ")
else:
    print(" It is cold ")

# A program that prints the largest number among three numbers
num1 = 45
num2 = 89
num3 = 32
if num1 > num2 and num1 > num3 :
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3 :
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")

# A program that checks whether a number is even or odd
number = 56
if number % 2 == 0:
    print(number, "is even")
else :
    print(number, "is odd")

# A program that checks whether a number is prime or not

num = 11
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")
