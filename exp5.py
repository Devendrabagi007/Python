#list_Problem_statements

#1.Write a Python program to create a list of five fruits and display the list.
 
#a = ["Apple","Mango","Bananna","Guava"]
#print(a)


#2. Create a list of five integers. Display:
# First element
# Last element
# Third element

#a = [1,2,3,4,5]
#print("First Element is:",a[0:1])
#print("First Element is:",a[4:5])
#print("First Element is:",a[2:3])

#3. Create a list of colors. Replace the third color with another color and display the
#updated list.

#a = ["Blue","Black","Yellow","Red","white"]
#print("The orginal list is:",a)
#a[2]= 'voilet'
#print("The updated list is:",a)

#4. Create a list of numbers. Add:
# One element at the end
# One element at the beginning
# One element at a specified position

#a = [1,2,3,4,5,6]
#print("The orignal list is:",a)
#a.append(7)
#a.insert(0,0)
#a.insert(4,55)
#print("The updated list is:",a)

#5. Create a list of student names. Remove:
# First student
# Last student
# A specific student by name
#Display the remaining list.

#a = ["dev","sam","Ram","sham"]
#print("The orginal list is:",a)
#a.remove("dev")
#a.pop(2)
#a.pop(0)
#print("The updated list is:",a)


#6. Write a program to find the largest and smallest number in a list without using max()
#or min().

#numbers = [10, 45, 20, 5, 30]

#largest = numbers[0]
#smallest = numbers[0]

#for num in numbers:
#    if num > largest:
#        largest = num

#    if num < smallest:
#        smallest = num

#print("Largest:", largest)
#print("Smallest:", smallest)

#7. Accept 10 numbers fromthe user and store themin a list. Calculate:
# Sum
# Average

#numbers = []

#for i in range(10):
#    num = int(input("Enter number: "))
#    numbers.append(num)

#total = sum(numbers)
#average = total / 10

#print("Sum:", total)
#print("Average:", average)

#8.Store 15 integers in a list. Count howmany numbers are:
# Even
# Odd

#numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

#even = 0
#odd = 0

#for num in numbers:
#    if num % 2 == 0:
#        even += 1
#    else:
#        odd += 1

#print("Even numbers:", even)
#print("Odd numbers:", odd)

#9. Create a list of cities. Ask the user to enter a city name and checkwhether it exists
#in the list.

#cities = ["Pune", "Mumbai", "Delhi", "Nagpur", "Kolhapur"]

#city = input("Enter city name: ")

#if city in cities:
#    print("City exists in the list")
#else:
#    print("City does not exist")

#10.Write a program to reverse a list without using the reverse()method
#numbers = [10, 20, 30, 40, 50]

#reversed_list = []

#for i in range(len(numbers)-1,-1,-1):
#  reversed_list.append(numbers[i])

#print(reversed_list)

#11. Create a list of 10 numbers and display:
# First 5 elements
# Last 5 elements
# Middle 4 elements
# Alternate elements
# Reverse list using slicing


#numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#print("First 5:", numbers[:5])
#print("Last 5:", numbers[-5:])
#print("Middle 4:", numbers[3:7])
#print("Alternate elements:", numbers[::2])
#print("Reverse:", numbers[::-1])


#12. Display all elements present at even index positions.

#numbers = [10, 20, 30, 40, 50, 60]

#for i in range(0, len(numbers), 2):
#    print(numbers[i])

#13. Accept 10 numbers and sort them in:
# Ascending order
# Descending order

#numbers = []

#for i in range(10):
#    num = int(input("Enter number: "))
#    numbers.append(num)

#numbers.sort()
#print("Ascending:", numbers)

#numbers.sort(reverse=True)
#print("Descending:", numbers)

#14. Create a list containing duplicate values and display only unique elements.

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

#15.Find the second largest element in a list

numbers = [10, 40, 20, 50, 30]

numbers.sort()

print("Second largest:", numbers[-2])

#16.Create a nested list storing:
# Student Name
# Roll Number
# Marks

students = [
    ["Rahul", 1, 85],
    ["Priya", 2, 90],
    ["Amit", 3, 78]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()

    
#17. Create two 3 × 3 matrices using nested lists and performmatrix addition.

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])

    result.append(row)

print("Result:")

for row in result:
    print(row)

    
#18. Create a shopping cart using a list.
#Perform:
# Add item
# Remove item
# Search item
# Display cart
# Count total items

    
cart = ["Milk", "Bread", "Rice"]

cart.append("Sugar")
cart.remove("Bread")

item = input("Enter item to search: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")

print("Shopping Cart:", cart)
print("Total Items:", len(cart))


#19.Store names of students present in class.
#Display:
# Total students
# Search a student's attendance
# Add a new student
# Remove an absent student


students = ["Rahul", "Amit", "Priya"]

print("Total Students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

new_student = input("Enter new student name: ")
students.append(new_student)

absent_student = input("Enter absent student name to remove: ")

if absent_student in students:
    students.remove(absent_student)

print("Updated List:", students)


#20.Create a list of books.
#Implement:
# Add a new book
# Search a book
# Remove a book
# Display all books
# Count total books


books = ["Python", "Java", "C++"]

new_book = input("Enter new book: ")
books.append(new_book)

search_book = input("Enter book to search: ")

if search_book in books:
    print("Book found")
else:
    print("Book not found")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)

print("Books:", books)
print("Total Books:", len(books))
