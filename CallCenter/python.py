class Call(object):
    def __init__(self, unique_id,name,phonenumber,time):
        self.unique_id = unique_id
        self.name = name
        self.phonenumber = phonenumber
        self.time = time
        self.display_all()
              
    def display_all(self):
        # for i in call: loop in call center
        print "ID: ", self.unique_id, "Name: ", str(self.name),"Number: " , self.phonenumber, "time: " , self.time
        return self




class CallCenter(object):

    def __init__(self):
        self.calls = []
    def add(self, call):
        self.calls.append(call)
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def remove_number(self):
        for number in self.calls:
            if self.unique_id == 1111:
                del self.calls[self.unique_id.index(number)]
        return self
    def info(self):
        for info in self.calls:
            info.display()
        print len(self.calls)
        return self

callcenter_1=Call(1111,"Rick Dickinsin","7739999999","5:00AM")
callcenter_2=Call(1312,"Mitch Mickenwhatever","873827382738","5:00PM")
callcenter_3=Call(1378,"Rachel wtfson","99999999999",'7:00PM')

callcenter_4=Call(1111,"Rick Dickinsin","7739999999","5:00AM")
callcenter_5=Call(1312,"Mitch Mickenwhatever","873827382738","5:



    