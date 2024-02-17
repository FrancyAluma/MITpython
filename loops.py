# 1.While loop
# Incrementing a value
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrementing values
num = 105
while num >= 100:
    print(num)
    num -= 2

# Break statement
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1

# continue
count = 19
while count < 25:
    count += 1
    if count == 23:
        continue
    print(count)

# 2. For loop
languages = ["Python", "C++", "Kotlin"]
for lang in languages:
    print(lang)

# Range
for z in range(6):
    print(z)

for y in range(20,31):
    print(y)

for i in range(30, 41, 2):
    print(i)

# Assignment 2
assignment = "Innovation"
for assignment in "Innovation":
    print(assignment)


