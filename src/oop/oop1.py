# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # base class
    pass


class FlightVehicle(Vehicle):  # vehicle is a base class, flight vehicle derives from it
    pass


class Starship(FlightVehicle):  # flight vehicle is a base class and starship derives from it
    pass


class Airplane(FlightVehicle):  # flight vehicle is a base class and airplane derives from it
    pass


class GroundVehicle(Vehicle):  # vehicle is a base class, ground vehicle derives from it
    pass


class Car(GroundVehicle):  # ground vehicle is a base class, car derives from it
    pass


class Motorcycle(GroundVehicle):  # ground vehicle is a base class, motorcycle derives from it
    pass
