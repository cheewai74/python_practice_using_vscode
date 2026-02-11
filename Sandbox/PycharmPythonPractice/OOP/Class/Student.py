class Student:

    #  you should place the __init__ method after these class attributes
    # __init__ means initialization,
    # which refers to the process of setting the initial state
    # of the newly created instance object.
    def __init__(self, name):
        self.name = name
        self.registered = False
        self.guardian = None

    def verify_registration(self):
        self.registered = True

    def get_guardian_name(self):
        self.guardian = "Someone"