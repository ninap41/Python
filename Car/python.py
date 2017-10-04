class Car():

    def __init__(self,price,speed,fuel,mileage,tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
        if price > 10000:
           self.tax = .15
        else:
            self.tax = .12
        self.display_all()

        
    def display_all(self):
        print "Car Stats"
        print 'Price: $' + str(self.price) + ', Speed:', str(self.speed) + ' mph, Mileage:', str(self.fuel) + ' miles','Fuel:' + str(self.fuel),'Tax: ' + str(self.tax)


car_1=Car(2000,35,'Full',15,.12)
car_2=Car(2000,5,'not full',105,.12)
car_3=Car(2000,15,'Kind of Full',105,.12)
car_4=Car(2000,25,'Full',25,.12)
car_5=Car(2000,45,'Empty',25, .12)
car_6=Car(2000,35,'Empty',15,.15)






