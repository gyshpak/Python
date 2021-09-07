int_list = []

item = 0
for item in range(10):
    int_list.append(item)
   
print(int_list)

for item in range(10):
    int_list[item] = float(int_list[item])
   
print(int_list)