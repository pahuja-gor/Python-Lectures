import math

class Planet:

    def __init__(self, iName, iRad, iM, iDist):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist

    def get_name(self):
        return self.__name
    def get_radius(self):
        return self.__radius
    def get_mass(self):
        return self.__mass
    def get_distance(self):
        return self.__distance

    def get_volume(self):
        return (4/3) * math.pi * self.__radius**3
    def get_surface_area(self):
        return 4 * math.pi * self.__radius**2
    def get_density(self):
        return (self.__mass / self.get_volume())

    def set_name(self, new_name):
        self.__name = new_name
    def set_radius(self, new_radius):
        self.__radius = new_radius
    def set_mass(self, new_mass):
        self.__mass = new_mass
    def set_distance(self, new_dist):
        self.__distance = new_dist

    def __str__(self):
        return self.__name
    def __lt__(self, otherPlanet):
        return self.__distance < otherPlanet.__distance
    def __gt__(self, otherPlanet):
        return self.__distance > otherPlanet.__distance