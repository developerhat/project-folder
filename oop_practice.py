#OOP Practice 04/08/20



class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@patgo.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('pat','go',300000)
emp_2 = Employee('xavier', 'braxis',15000)


#emp_1.first = "Pat"
#emp_1.last = "G"
#emp_1.email = 'pat.g@patrickgo.com'
#emp_1.pay = '300,000'

#emp_2.first = "Pet"
#emp_2.last = "f"
#emp_2.email = 'patooly'
#emp_2.pay = '20,000'


print(Employee.fullname(emp_2))

print(emp_2.fullname())
