import types

class Dog:
    def bark(self):
        print("WOOF")

boby = Dog()
boby.bark() # WOOF

def _bark(self):
    print("WoOoOoF!!")

boby.bark = types.MethodType(_bark, boby)

boby.bark() # WoOoOoF!!