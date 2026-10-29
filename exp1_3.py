#while Loop problem statements

#1. Print Natural Numbers up to n
n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i = i + 1

    
#2. Print Even Numbers up to n
n = int(input("Enter n: "))

i = 2

while i <= n:
    print(i)
    i = i + 2

    
#3. Print Odd Numbers up to n
n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i = i + 2
    
#4. Print Sum of Natural Numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)


#1. Print Sum of Odd Numbers up to n
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum =", sum)

#2. Print Sum of Even Numbers up to n
n = int(input("Enter n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum =", sum)


#3. Print Natural Numbers up to n in Reverse Order
n = int(input("Enter n: "))

while n >= 1:
    print(n)
    n = n - 1
    
#4. Print Fibonacci Series up to n
n=int(input("enter number n: "))
i=0
j=1
sum=1
while(sum<=n):
    print(i)
    c=i+j
    i=j
    j=c
    sum+=1

    
#5. Find the Factorial of a Given Number
n = int(input("Enter a number: "))

fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print("Factorial =", fact)

#1. Check Whether a Number is Prime or Not
n = int(input("Enter a number: "))

i = 2
count = 0

while i < n:
    if n % i == 0:
        count = count + 1
    i = i + 1

if count == 0 and n > 1:
    print("Prime Number")
else:
    print("Not a Prime Number")

    
#2. Find the Sum of Digits of a Given Number
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of Digits =", sum)

#3. Check Whether the Entered Number is Palindrome or Not
n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

    
#4. Reverse the Given Number
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse Number =", rev)

#1. Print the Multiplication Table
n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1

    
#2. Print the Largest of n Numbers
n = int(input("Enter how many numbers: "))

i = 1

num = int(input("Enter number: "))
largest = num

while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest number =", largest)


#3. Print the Smallest of n Numbers
n = int(input("Enter how many numbers: "))

i = 1

num = int(input("Enter number: "))
smallest = num

while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest number =", smallest)
