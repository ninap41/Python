class Product(object):
    def __init__(self, price,item_name,weight,brand,status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        if self.status == True:
            print "For Sale" 
        elif self.status == False:
            print "Sold" 
        return self
        self.display_all() 

    def sell(self):
        if self.status == True:
            print "For Sale"
        else:
            print "defective"  
        return self
        
    def add_tax(self):
        self.price += self.price *.12
        return self

    def return_it(self):
        if self.status == 'Defective':
            self.price= 0


    def display_all(self):
        print 'Price: $' + self.price
        print 'Name:' + str(self.item_name)
        print 'Weight:' + self.weight
        print 'Brand' + str(self.brand)
        print 'Status: ' + str(self.status)
    
thing_1=Product(12,"Tis A Shirt?", 9000,"The Closet Nihilist",True)
thing_2=Product(10,"another shirt?", 20,"The Closet Nihilist",False)
thing_3=Product(15,"burn the shirts", 20,"The Closet Nihilist",True)

# thing_1.sell().

# Status: default "for sale"
# Methods:

# • Sell: changes status to "sold"

# • Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

# • Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.

# • Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.
        

