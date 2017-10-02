# multiples
odd = 0
for odd in range(1,1000):
    if odd % 2 != 0:
        print odd

five = 0
for five in range(5,1000000):
    if five % 5 == 0:
        print five
# sum list
sum = 0
a = [1, 2, 5, 10, 255, 3]
for i in a:
    sum = sum + i
    print sum




#average list

a = [1, 2, 5, 10, 255, 3]
print(sum(a) / len(a))