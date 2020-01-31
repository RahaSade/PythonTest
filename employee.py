class Employee:
    raise_amt = 1.05


    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

        '''
        as you can see it seems that this class has different properties, such as first, last, pay that we didn't define them beforehand.
        moreover, different properties such as email and fullname are just defined using the previous information we had so far!
        '''