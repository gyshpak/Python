input_number = input("Please input four-digit natural number  ")

print("Your number is ", input_number)

print("Number in reverse order is ", input_number[::-1])

if len(input_number) == 4:
    i = 0
    multi_val = 1
    while i < len(input_number):
        multi_val *= eval(input_number[i])
        i+=1
    print(f"\nMultiplication all numbers is {multi_val} \n")
    
    print("Sort list is",sorted(input_number))

else:
    print("Try again to enter a 4-digit number \n")


        
