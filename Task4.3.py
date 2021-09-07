number_Fib = int(input("Enter number "))

item = 2
if number_Fib != 0 and number_Fib != 1:
    list_Fib = [0,1]
    while item < number_Fib:
        list_Fib.append(list_Fib[item-1] + list_Fib[item-2])
        item +=1

    print (list_Fib)
