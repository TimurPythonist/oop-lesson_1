# class Employee:
#     pass

# Marian = Employee()
# Bob = Employee()

# print(Marian)
# print(Bob)
# print(type(Marian))
# print(type(Bob))
# print(type('ABC'))
# print(isinstance(Marian, Employee))   
# print(isinstance('ABC', str))
# print(isinstance(1000, int))


# # create a clsss # #
class Employee:

    # # class attributes # #
    os = 'Windows 2010'
    work_style = 'remote'
    hourly_salary = 15

    # # constructor method / initializer # #
    def __init__(self, role, is_manager, location = 'New York branch') -> None:
        self.role = role
        self.is_manager = is_manager
        self.location = location

    def bio(self):
        return f'Hello! I am a {self.role} and I am located in work in {self.location} branch'

# # create object/instance # #
Marian = Employee('Developer', False, 'Singapore')
Bob = Employee('QA', True)

print(Marian.bio())
print(Bob.bio())
# print(Marian.role)
# print(Bob.is_manager)
# print(Bob.role)

# # # update class atribute # #
# Employee.hourly_salary = 16.75
# Marian.hourly_salary = 30
# Employee.hourly_salary = 18

# print(Marian.os)
# print(Bob.work_style)
# print(Marian.hourly_salary)
# print(Employee.os)

# print(Bob.hourly_salary)
# print(Marian.hourly_salary)

# Employee.os = 'Lunix'

# print(Marian.os)
# print(Bob.os)

# print(id(Employee.hourly_salary))
