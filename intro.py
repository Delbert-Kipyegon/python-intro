# Try except

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')



# temp = "5 degrees" #user input
temp = 5

cel = 0

try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter the correct temperature')

a = "Python is cool"
print(a[7:])


if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")

for i in range(2, 10, 2):
    print(i, end=" ")

if 12 == 48/4:
    print("Holberton")
else:
    print("School")


if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")


a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")

for i in range(2, 4):
    print(i, end=" ")

for i in range(4):
    print(i, end=" ")


a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")



















