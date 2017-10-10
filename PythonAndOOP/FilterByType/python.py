# INTEGER PRINT GREATER AND LESS
# num = 50
# if num >= 100:
#     print "thats a big number dude."
# if num <100:
#     print "Thats a teeny number man"

# # STRING
# string = "This is a dang string and python is weird"
# if string >= 50:
#     print "Long sentence."
# if string<100:
#     print "Short Sentence"

#LIST

# sI = 45
# mI = 100
# bI = 455
# eI = 0
# spI = -23
# sS = "Rubber baby buggy bumpers"
# mS = "Experience is simply the name we give our mistakes"
# bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# eS = ""
# aL = [1,7,4,21]
# mL = [3,5,7,34,3,2,113,65,8,89]
# lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# eL = []
# spL = ['name','address','phone number','social security number']


x = ['name','address','phone number','social security number']
if (type(x) == int):
    if (x >= 100):
            print "thats a big number dude."
    else:
            print "Thats a teeny number man"
elif(type(x) == str):
    if (len(x) >= 100):
            print "Long sentence."
    else:
            print "Short Sentence"
elif (type(x) == list):
    if (len(x) >= 100):
            print "Big list"
    else:
            print "Short List"
else:
            print "Neither of these types!"
           


