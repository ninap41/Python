my_dict = {
"Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def my_dict_tuple(data):
   for key in data:
       print key, data[key]
   print my_dict.items()
#    for key,value in my_dict.iteritems():
#        key,value.items()
#        new_list = [tuple((key,value))]
#        new_list.items()
my_dict_tuple(my_dict)