from socketserver import ForkingMixIn, TCPServer


class Animal(object):
    pass


class Bird(Animal):
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class CarnivorousMixIn(object):
    pass


class HerbivoresMixIn(object):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass
