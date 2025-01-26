class Employee:
    increment = 1.04
    no_of_emp = 0
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
        Employee.no_of_emp += 1


    def fullname(self):
        return self.first+self.last
    
 

    
    def raise_sal(self):
        self.sal= int(self.sal*self.increment)
    


emp1=Employee('mohammad','faisal',100)
emp2=Employee('mohammad','fahad',200)
print(emp1.fullname())
print(Employee.no_of_emp)
print("current sal",emp1.sal)
#emp1.raise_sal()
#print("sal post inc",emp1.sal)
emp1.increment=1.05
emp1.raise_sal()
print("sal post inc",emp1.sal)

print(emp1.__dict__)
print(Employee.__dict__)