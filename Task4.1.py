input_value = int(input("Input number: "))

i=1
your_factorial = input_value

while i < input_value:
    your_factorial *= (input_value - i)
    i+=1
print("Your factorial is: ", your_factorial)
