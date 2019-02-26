class Vehicle :
    
    def __init__(self, price, year) :
        self.price = price
        self.year = year
        
class Car(Vehicle) :
    
    def __init__(self, price, year, wheel_count, capacity) :
        Vehicle.__init__(self, price, year)
        self.wheel_count = wheel_count
        self.capacity = capacity
    
    def pay_tax(self) :
        return self.price*(0.15)

    def park(self,hour) :
        total = 1250*self.wheel_count*hour
        if self.capacity > 5 :
            total += 5000
        return total
    
class Motorbike(Vehicle):
    
    def __init__(self, price, year, wheel_count, capacity) :
        Vehicle.__init__(self, price, year)
        self.wheel_count = wheel_count
        self.capacity = capacity
    
    def pay_tax(self) :
        return self.price*(0.1)
    
    def park(self,hour) :
        total = 1250*self.wheel_count*hour
        if self.capacity > 5 :
            total += 5000
        return total     

class Bicycle(Vehicle):
    
    def __init__(self, price, year, wheel_count, capacity):
        Vehicle.__init__(self, price, year)
        self.wheel_count = wheel_count
        self.capacity = capacity
        
    def pay_tax(self):
        return self.price*0

    def park(self,hour):
        total = 1250*self.wheel_count*hour
        if self.capacity > 5 :
            total += 5000
        return total
