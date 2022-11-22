from Common.Mammal import Mammal

class Dog(Mammal):

    legs = 6
    eyes = 2

    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print('Whoof', 'Whoof')

    # # this is a static methob, meant to be called directly from the class # #
    @staticmethod
    def walk():
        print('I am walking')

# # object # # 
Clifford = Dog('Clifford', 2, 'Huskie')

Mammal.bio()
Dog.bio()
Clifford.bio()

# print(Mammal.feeds_milk)
# print(Dog.feeds_milk)
# print(Clifford.feeds_milk)
# print(message)
# say_hello()
# Clifford.bark()
# Dog.walk()
# Clifford.walk()