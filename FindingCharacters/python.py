
char = 'n'
new_list = []
list = ['hello', 'world', 'my', 'name', 'is', 'Anna', 'lol']
for x in list:
    for letter in x:
        if (letter == char):
                new_list.append(x)
print new_list