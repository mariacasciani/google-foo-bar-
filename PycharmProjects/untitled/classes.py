# write a function to deposit money
# classes are a way to classify all objects that correspond to a certain set
# they are a way to create infrastructure
# inside a class BankAccount
# -function always acts on BankAccount
# -bankaccount class has a certain consistency


class BankAccount(object):

    def __init__(self, starting_balance):
        self.balance = starting_balance

    def deposit(self, additional_money):
        print 'Depositing $'+str(additional_money)
        self.balance += additional_money

    def withdraw(self, money_to_withdraw):
        print "Withdrawing $"+str(money_to_withdraw)
        self.balance -= money_to_withdraw


class Student(object):

    def __init__(self, money):
        self.money = money
        self.year = 'Freshman'
        self.classes = []
        self.finished_classes = {}

    def enroll(self, new_class):
        self.classes.append(new_class)

    def switch(self, old_class, new_class):
        self.classes.remove(old_class)
        self.enroll(new_class)

    def pass_class(self, passed_class, grade):
        self.finished_classes[passed_class] = grade

    def change_year(self):
        self.years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
        if len(self.finished_classes.keys()) == len(self.classes):
            self.year = self.years[self.years.index(self.year)+1]

    def calculate_gpa(self):
        total = 0.0
        for grade in self.finished_classes.values():
            total+= grade
        self.gpa = float(total)/len(self.finished_classes.values())
    #def foo(self): #foo must always act
        #Bankaccount.foo(my_bank_account)
        #my_bank_account.foo()


my_bank_account = BankAccount(starting_balance=100)
print type(my_bank_account)
print my_bank_account.balance
my_bank_account.deposit(20)
print my_bank_account.balance
my_bank_account.withdraw(80)
print my_bank_account.balance

new_student = Student(money=100)
new_student.enroll('8.01')
new_student.enroll('7.012')
new_student.enroll('18.03')
new_student.enroll('24.00')
print new_student.classes
new_student.pass_class('8.01', 5.0)
new_student.pass_class('7.012', 5.0)
new_student.pass_class('18.03', 5.0)
new_student.pass_class('24.00', 4.0)
print new_student.finished_classes
new_student.change_year()
print new_student.year
new_student.calculate_gpa()
print new_student.gpa

class Undergraduate(Student):
    #Overriding a method:
    #if a subclass has the same method as its parent class that when calling the method from a subclass
    #the interpreter will call subclass method instead
    #these types of methods are polymorphic
    def enroll(self, new_class):
        print "Student enrolled in", new_class
        self.classes.append(new_class)

#Undergraduate - subclass. "inherits' all attributes and method of its parent
#Student is a superclass, parent class, or base class of Undergraduates

Alice = Undergraduate(money=100)
print Alice.money #100
print Alice.classes # []
print isinstance(Alice, Undergraduate)
print isinstance(Alice, Student)
print Undergraduate.__bases__ #returns Student

class Freshman(Undergraduate):
    def __init__(self, money, year):
        super(Undergraduate, self).__init__(money)
        self.year = year

print Freshman.__bases__ #only returns Undergraduate
