class Product(object):
    def __init__(self, price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def sell(self):
        self.status = "sold"
        return self
        
    def add_tax(self):
        self.price += self.price *.12
        return self

    def return_it(self, reason):
        if reason == "this torn":
            self.price = 0
            self.status = 'defective'
        elif reason == 'like new':
            self.status = 'for sale'
        elif reason == 'slight use':
            self.price -= (self.price * .20)
        else: 
            print "sorry no return"

    def display_info(self):
        print 'Price:$' , self.price
        print 'Name:', str(self.item_name)
        print 'Weight:' , self.weight, 'lbs.'
        print 'Brand:' , str(self.brand)
        print 'Status:' , str(self.status)
    
thing_1 = Product(12,"'Tis A Shirt?'", -1,"The Closet Existentialist")
thing_2=Product(10,"'What a Pointless Shirt'", -3,"The Closet Nihilist")
thing_3=Product(15,"'Burn All Shirts!'", -2,"The Closet Nihilist")


thing_1.display_info()
thing_2.display_info()
thing_3.display_info()
