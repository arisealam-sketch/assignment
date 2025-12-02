def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial


n = int(input("enter a number: "))
print(f"factorial of {n} is {fact(n)}")

import math

a = int(input("enter a number: "))
result = math.sqrt(a)
natural_log = math.log(a)
sin_value = math.sin(a)

out = math.sqrt(a)
print(f"square root of {a} is {out}")
print(f"logarithm: {math.log(a)}")
print(f"Sine:{math.sin(a)}")
