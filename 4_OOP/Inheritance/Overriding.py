class Employee:
    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

class SalesOfficer(Employee):
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)
        self.inct=inc
    def getSalary(self):
        return self.salary + self.inct

e1 = Employee("Rajesh",9000)
print("{} is {}".format(e1.getName(),e1.getSalary()))

s1 = SalesOfficer("jaydev",12000,1000)
print("{} is {}".format(s1.getName(),s1.getSalary()))
