
#tests
c = ['magical unicorns',19,'hello',98.98,'world']
g= [2,3,1,7,4,12]
y= ['magical','unicorns']

count_int = 0
count_str = 0
makestring = "String:"
sum =0

y =['magical','unicorns']
for x in y:
    if (type(x) == int):
        count_int +=1
        sum = sum + x
    if(type(x) == str):
        count_str +=1
        makestring = "made string:" + y[0] + ''  

if (count_int == 0):
    print "The list you entered was a string"
elif (count_str == 0):
    print "The list you entered was a integer"
else:
    print "that was a mixed list"


if (count_str != 0):
    print makestring
if (count_int != 0):
    print "Sum:", sum





