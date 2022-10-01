"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

TYPE_SALARY = 1
TYPE_CONTRACT = 2

COMMISSION_TYPE_NONE = 0
COMMISSION_TYPE_BONUS = 1
COMMISSION_TYPE_CONTRACT = 2


class Employee:
    
    def __init__(self, type, name, pay, hours, ctype, commission, contracts):
        self._type = type
        self._name = name
        self._pay = pay
        self._hours = hours
        self._ctype = ctype
        self._commission = commission
        self._contracts = contracts

        self._fpay = self.calc_full_pay()
        self._dstr = self.__make_str__()

    def get_pay(self):
        return self._fpay
        

    def calc_full_pay(self):

        match self._type:
            case x if x == TYPE_SALARY:
                mpay = self._pay

            case x if x == TYPE_CONTRACT:
                mpay = (self._pay * self._hours)

        
        match self._ctype:
            case x if x == COMMISSION_TYPE_BONUS:
                cpay = self._commission
                
            case x if x == COMMISSION_TYPE_CONTRACT:
                cpay = self._commission * self._contracts
                
            case _:
                cpay = 0
        

        return cpay + mpay 


    def __str__(self):
        return self._dstr
                
    def __make_str__(self):

        match self._type:
            case x if x == TYPE_SALARY:
                mstr = self._name + " works on a monthly salary of " + str(self._pay)

            case x if x == TYPE_CONTRACT:
                mstr = self._name + " works on a contract of " + str(self._hours) + \
                       " hours at " + str(self._pay) + "/hour"
        
            
        match self._ctype:
            case x if x == COMMISSION_TYPE_BONUS:
                cstr = " and receives a bonus commission of " + str(self._commission)
                epay = self._commission
                
            case x if x == COMMISSION_TYPE_CONTRACT:
                cstr = " and receives a commission for " + str(self._contracts) + \
                       " contract(s) at " + str(self._commission) + "/contract"
                epay = self._commission * self._contracts
                
            case _:
                cstr = ""
                epay = 0


        return mstr + cstr + ".  Their total pay is " + str(self._fpay) + "."
    
 

# Billie works on a monthly salary of 4000.  Their total pay is 4000.

billie = Employee(TYPE_SALARY, "Billie", 4000, 0, COMMISSION_TYPE_NONE, 0, 0)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.

charlie = Employee(TYPE_CONTRACT, "Charlie", 25, 100, COMMISSION_TYPE_NONE, 0, 0)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s)
# at 200/contract.  Their total pay is 3800.

renee = Employee(TYPE_SALARY,
                 "Renee",
                 3000,
                 0,
                 COMMISSION_TYPE_CONTRACT,
                 200,
                 4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s)
# at 220/contract.  Their total pay is 4410.

jan = Employee(TYPE_CONTRACT,
               "Jan",
               25,
               150,
               COMMISSION_TYPE_CONTRACT,
               220,
               3)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.
# Their total pay is 3500.

robbie = Employee(TYPE_SALARY,
                  "Robbie",
                  2000,
                  0,
                  COMMISSION_TYPE_BONUS,
                  1500,
                  0)


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.
# Their total pay is 4200.

ariel = Employee(TYPE_CONTRACT,
                 "Ariel",
                 30,
                 120,
                 COMMISSION_TYPE_BONUS,
                 600,
                 0)

print(billie.__str__() + "\n")
print(charlie.__str__() + "\n")
print(renee.__str__() + "\n")
print(jan.__str__() + "\n")
print(robbie.__str__() + "\n")
print(ariel.__str__() + "\n")


                 
