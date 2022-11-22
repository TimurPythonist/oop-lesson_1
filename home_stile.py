# # create a clsss # #
class House:

    # # class attributes # #
    room_size = 'Large'
    style = 'classic'
    floor_level = 3

    # # constructor method / initializer # #
    def __init__(self, public, is_obj) -> None:
        self.public = public
        self.is_obj = is_obj
    
    def bio(self):
        return f'Still available {self.public}'

# # create object/instance # #
Modern = House('NO', False)
Historic = House('YES', True)



print(Modern.bio())
print(Historic.bio())
print(Modern.bio())

# # create object/instance # #
# Modern = House()
# Historic = House()

# # # update class atribute # #
# House.floor_level = 2
# House.style = 'modern'
# House.floor_level = 4

# print(Modern.room_size)
# print(Historic.floor_level)