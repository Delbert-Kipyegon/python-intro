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