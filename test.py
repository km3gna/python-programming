# >> (#!/usr/bin/python)

import sys
import calculator

# print(sys.argv) # take out

if sys.argv[1].isdecimal() and sys.argv[2].isdecimal():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
else:
    print("Both must be integer")
    sys.exit()

print("Sum of arguments:", calculator.add(num1,num2))
print("Average of arguments:", calculator.average(num1,num2))
