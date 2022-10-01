"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

"""
Commission classes

"""

class CommissionInterface:

    def __commission_str__(self):
        pass

    def get_commission_pay(self):
        pass


class NoCommission(CommissionInterface):
    
    def __commission_str__(self):
        return ""

    def get_commission_pay(self):
        return 0


class AbstractYesCommission(CommissionInterface):

    def __init__(self, commission):
        self._commission = commission


# (commission) is a fixed bonus commission
class BonusCommission(AbstractYesCommission):

    def __commission_str__(self):
        return  " and receives a bonus commission of " + str(self._commission)

    def get_commission_pay(self):
        return self._commission


# (commission) is the per contract commission
class ContractCommission(AbstractYesCommission):
    
    def __init__(self, commission, contracts):
        super().__init__(commission)
        self._contracts = contracts
    
    def __commission_str__(self):
        return " and receives a commission for " + str(self._contracts) + \
               " contract(s) at " + str(self._commission) + "/contract"

    def get_commission_pay(self):
        return self._commission * self._contracts
    
"""
Employee classes

"""

class AbstractEmployee:
    
    def __init__(self, name, pay):
        self._name = name

        self._pay = pay

    def get_main_pay(self):
        pass

    def get_pay(self):
        return self.get_main_pay() + self.get_commission_pay()

    def __employment_str__(self):
        pass

    def __str__(self):
        return self.__employment_str__() + self.__commission_str__() + \
               ".  Their total pay is " + str(self.get_pay()) + "."


# (pay) is the monthly pay
class AbstractSalaryEmployee(AbstractEmployee):
    
    def __init__(self, name, pay):
        AbstractEmployee.__init__(self, name, pay)

    def get_main_pay(self):
        return self._pay

    def __employment_str__(self):
        return self._name + " works on a monthly salary of " + str(self._pay)
    

""" (pay) is the hourly pay """
class AbstractContractEmployee(AbstractEmployee):
    
    def __init__(self, name, pay, hours):
        AbstractEmployee.__init__(self, name, pay)
        
        self._hours = hours

    def get_main_pay(self):
        return self._pay * self._hours

    def __employment_str__(self):
        return self._name + " works on a contract of " + str(self._hours) + \
               " hours at " + str(self._pay) + "/hour"

class SalaryEmployeeNoCommission(AbstractSalaryEmployee, NoCommission):
    pass

class ContractEmployeeNoCommission(AbstractContractEmployee, NoCommission):
    pass


class SalaryEmployeeBonusCommission(AbstractSalaryEmployee, BonusCommission):

    def __init__(self, name, pay, commission):
        AbstractSalaryEmployee.__init__(self, name, pay)
        BonusCommission.__init__(self, commission)


class SalaryEmployeeContractCommission(AbstractSalaryEmployee, ContractCommission):
    
    def __init__(self, name, pay, commission, contracts):
        AbstractSalaryEmployee.__init__(self, name, pay)
        ContractCommission.__init__(self, commission, contracts)

        
class ContractEmployeeBonusCommission(AbstractContractEmployee, BonusCommission):
    
    def __init__(self, name, pay, hours, commission):
        AbstractContractEmployee.__init__(self, name, pay, hours)
        BonusCommission.__init__(self, commission)


class ContractEmployeeContractCommission(AbstractContractEmployee, ContractCommission):
    
    def __init__(self, name, pay, hours, commission, contracts):
        AbstractContractEmployee.__init__(self, name, pay, hours)
        ContractCommission.__init__(self, commission, contracts)



# Billie works on a monthly salary of 4000.  Their total pay is 4000.

billie = SalaryEmployeeNoCommission("Billie", 4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.

charlie = ContractEmployeeNoCommission("Charlie", 25, 100)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s)
# at 200/contract.  Their total pay is 3800.

renee = SalaryEmployeeContractCommission("Renee", 3000, 200, 4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s)
# at 220/contract.  Their total pay is 4410.

jan = ContractEmployeeContractCommission("Jan", 25, 150, 220, 3)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.
# Their total pay is 3500.

robbie = SalaryEmployeeBonusCommission("Robbie", 2000, 1500)


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.
# Their total pay is 4200.

ariel = ContractEmployeeBonusCommission("Ariel", 30, 120, 600)

print(billie.__str__() + "\n")
print(charlie.__str__() + "\n")
print(renee.__str__() + "\n")
print(jan.__str__() + "\n")
print(robbie.__str__() + "\n")
print(ariel.__str__() + "\n")
