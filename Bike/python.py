# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...


class Bike(object):

    def __init__(self,price,max_speed, miles):   #Specifying arguments
        self.price= price         #sets all the instance variables. like declaring a variable
        self.max_speed = max_speed 
        self.miles= 0   #must convert strings when printing?


    def displayInfo(self):
        print '$ ' + str(self.price) + ',', str(self.max_speed) + ' mph,', str(self.miles) + ' miles'
        # print str(self.max_speed) + ' ' + 'mph' 
        # print str(self.miles) + ' ' + 'miles'
        # print "$" + self.price + self.max_speed + "Mph" + self.miles + "miles" still working on more efficientt way... to print all of them

    def ride(self):
        print "riding 10 miles"
        self.miles = self.miles + 10
        if self.miles > 30:
            print "crap my new bike, broke what a piece o crap"

    def reverseMiles(self):
        print 'cycling backwards 5 miles' 
        self.miles = self.miles - 5
        if self.miles < 0:
            self.miles = 0 # resets miles rode!
        
        
bike_1 = Bike(99.99, 12, 0)        #### attributes of instance inside instance
bike_2 = Bike(125.80, 10, 0)

print 'new bike! here are its stats and then lets take it for a ride'
print bike_1.displayInfo()
print 'Another new bike? here are its stats and then lets take it for a ride'
print bike_2.displayInfo()

bike_1.ride()
bike_1.ride()
bike_1.ride()
bike_1.reverseMiles()
print 'here are our stats after the bike ride.. notice how the object changed. Yay I dont suck today'
print bike_1.displayInfo()










