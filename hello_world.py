# print "hello world"
# x = "Hello Python"
# print x
# y = 42
# print y

# first_name = "Zen"
# last_name = "Coder"
# print "My name is {} {}".format(first_name, last_name)

# hw = "hello %s" % 'world'
# print hw
# # the output would be:
# # hello world

# x = "Hello World"
# print x.upper()
# # output:
# "HELLO WORLD"

# ninjas = ['Rozen', 'KB', 'Oliver']
# my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# empty_list = []
# print my_list + ninjas

# x = [1,2,3,4,5]
# x.append(99)
# x.append(100)
# print x
# #the output would be [1,2,3,4,5,99]

# x = [99,4,2,5,-3]
# print x[:]
# #the output would be [99,4,2,5,-3]
# print x[1:]
# #the output would be [4,2,5,-3];
# print x[:4]
# #the output would be [99,4,2,5]
# print x[2:4]
# #the output would be [2,5];


# my_list = [1, 'Zen', 'hi']
# print len(my_list)
# # output will be 3 with len


# age = 15
# if age >= 18:
#   print 'Legal age'
# else:
#   print 'You are so young!'

# for count in range(0, 5):
#     print "looping -", count
    


# # FOR LOOP through list/array
# my_list=[4,'dog', 99, ['list','inside','another'], 'hello world']   
# for element in my_list: 
#     print element 

# # FOR LOOP through string
# for val in "string":
#   if val == "i":
#     break
#   print val

def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in arr:
        print x
        x *= num
        print x
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

