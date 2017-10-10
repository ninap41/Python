class Patient(object):
    Id = 500
    def __init__(self,allergies,name,):
        self.id = Patients.ID
        Patients.ID += 1
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        
class Hospital (object):
    def __init__(self,name,capacity):
         self.patients = []
        self.name = name
        self.capacity = capacity
    def admit_patients(self,name, allergies= None):
        if len(self.patients) >= self.capacity:
            print "We are full right now and cannot admit you"
        else: 
            new_patient = Patient(name,allergies)
            new_patient.bed = len(self.patients) +1
            self.patients.append(new_patient)
            print name + "you are now in our system for admission!"
            return self
    def discharge_patients(self, aname):
        for people in self.patients:
            if people.name == aname:
                self.patients.remove(people)
                print people.name + ', you have been discharged'
       
    def display_info(self):
        for people in self.patients:
            print "Id:", self.number, "Allergies: ", str(self.allergies), "Name: ", str(self.name), self.bed
        
patient = Hospital('lutheran', 10)
patient.admit_patients('The post office and being decent to women', 'Charles Bukowski')
patient.admit_patients('Sobriety','William S Burroughs')
patient.admit_patients('Ted Hughes','Sylvia Plath')
patient.admit_patients('Pennacilin','Jack Kirk')
patient.admit_patients('Bugs','Franz Kafka')
patient.admit_patients('happiness in general','Virginia Woolf')
patient.admit_patients('Thermasol',"Jane Smiley")
patient.admit_patients('using quotations','Cormac Mcarthy')
patient.admit_patients('good writing','James Patterson')
patient.admit_patients('describing ONE MEANINGLESS THING in less than 3 pages','JRR Tolkein')


hospital.display_info()

