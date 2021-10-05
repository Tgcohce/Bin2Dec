#October 5, 2021
# Tolga Gokturk Cohce

# taking the input
num = input("Enter Binary Number to be converted to Decimal: ")

# inverting the input
inverted_num = num[::-1]

# Position of letters set to 0
x = 0
# declaring the output beforehand
oupt = 0


for i in range(0, len(num)):
    decimal = int(inverted_num[x]) * (2 ** x)
    oupt += decimal
    x += 1

print(oupt)