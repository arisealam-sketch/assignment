num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

toal = 0
for num in range(1, 51):
    toal += num
print("the sum of number from 1 to 50is", toal)