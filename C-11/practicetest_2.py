class Animals:
    pass
class Pets(Animals):
     pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("BARRRRK")
d=Dog()
d.bark()

