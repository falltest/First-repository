import random

class Human:
    '''Our First class'''
    genom_count = 46
    #атрибут класса
    def __init__(self, name: str, age: int, description: str):
        self.name = name 
        self.age = age
        self.description = description
    def show_description(self):
        print(f'{self.name}, {self.description}, {self.age} years old')
    @classmethod
    def get_genom_count(cls):
        return cls.genom_count
    @classmethod
    def set_genom_count(cls, count: int):
        cls.genom_count = count
    @staticmethod
    def choice_name():
        return random.choice('ILIAS', 'SVETA', 'MAKS')
human = Human('Denis', 23, 'cool')
print(human.show_description())