students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
  
#   Part 1

def names_names(student_list):
    for student in student_list:
        print student['first_name'], student['last_name']
names_names(students)

# PART 2

def names_names(student_list):
    for key, value in student_list.iteritems():
        print key
        for names in value:
            print value.index(names) + 1," ",names['first_name'],names['last_name'], "-",len(names['first_name'])+len(names['last_name'])
names_names(users)

