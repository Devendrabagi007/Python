#operators

#1.floor Division 
#a = int(input("Enter the number one:"))
#b = int(input("Enter the number second:"))

#sum = a//b 

#print("The result is:", sum)

#2.Normal division
#a = int(input("Enter the number one:"))
#b = int(input("Enter the number second:"))

#sum = a/b

#print("The result is:", sum)


#-------------------------------------------------------------------------------

#if loop problem statement

#1.
n = int(input("Enter a number: "))

if n == 0:
    print("Number is Zero")
else:
    print("Number is Non-Zero")

#2.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

    
#3.
n = int(input("Enter a number: "))

if n >= 0:
    print("Number is Positive")
else:
    print("Number is Negative")

#Alternative (checks Zero separately):

n = int(input("Enter a number: "))

if n > 0:
    print("Number is Positive")
elif n < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


#4. 
ch = input("Enter a character: ")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("It is a Vowel")
else:
    print("It is a Consonant")

#1. Student Performance Evaluation
per = float(input("Enter percentage: "))

if per >= 90:
    print("Excellent Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print("Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")

    
#2. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is", a)
elif b >= a and b >= c:
    print("Largest number is", b)
else:
    print("Largest number is", c)


#3. Smallest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is", a)
elif b <= a and b <= c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)


#1. Check Whether a Number is Even or Odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


#2. Check Whether a Year is a Leap Year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

    
#3. Driver Insurance Program
status = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if status == "married":
    print("Driver is Insured")
elif status == "unmarried" and gender == "male" and age > 30:
    print("Driver is Insured")
elif status == "unmarried" and gender == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")
