value1 = int(input("Input value1 - "))
value2 = int(input("Input value2 - "))

# value1, value2 = value2, value1

# print(f"New value1 {value1}")
# print(f"New value2 {value2}")
value1 += value2
value2 =value1 - value2
value1 -= value2

print(f"New value1 {value1}")
print(f"New value2 {value2}")