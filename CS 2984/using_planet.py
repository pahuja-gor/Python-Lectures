# lowercase because of planet.py

def print_planet_info(my_planet):
    print("Name:", my_planet.get_name())
    print("Radius:", my_planet.get_radius())
    print("Mass:", my_planet.get_mass())
    print("Volume:", my_planet.get_volume())
    print("Surface Area:", my_planet.get_surface_area())
    print("Density:", my_planet.get_density())
    print("Distance:", my_planet.get_distance())


from planet import *

# uppercase because of Class name
myPlanet = Planet("X25", 45, 198, 1000)

print_planet_info(myPlanet)
print('')

# create Earth using mutators
myPlanet.set_name("Earth")
myPlanet.set_radius(6371)
myPlanet.set_mass(5.97e24)
myPlanet.set_distance(152087701)

print_planet_info(myPlanet)

mercury = Planet("Mercury", 19, 10, 25)
mars = Planet("Mars", 47, 50, 35)

print('')
print("Mars > Mercury?", mars > mercury)