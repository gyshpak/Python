zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never .
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

list_zen = zen.split()

find_words = ['better','never','is']

len_zen = len(list_zen)

len_words = len(find_words)

#count_words = 0

j = 0
while j < len_words:
    i = 0
    count_words = 0 
    while i< len_zen:
        if find_words[j] == list_zen[i]:
            count_words +=1
        i+=1
    
    print(f"count {find_words[j]} is ", count_words)
    j+=1     

str_zen = zen.replace('\n',' ')
print("\n UPPER TEXT: \n", str_zen.upper())

print("\nChanged i to & \n", zen.replace('i','&'))
