list_numbers = [2, 8, 20, 43, 4, 56, [7, 4], 6]

# item = 0

# while item < len(list_numbers):

#     if list_numbers[item] % 2 != 0:
#         break        
#     item +=1

# print ("Your list conteins odd numer", list_numbers[item])


for item in list_numbers:

    if item % 2 != 0:
        #break
        continue
    print ("Your list conteins odd numer", item)

