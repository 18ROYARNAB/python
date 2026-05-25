class bank:
    def __init__(self,name : str , balance : int):
        self.name= name
        #private attribute 
        self.__balance = balance
    # GETTER
    def get_balance(self):
        print(f"Current balance : {self.__balance}")
    
    # SETTER
    def set_balance(self,new_amount):
        self.__balance = new_amount

# method hide
    def __is_serverlive(self):
        return True

    def deposit(self,amount: int):
        if self.__is_serverlive() is True :
            self.__balance += amount
            print(f"Amount desposited {amount},Balance : {self.__balance} ")
    def withdrawl(self,amount: int):
        if amount>self.__balance:
            print("Insufficient balance ")
        else:
            self.__balance -= amount
            print(f" Amount withdrawn: {amount}, current balance = {self.__balance}\n")

acc=bank("arnab",5000)
acc.deposit(1000)
# acc.balance=100000  # not affect after private attribute __balance from balance
acc.withdrawl(1999)