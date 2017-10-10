

class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100     
    def walk_walk(self):
        self.health = self.health - 5
        return self
    def run_run(self):
        #for i in range(1,4)    instead of walk walk walk walk just loopppp it dingus
        self.health = self.health - 10
        return self
    def displayHealth(self):
        print str(self.name), self.health 
        return self

animal_1= Animal('basicbill')
animal_1.walk_walk().walk_walk().walk_walk().run_run().run_run().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name) #instead of of super just declare the instant variables
        self.health = 150
    
    def pet_mine(self):
        self.health +=5
        return self

roofus_1 = Dog('Roofus')
roofus_1.walk_walk().walk_walk().walk_walk().run_run().run_run().displayHealth()

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170
        
    def flying_type(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "I am a dragon"
        super(Dragon, self).displayHealth()
        return self
    
smog_1 = Dragon('Smog')
smog_1.walk_walk().walk_walk().walk_walk().run_run().run_run().displayHealth()








        
