print("Ques no.1\n")
print("Good Morning!")
print("Welcome to Python Programming.")
print("Have a Nice Day!")

print("\nQues no.2\n")
a = 10
b = 20
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

print("\nQues no.3\n")
num = int(input("Enter the number: "))
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i += 1

print("Factorial =", fact)