class Citizen:
    '''Full name citizen'''

    greeting = "For the glory of Python!"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        new = self.first_name + " " + self.last_name
        return new


c1 = Citizen("John", "Wick")
print(c1.full_name())