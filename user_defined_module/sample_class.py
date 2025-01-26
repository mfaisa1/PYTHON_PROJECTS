class Employee:
 def __init__(self,first,second):
  self.first=first
  self.second=second

 def fullname(self):
  return '{} {}'.format(self.first,self.second)

emp1=Employee('mohammad','faisal')
## print(emp1.fullname())
##def test():
 ##print("hello")