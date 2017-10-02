
#tests
c = ['magical unicorns',19,'hello',98.98,'world']
g= [2,3,1,7,4,12]
y= ['magical','unicorns']

count_int = 0
count_str = 0
makestring = "String:"
sum =0

y = ['magical','unicorns']
for y in x:
    if (type(x) == int):
        Countin +=1
        sum = sum + x
    if(type(x) == str):
        Countstr +=1
        makestring = x + '' + makestring  

if (count_int == 0):
    print "The list you entered is of mixed type"
elif (count_str == 0):
    print "that was a integer list"
else:
    print "that was a mixed list"


if (count_str != 0):
    print makestring
if (count_int != 0):
    print "Sum:", sum





