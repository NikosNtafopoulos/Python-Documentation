# A class is basicaly a blueprint for creating instances
# Instances are class-based generated elements
# Instance contains data that is unique for every instance
# each regular method on a class takes automaticaly the instance as a first argument --> self
# classmethods recieving the class[cls] as the first argument and not the instance like self
# staticmethods dont pass anything automaticaly


class Emp:
    # global variable within the class
    empNum = 0
    bonus = 1000
    # special method init(initialize) || on other langauges is known as constructor

    def __init__(self, firstN, lastN, pay):
        # instances variables
        self.firstN = firstN
        self.lastN = lastN
        self.pay = pay
        self.email = firstN + '.'+lastN+'@email.com'
        # tracking our employees
        Emp.empNum += 1  # Emp.empNum = Emp.empNum + 1

    def fullname(self):
        return 'First Name: {}, Last Name: {}'.format(self.firstN, self.lastN)

    def payment(self):
        return 'Anual Payment: {}, contact: {}'.format(self.pay, self.email)

    def applyBonus(self):
        self.pay = int(self.pay + self.bonus)

    # classmethod
    @classmethod
    def setBonus(cls, amount):
        cls.bonus = amount + cls.bonus

    @staticmethod
    def is_workDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#                Inheritance
# example classes of employees [developers,technicians]
class Developer(Emp):
    bonus = 5000


class Technicians(Emp):
    pass


emp1 = Emp('John', 'Smith', 20000,)
#print (Emp.fullname(emp1))
emp2 = Emp('Nik', 'Doe', 15000)

#     First Testing
print emp1.fullname()
print emp1.email
print emp1.payment()
print emp2.fullname()
print emp2.email
print emp2.payment()
#print emp1.applyBonus()
#     testing
# print(emp1.__dict__)
#print (Emp.__dict__)
Emp.setBonus(100)
print 'Employess so far: ' + str(Emp.empNum)
#print Emp.bonus
print emp1.fullname() + '\nis Employee in Tech Company with bonus :' + \
    str(emp1.bonus) + ' Euros'

#print help(Developer)
emp3 = Developer('Nik', 'Doe', 40000)
print emp3.fullname() + '\nIs a Developer with  Anual payment:' + str(emp3.pay)
emp3.setBonus(200)
emp3.applyBonus()
