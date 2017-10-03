

scores = [50,40,20,100,99,20,]
def students_grades(sores):
    print "Students Grades!"
    for i in scores:
        if (i > 90 and i <= 100):
            print "Score: ", i,"; Your grade is A"
        elif (i > 80 and i  <= 90):
            print  "Score: ", i,"; Your grade is B"
        elif (i  > 70 and i  <= 80):
            print "Score: ", i,"; Your grade is C"
        elif (i  > 60 and i  <= 70):
            print "Score: ", i,"; Your grade is D"
        else:
            print "Youuuuu failureeee"


students_grades(scores)
        
#functions
# def read_from_list(list):
#     for thing in list:
#         print thing

# test_list = [1,2,3]
# read_from_list(test_list)