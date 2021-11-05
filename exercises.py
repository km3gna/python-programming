# # python3 first.py

# # CH02 - BASIC PYTHON SYNTAX

# # Exercise 1:

# text = input("Write a string of text: \n")
# print(text)
# print(len(text))


# # Exercise 2:

# first_name = input("Hello! \nWhat is your first name? ")
# last_name = input("What is your last name? ")

# full_name = first_name.capitalize() + " " + last_name.capitalize()
# print("Hi {}! Nice to meet you!".format(full_name))

# initials = first_name[0].upper() + last_name[0].upper()
# print(initials)


# # Exercise 3:

# text = input("Write a string of text: \n")
# print(text.endswith("."))
# print(text.isalpha())
# print(text.find("x"))

# new_text = "Let's change all the lower-case e's to uppercase e's."
# print(new_text)
# print(new_text.replace('e', 'E'))


# # Exercise 4:

# text = input("Write a string of text: \n")
# print(text[0] + " shows up " + str(text.count(text[0])) + " time(s) in the string.")
# print(text[-1] + " shows up " + str(text.count(text[-1])) + " time(s) in the string.")


# # Exercise 5:

# def areaOfCircle():
#     PI = 3.14159
#     r = float(input("Enter the radius: "))
#     area = PI * r * r
#     print("Are of the circle = %.5f" %area)

# areaOfCircle()


# # Exercise 6:

# int1 = int(input("Enter an integer: "))
# int2 = int(input("Enter another integer: "))
# print(int1 * int2)

# print("The current data type is an integer but it needs to be a double/float to process decimals. Same goes for non-numeric data (cannot calculate string datatype).")


# # Exercise 7:

# string = input("Enter a string: ")
# number = input("Enter a number: ")
# print(string * 3)
# print(number * 3)
# print(string * int(number))


# # Exercise 8:

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# result = num1 ** num2
# print(result)

#------------------------------------------------------------------------------------------------------

# # CH03 - LANGUAGE COMPONENTS

# # Exercise 1 & 2:

# lucky_number = input("Enter in a lucky number: ")

# if lucky_number.isdigit():
#     print("Your lucky number is {}!".format(lucky_number))
#     print("There are {} digits in your lucky number!".format(len(str(lucky_number))))
# else:
#     print("That is not a valid entry.")


# # Exercise 3:

# num1 = input("Enter an integer: ")
# num2 = input("Enter another integer: ")

# if num1 == num2:
#     print("{} and {} are equal.".format(num1,num2))
# else:
#     print("{} is the larger of the two numbers.".format(max(num1, num2)))


# # Exercise 4:

# int1 = int(input("Enter an integer: "))
# int2 = int(input("Enter another integer: "))

# sum = 0
# for i in range(int1, int2+1):
#     sum = sum + i

# print("The sum of the integers from {} to {} is {}".format(int1, int2, sum))


# # Exercise 5: 

# input = input("Enter multiple numbers: ")

# nums = []

# nums = nums.append(input.split())

# for n in nums:
#     if n > 0:
#         print (n)
#     else:
#         continue


# # Exercise 6:

# lower = int(input("Enter a number to represent the lower limit: "))
# higher = int(input("Enter a number to represent the higher limit: "))
# step = int(input("Enter a number to represent the step value: "))

# for i in range(lower, higher+1, step):
#     print(i)


# # Exercise 7: ?????

# fmt = "{:3}"
# for i in range(50):
#     if i == 9:
#         print(fmt.format(i), end="\n\n")
#     elif i % 10 == 9:
#         print(fmt.format(i), "\n")
#     else:
#         print(fmt.format(i), end=" ")


# Exercise 8:

# int1 = int(input("Enter an integer: "))
# int2 = int(input("Enter another integer: "))

# if int1 > int2:
#     int1, int2 = int2, int1

# sum = 0
# for i in range(int1, int2+1):
#     sum += i

# print("The sum of the integers from {} to {} is {}".format(int1, int2, sum))

#------------------------------------------------------------------------------------------------------

# # CH04 - COLLECTIONS

# # Exercise 1: ?????

# days = []

# for index, value in enumerate(first):
#     days.append(f'{day}{second[index]}')

# #OR

# list1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# list2 = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

# for i in range(len(list1)):
#     days = list1[i] + list2[i]
#     print(days, end=" ")
    

# # Exercise 2:

# num_list = []

# prompt = "Enter a number (or the word 'end' to quit): "

# while True:
#     data = input(prompt)
#     if data == "end":
#         break
#     num_list.append(int(data))

# print("Here is your list of numbers:", num_list)

# sum = 0
# for i in num_list:
#     sum += i
# print("The sum of all the numbers in the list is:", sum)


# # Exercise 3: ?????
# # ?? How to continue loop if invalid string entry (except "end" and int) ??

# set_numbers = set()

# counter = 0

# prompt = "Enter a number: "

# while True:
#     numbers = input(prompt)
    
#     if numbers == "end":
#         break
#     elif int(numbers) in set_numbers:
#         print("Number already exists in this set.")
#         counter += 1
    
#     set_numbers.add(int(numbers))

# print("Here is your set of numbers:", set_numbers)
# print("Number of times an input was not add to the set:", counter)


# # Exercise 4:

# unique_set = set()
# counter = 0

# prompt = "Enter a word (or type 'done' to quit): "

# while True:
#     word = input(prompt)
#     if word == "done":
#         break
#     unique_set.add(word)
#     counter += 1

# unique_set = list(unique_set)
# unique_set.sort()

# print("Here is your unique set of words:", unique_set)
# print("This set has {} unique words.".format(counter))


# # Exercise 5:

# digits = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

# prompt = input("Enter a number: ")

# for n in prompt:
#     print(digits[int(n)], end = " ")

# print()


# # Exercise 6: ?????
# # Rewrite Exercise 4 but this time count the frequency of each word in user's input.
# # A dict provides the perfect data structure for this program. Let the words be the keys and counts be the values.
# # Print the results sorted by the words. Then, print the results sorted by the counts.

# word_dict = {}

# prompt = "Enter a some text (or just the word 'end' to quit) "
# while True:
#     data = input(prompt)
#     if data == "end":
#         break

#     word_list = data.split()
#     for word in word_list:
#         word_dict[word] = word_dict.get(word, 0) + 1          # add 1 to value
#                                                               # dictionary.get(keyname, value)    # get() method returns the value of the item

# key_list = list(word_dict.keys())

# print()
# print("Words and Word Count sorted by Words (the key)")
# key_list.sort()
# for word in key_list:
#     print(word, word_dict[word])

# print("Words and Word Count sorted by Word Count (the value)")

# key_list.sort(key=word_dict.get)
# for word in key_list:
#     print(word, word_dict[word])

#------------------------------------------------------------------------------------------------------

# # CH05 - FUNCTIONS

# # Exercise 1:
# # Write and test a function that validates input.
# # Prompt for positive integer. Validate. If input is valid, return the number. 
# # If input is invalid, return a zero (0) instead.
# # The application, not function, should indicate with a message in the output 
# # each time an invalid entry is given.

# def validate():
#     prompt = input("Enter a positive integer: ")
#     if prompt.isnumeric():
#         return int(prompt)
#     else:
#         return 0              # boolean for False


# # Use of if not ?????
# result = validate()
# if not result:
#     print("Invalid entry.")


# # ** Exercise 2:
# # Write and test a function that takes a collection of strings and returns the length of the longest string in the collection.
# # The application should loop through the collection of strings and rely on the value returned by the function to format all of the strings
# # to the output such that they are all right justified to the width of the longest string.

# def max_length(data):
#     return len(max(data, key=len))

# words = ["hello", "variables", "g", "dog", "thelongestword"]
# longest = max_length(words)

# for word in words:
#     # print(f"{word:>{longest}s}")    # denotes string type


# # Exercise 3: ?????
# # Write a similar function to the built-in function 'sum', but instead of taking a collection as a parameter, the function should take
# # a variable number of arguments and return the sum of them.

# def get_sum(*args):
#     return sum(args)

# print(f"sum of 5, 6, 7 is {get_sum(5, 6, 7)}")


# # Exercise 4:
# # Rewrite the function in Exercise 3 to return a tuple instead of a sum.
# # The tuple should be the sum and the average of all the arguments passed to the function.

# def get_sum_avg(*args):
#     total = sum(args)
#     return(total, total/len(args))

# total, avg = get_sum_avg(5, 6, 7)
# print(f"sum of 5, 6, 7 is {total}, average is {avg}")


# # Exercise 5:
# # Write a calculator app that presents the following menu:
# # Calculator options:
# #     1. Add
# #     2. Subtract
# #     3. Multiply
# #     4. Divide
# #     5. Quit
# # User is expected to enter a number from the above menu. After choosing the operation, user
# # should be prompted twice for two numbers and the chosen operation performed on them with the
# # result displayed on the screen.

# def get_values():
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#     return (x, y)

# def add():
#     x, y = get_values()
#     print(f"{x}+{y}={x+y}\n")

# def subtract():
#     x, y = get_values()
#     print(f"{x}-{y}={x-y}\n")

# def multiply():
#     x, y = get_values()
#     print(f"{x}*{y}={x*y}\n")

# def divide():
#     x, y = get_values()
#     print(f"{x}/{y}={x/y:.2f}\n")

# def quit():
#     print("Exiting...")
#     exit()

# def not_an_option():
#     print("This calculator can't do that...\n")

# calc = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": quit}
# while True:
#     print("Calculator Options:")
#     for key in calc:
#         print(f"{key}. {calc[key].__name__.capitalize()}")
#     choice = input("Choose an action: ")

#     calc.get(choice, not_an_option)()


# # **Exercise 6:
# # Write and test a function that receives a list as its only parameter
# # and returns a new list of the positive elements only.



# # **Exercise 7:
# # Write and test a function that takes a variable number of arguments as its first parameter
# # and a number as its second parameter. Function should return the count of the values in
# # the tuple parameter (the variable number of arguments) that are greater than the
# # second parameter (num in the sample below). Call to a function named positive:
# # res = positive(5, -10, 10, -20, 30, num=0) --> in this case function returns a value of 3



# # Exercise 8:
# # Write a function that returns a nested function.
# # When nested function is executed it should return the sum of two integers.
# # The two parameters should be passed to the outer function and used by the inner function.



# # Exercise 9:
# # Re-write your solution to Exercise 8 such that the outer function receives no parameters,
# # and the nested function is defined as taking teh two parameters.



# # Exercise 10:
# # Re-write solution to either Exercise 8 or 9 so that it uses a lambda expression as the nested function.

#------------------------------------------------------------------------------------------------------

# # CH06 - MODULES

# # Exercise 1:

# import calculator

# calculator.add(2,3)


# # Exercise 2:

# import calculator
# import sum

# calculator.add(2,3)
# sum.add(2,3)


# # Exercise 3:

# from sys import argv

# argv.pop(0)
# argv.sort()
# for arg in argv:
#     print(arg)


# # Exercise 4:

# # print("Number of arguments:", len(sys.argv), "arguments")
# # print("Arugment List:", str(sys.argv))

# # list = [int(arg) for arg in sys.argv[1:]]
# # print("Sum: {} and Average: {}".format(sum(list), int(sum(list)/len(list))))
# # a = int(sys.argv[1])
# # b = int(sys.argv[2])

# # total = sum(a,b)
# # avg = sum(a,b) / len(sys.argv[1:2])

# # print("Sum = ", total, " and average = ", avg)

# # ANSWER

# # from sys import argv

# # total = 0
# # for item in argv[1:]:
# #     total += float(item)

# # print("Total:", total)
# # print("Average:", total / (len(argv) - 1))

# # ***** ANSWER *****
# #!/usr/bin/python

# import sys
# import calculator

# # print(sys.argv) # take out

# if sys.argv[1].isdecimal() and sys.argv[2].isdecimal():
#     num1 = int(sys.argv[1])
#     num2 = int(sys.argv[2])
# else:
#     print("Both must be integer")
#     sys.exit()

# print("Sum of arguments:", calculator.add(num1,num2))
# print("Average of arguments:", calculator.average(num1,num2))

#------------------------------------------------------------------------------------------------------

# # CH07 - CLASSES IN PYTHON

# # Exercise 1 & 2 & 3:

# # Need to modify to have getters and setters or with property procedures.

# class Person:

#     default = "Unknown"

#     def __init__(self, name=default, age=default, gender=default):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def __str__(self):
#         return "{} {} {}".format(self.name, self.age, self.gender)

# class Family:

#     def __init__(self, parent1, parent2, *children):
#         self.parent1 = parent1
#         self.parent2 = parent2
#         self.kids = list(children)
    
#     def add(self, child):
#         self.kids.append(child)

#     def __str__(self):
#         family = "\n\t" + str(self.parent1) + "\n\t" + str(self.parent2)
#         for kid in self.kids:
#             family += "\n\t" + str(kid)
#         return family

#     def __gt__(self, other):
#         return len(self.kids) > len(other.kids)

#     def __eq__(self, other):
#         return len(self.kids) == len(other.kids)

#     def __lt__(self, other):
#         return len(self.kids) < len(other.kids)


# def main():
#     # p1 = Person("Jane", 35, "F")
#     # p2 = Person("John", 25, "M")

#     # print(p1)
#     # print(p2)

#     mom = Person("Marge", 40, "F")
#     dad = Person("Homer", 45, "M")
#     kid1 = Person("Bart", 22, "M")
#     kid2 = Person("Lisa", 21, "F")

#     fam1 = Family(mom, dad, kid1, kid2)

#     print("The Simpsons...")
#     print(fam1)
#     print()

#     kid3 = Person("Maggie", 10, "F")
#     fam1.add(kid3)
#     print("The Simpsons...")
#     print(fam1)

#     fam2 = Family(mom, dad, kid1)

#     if fam1 > fam2:
#         print("fam1 has more kids than fam2")
    
#     fam2.add(kid3)
#     fam2.add(Person("Josh", 25, "M"))

#     if fam1 == fam2:
#         print("fam1 and fam2 have the same number of kids")

#     fam2.add(Person("Jane", 56, "F"))

#     if fam1 < fam2:
#         print("fam1 has fewer kids than fam2")
    

# if __name__ == "__main__":
#     main()


# # Exercise 4:

# class Worker:

#     def __init__(self, name, salary, years):
#         self.name = name
#         self.salary = salary
#         self.years = years
    
#     def pension(self):
#         return self.years * .10 * self.salary
    
#     def get_name(self):
#         return self.name


# class Manager(Worker):
    
#     def __init__(self, name, salary, years):
#         super().__init__(name, salary, years)

#     def pension(self):
#         return self.years * .20 * self.salary

#     def get_name(self):
#         return self.name
    

# class Executive(Manager):

#     def __init__(self, name, salary, years):
#         super().__init__(name, salary, years)
    
#     def pension(self):
#         return self.years * .30 * self.salary

#     def get_name(self):
#         return self.name
    
# def main():
    
#     workers = [Executive("Elon", 1000000, 15),
#                 Manager("Jen", 500000, 10),
#                 Worker("Sam", 125000, 8)]

#     fmt = "{:3} {:15.2f} {}"
#     for idx, worker in enumerate(workers):
#         print(fmt.format(idx, worker.pension(), worker.get_name()))


# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------------------------------

# # CH08 - EXCEPTIONS

# # Exercise 1 & 2:

# def valid_num():
#     data = input("Enter a number or 'end' to end program: ")
#     if data == "end":
#         return None
#     number = int(data)
#     if number < 0:
#         raise IndexError("Negative indexes not allowed.")   

#     return int(data)
        

# def main():
#     list = [15, 11, 28, 33, 45, 58, 61, 72, 84, 99]
#     while True:
#         try:
#             data = valid_num()            
#         except ValueError:                # handle case of illegal subscript
#             print("Not an integer.")
#             continue
#         except IndexError as ie:          # handle case of negative number
#             print(ie)
#             continue
#         if data is None:
#             break                         # end of program

#         try:
#             print(list[data])
#         except IndexError:                # handle case of illegal number
#             print("Index out of range.")


# if __name__ == "__main__":
#     main()



#------------------------------------------------------------------------------------------------------

# # CH09 - INPUT AND OUTPUT

# # Exercise 1:

# def main():
#     char_count = word_count = line_count = 0
#     try:
#         with open(input("Enter a file name: "), "r") as a_file:
#             while True:
#                 txt = a_file.readline()
#                 if not txt:
#                     break
#                 char_count += len(txt)
#                 word_count += len(txt.split())
#                 line_count += 1
#     except OSError as err:
#         print("IO Error:", err)
    

#     print("Characters:", char_count, "Words:", word_count,"Lines:", line_count)

# if __name__ == "__main__":
#     main()

# # Solution:

# from sys import argv
# fmt = "{:20} {:^5} {:^5} {:^5}"
# print(fmt.format("FILE NAME", "LINES", "WORDS", "CHARS"))

# for filename in argv[1:]:
#     f = open(filename, "r")
#     lines = words = chars = 0
#     for line in f:
#         lines += 1
#         chars += len(line)
#         data = line.split(None)   # What is this for??
#         words += len(data)
#     f.close()
#     print(fmt.format(filename, lines, words, chars))


# # Exercise 2:
# # program that counts the number of lines, words and characters for each named file on command line
# # accepts as an optional first command line argument a -t option (command line argument)
# # program should then only print the total number of lines, words, and chars in all files combined




# # Exercise 3:
# program asks user for names of an i&o file
# open both files; program reads from input file (readline()) and write to the output file (write())

# def main():

#     try:
#         # write to file
#         with open(input("Enter file name: ", "r") as a_file:
#             while True:

    
#         # read from file
#         with open("Enter file name: ", "w") as b_file:
    
#     except OSError as err:
#         print("OS Error": err)

# if __name__ == "__main__":
#     main()


#------------------------------------------------------------------------------------------------------

# # CH10 - DATA STRUCTURES

# # Exercise 1:

# def main():
#     num_list = [int(x) for x in range(100)]
#     print("-----" * 10)
#     print("Multiples of 5 from 0-100")
#     print([int(x) for x in range(100) if x % 5 == 0])
#     print()
#     print(type(num_list), num_list, sep="\n")


# if __name__ == "__main__":
#     main()


# # Exercise 2:

# import math

# def factorial(x):
#     return math.factorial(x)

#     print(factorial(x))

# tuple1 = (5, 6, 7, 8, 9, 10)
# result = tuple(factorial(x) for x in tuple1)

# print(tuple1)
# print(result)
# print(type(result), result, sep="\t")


# # Exercise 3:

# import math

# def factorial(x):
#     return math.factorial(x)

#     print(factorial(x))

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = {x: factorial(x) for x in list}
# print(result)
# print("6! * 5! = ", result[6] * result[5]


# # Exercise 4:
# # file has 3 values per line (OwnerName, ComputerType, ComputerValue) == test2.txt
# # Read the lines and make a dictionary of dictionaries so
# # keys = owner, values = dictionary of computer type as key and computer value as value)
# # print the dictionary so that fmt = {'name' : {comptype: compvalue}}

# import sys

# file = open("test2.txt", "r")

# lines = file.readlines()
# file.close

# cust_dict = {}




# for line in lines:
#     name, comptype, compamt = line.split()  # unpack list into 3 variables
#     # check to see if the name is in there already get the key but if not then nothing
#     ctm = cust_dict.get(name) # first time, not there so none
#     if ctm:
#         value = ctm.get(comptype)   # get the type
#         if value:                           # returns none/false if not there
#             ctm[comptype] += int(compamt)
#         else:
#             ctm[comptype] = int(compamt)
#     else:
#         cust_dict[name] = {comptype: int(compamt)}

# print(cust_dict)

# pprint.pprint(cust_dict)  # better output formatting


print(map)


#--------------------------------------------------NOTES----------------------------------------------

#!/usr/bin/env python3  --> what is this for?

# return keyword exits a function and instructs Python to continue executing the main program
# return keyword can send a value back to the main program (allows data to be processed within a function)
# Ex: def foo() returns "2", instead of writing to the console, it gets used in def bar()
# so when foo() and bar() is printed, you see "2" and the result from bar()


# def sum(*args):
#   total = 0
#   print("Parameter type:", type(args), end=" ")
#   for elem in args:
#       total += elem
#   return total

# total = sum(1, 2, 3, 4, 5)
# print("Sum is: ", total)

# special dunder methods __init__,etc
# __eq__ / __neq__
# __lt__ / __gt__


# 'abc' < 'def' --> True

# Car.quantity = Class quantity
# dtor
# best place to close, clean up unmanaged resources --> __del__() == the destructor

# # Decorator in Python

# def decorator(func):
#        return func

# @decorator
# def some_func():
#     pass
# Is equivalent to this code:

# def decorator(func):
#     return func

# def some_func():
#     pass

# some_func = decorator(some_func)
# In the definition of a decorator you can add some modified things that wouldn't be returned by a function normally.

# ctrl + D
# goes to EOF

# try:
    # print(add(12, 3))
    # print("done")
# except RangeError as ex:
    # print("rg", ex)

# def add(n1, n2):
    # assert isinstance(n1, int), "n1 must be int"
    # return n1 + n2


# relative addressing 'r'


# 5 def main():
# 6   files = os.listdir(".")
# 7   fileinfo = {f: os.path.getsize(f) for f in files}  # file name : size
# 8   for name, size in fileinfo.items():
# 9   print("{0:30} : {1:>6} bytes".format(name, size))
