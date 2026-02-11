class Person:
    def greet(self):
        print('I am a Person')


# class Teacher:
class Teacher(Person):

    def greet(self):
        super().greet()
        print('I am a Teacher')


# class Student:
class Student(Person):
    def greet(self):
        super().greet()
        print('I am a student')


class TeachingAssistant(Student, Teacher):
    # pass # Searches from left to right (o/p will display Student

    def greet(self):
        super().greet()
        print('I am a Teaching Assistant')


x = TeachingAssistant()
x.greet()
print(TeachingAssistant.__bases__)