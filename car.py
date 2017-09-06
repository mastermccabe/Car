class Car(object):
    def __init__(self, price, speed, fuel, milage):
        # self.price(price)
        self.price = price

        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        self.cartax()
        # self.tax = 0.12

    def cartax(self):

        if self.price > 10000: self.tax = 0.15
        else: self.tax = 0.12
        return self




    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Milage:",self.milage,"mpg"
        print "Tax:",self.tax

car1 = Car(20000,35,'Full',15)
car2 = Car(1000,35,'Kind of full',95)
car3 = Car(200,35,'Empty',25)
car4 = Car(200000,35,'Almost empty',15)
print "----------------- Car 1 ----------------- \n"
car1.display_all()
print "----------------- Car 2 ----------------- \n"
car2.display_all()
print "----------------- Car 3 ----------------- \n"
car3.display_all()
print "----------------- Car 4 ----------------- \n"
car4.display_all()
# display_all(car1)
