 # Creating a dictonary where the student name are keys value there

students= {
     "Arsh": 85,
     "bob": 75,
     "Ronit": 90,
     "Rahul": 87
  }
  # Ask the use to input a students name

name = input("Enter a students name: ")
if name in students:
        print(f"{name}'s marks: {students[name]} ")
else:
         print("Student not found.")

# creating a list of
numbers = list(range(1,11))
# extract first five Element
first_five = numbers[:5]
# reverse there extracted elements
reversed_first_five = first_five[::-1]
print(f'orignal list: {numbers}')
print(f'Extract First Five: {first_five}')
print(f'reversed list: {reversed_first_five}')