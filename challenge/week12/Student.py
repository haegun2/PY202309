class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_average(self):
        return (self.korean + self.math + self.english)/3