class Employee:

    def __init__(self, fname, lname):

        self.fname = fname
        self.lname = lname

    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'
    
    @property
    def prop_email(self):
        return f'{self.fname}.{self.lname}@gmail.com'

    @property
    def fullname(self):
        return f'{self.fname} {self.lname}'
    
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.lname = None
        print('name deleted')

emp = Employee('Klay', 'Thompson')

print(emp.fname)
print(emp.lname)
print('\n-------- Access email method ----------')
print(emp.email())

print('\n-------- Access method prop_email() and fullname() as an class property without () ----------')
emp.fullname = 'Dray Green' # Set full name as the new one
print(emp.prop_email)
print(emp.fullname)

print('\n-------- Invoke delete operation ----------')
del emp.fullname
print(emp.prop_email)
print(emp.fullname)