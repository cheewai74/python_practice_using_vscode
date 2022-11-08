class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession
        
    #  Behavior (Instance method)
    def show(self):
        print("Name: " + self.name + " sex: " + self.sex + " profession: " + self.profession)
        
    #  Behavior (Instance method)
    def work(self):
        print(self.name + " is working as a "+self.profession)
        
ricky = Person('Ricky','Male','Software Engineer')

ricky.show()
ricky.work()
        