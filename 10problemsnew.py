# // -- (1) Find largest number and minimum number in array --/


numbers = [45, 78, 30, 28, 49, 12, 4, 100, 223, 922]

minimum = numbers[0]
maximum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number

print(f"The minimum number is: {minimum}")
print(f"The maximum number is: {maximum}")


# // --  2- Count Even and Odd Numbers -- //

numbers = [2, 4, 19, 14, 30, 39, 48, 46, 59, 20, 40, 50, 27, 28, 15]

print(f"Total numbers: {len(numbers)}")

even_count = 0
odd_count = 0

for number in numbers:

    if number % 2 == 0:
        even_count = even_count + 1

    else:
        odd_count = odd_count + 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")



# // -- 3- Search for an Element --//

names = ["Ali", "Ahmed", "Hamza", "Usman", "Bilal",
         "Hassan", "Saad", "Zain", "Umar", "Talha"]

search_name = input("Enter a name: ")

if search_name in names:
    print(f"{search_name} is found in the list.")

else:
    print(f"{search_name} is not found in the list.")


# // -- 4- Remove Duplicate Values --//

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = []

for number in numbers:

    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"Original List: {numbers}")
print(f"Unique List: {unique_numbers}")

# // -- 5- Student Marks Analysis --//

marks = [45, 78, 92, 33, 67, 50, 84, 39]

maximum = marks[0]
minimum = marks[0]

total = 0
above_50 = 0

for mark in marks:

    if mark > maximum:
        maximum = mark

    if mark < minimum:
        minimum = mark

    total = total + mark

    if mark >= 50:
        above_50 = above_50 + 1

average = total / len(marks)

print(f"Highest Mark: {maximum}")
print(f"Lowest Mark: {minimum}")
print(f"Average Mark: {average}")
print(f"Students with 50 or above: {above_50}")



# // -- 6- Student Record Using Dictionary --//


students = {
    "Ali": 78,
    "Ahmed": 65,
    "Hamza": 92,
    "Usman": 55
}

student_name = input("Enter student name: ")

marks = students.get(student_name)

if marks is not None:
    print(f"{student_name}'s marks are: {marks}")

else:
    print("Student not found")


# // -- 7- Count Word Frequency --//


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1

    else:
        frequency[word] = 1

print(frequency)



# // -- 8: Product Price Lookup --//


products = {
    "Laptop": 120000,
    "Mouse": 2500,
    "Keyboard": 5000,
    "Headphones": 7000
}

product_name = input("Enter product name: ")

price = products.get(product_name)

if price is not None:
    print(f"{product_name} price is: {price}")

else:
    print("Product not found")


# // -- 9- Grade Counter --//


grades = ["A", "B", "A", "C", "B", "A",
          "D", "F", "C", "A", "B", "F"]

grade_count = {}

for grade in grades:

    if grade in grade_count:
        grade_count[grade] = grade_count[grade] + 1

    else:
        grade_count[grade] = 1

print(grade_count)




# // -- 10: Inventory Management --//



inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15,
    "Headphones": 8
}

item = input("Enter item name: ")
quantity = int(input("Enter quantity to purchase: "))

if item in inventory:

    if inventory[item] >= quantity:
        inventory[item] = inventory[item] - quantity

        print("Purchase successful!")
        print(f"Updated {item} quantity: {inventory[item]}")

    else:
        print("Insufficient stock")

else:
    print("Item not found")