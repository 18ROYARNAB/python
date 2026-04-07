class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print ("Need food to eat")

    def sleep(self):
        print("Sleepy")
    def move(self):
        print("1211")
class dog(animal):
    def __init__(self, name : str , age : int , breed : str):
        super().__init__(name,age)
        self.breed=breed
        print(f"dog breed :{self.breed} ")
    def bark(self):
        print("barking")
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")
    def move(self):
        print("31212")
class cat(animal):
    def meow(self):
        print ("mewoww")
    
Wilddog= dog("cherry",4,"labradaor") 

Wilddog.move()

