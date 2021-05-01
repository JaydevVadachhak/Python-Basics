class Employee:
    def __init__(self):
        self.name = "kiran"
        self.salary = 20000
    def __str__(self):
        return "name="+self.name+"and salary="+str(self.salary)
e1 = Employee()
print(e1)
        
        
