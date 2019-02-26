class pets:

    

    def __init__(self,list):
        self.list = list
    
    def is_hungry(self):
        index = 0
        while(index < len(self.list) and self.list[index].hungry != True ):
            index += 1
        if (self.list[index-1].hungry == True):
            return True
        else : 
            return False
    
    def whos_hungry(self):
        who_hungry = []
        for x in self.list:
            if(x.hungry == True):
                who_hungry.append(x)
        return who_hungry





class animal: #class untuk pets

    def __init__(self,name,age,hungry): #fungsi untuk inisiasi data hewan
        self.name = name
        self.age = age
        self.hungry = hungry
    
    def eat(self) : #fungsi mengembalikan true dari hungry
        self.hungry = False
        return self.hungry

class cat(animal): #subclass dari animal  
    def __init__(self,name,age,hungry,cat_species): #inisiasi data kucing
        animal.__init__(self,name,age,hungry)
        self.cat_species = cat_species


    def sound(self): #mengeluarkan suara kucing 
        return 'Miaw\n' 

class dog(animal): #subclass dari animal
    def __init__(self,name,age,hungry,dog_species): #inisiasi data anjing
        animal.__init__(self,name,age,hungry)
        self.dog_species = dog_species
    
    def sound(self): #mengeluarkan suara anjing
        return 'gukguk\n'

class bird(animal): #subclass dari animal
    def __init__(self,name,age,hungry,bird_species): #inisiasi data burung
        animal.__init__(self,name,age,hungry)
        self.bird_species = bird_species
    
    def sound(self): #mengeluarkan suara burung
        return 'chirp\n'
    
  

x1 = cat("kucing",18,False,"Felis Catus")
x2 = cat("kucing",18,True,"Felis Catus")
x3 = cat("kucing",18,True,"Felis Catus")

y1 = dog("guk",18,False,"Felis anjing")
y2 = dog("guk",18,True,"Felis anjing")
y3 = dog("guk",18,True,"Felis anjing")

z1 = bird("chip",18,False,"Felis burung")
z2 = bird("chip",18,True,"Felis burung")
z3 = bird("chip",18,True,"Felis burung")

x_cat = [x1,x2,x3]
y1 = pets(x_cat)
print(y1.is_hungry())

list_hasil = y1.whos_hungry()
print(list_hasil)
for x in list_hasil :
    print("nama:{} age:{} hungry:{} cat_species:{}".format(x.name, x.age, x.hungry, x.cat_species))


x1.eat()


# print("nama:{} age:{} hungry:{} cat_species:{}".format(x1.name, x1.age,x1.hungry,x1.cat_species)) 
    

