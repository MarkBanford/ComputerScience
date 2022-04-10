'''Define a class called Student that can be created with name only
It will have a greeting function that randomly picks a greeting
It will also have a function to create a bunch of student objects
'''
from random import choice


class Student:
    educational_platform = 'online'

    def __init__(self, name, age=25):
        self.name = name
        self.age = age

    def greeting(self):
        greetings = ["Hi, I'm", "Hey there, my name is", "Hi, oh my name is"]
        return f'{choice(greetings)} {self.name}'


def class_create(student_names):
    return [Student(name) for name in student_names]


if __name__ == '__main__':
    names = ['Bill', 'Mary', 'John']

for student in class_create(names):
    print(student.greeting())
