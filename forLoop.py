#For Loop problem statements.


#1. Print Natural Numbers up to n
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)

    
#2. Print Even Numbers up to n
n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)
#3. Print Odd Numbers up to n
n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)

    
#4. Print the Series 1 2 4 8 16 32 ... up to n Terms
n = int(input("Enter number of terms: "))

x = 1

for i in range(1, n + 1):
    print(x)
    x = x * 2

    
#5. Sum the Series 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)


#6.Write a PYTHON program to compute the cosine series cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!









#7. Check Whether the Square Root of a Number is Prime or Not

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))
count = 0

for i in range(2, root):
    if root % i == 0:
        count = count + 1

if count == 0 and root > 1:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")

    
#8. Produce the Following Design
A B C
A B C
A B C
for i in range(3):
    for j in range(65, 68):
        print(chr(j), end=" ")
    print()


#9. Produce the Following Design
#A
#A B
#A B C
#A B C D
#A B C D E


















#10.10. Produce the Following Design
#A B C D E
#A B C D
#A B C
#A B
#A















#11. Write a PYTHON program to produce following design
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5














      

#12. Write a PYTHON program to produce following design
#1
#2 2
#3 3 3
#4 4 4 4 
#5 5 5 5 5

    


    
