from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, dist_from_earth):
        self.id = id
        self.name = name
        self.description = description
        self.dist_from_earth = dist_from_earth # million km

planet_list = [
    Planet(1, "Mercury", "smallest, closest to Sun", 92),
    Planet(2, "Venus", "hottest, spins opposite direction", 41),
    Planet(3, "Earth", "home, liquid water on surface, known living things", 0),
    Planet(4, "Mars", "dusty, cold, thin atmospher", 78),
    Planet(5, "Jupiter", "more than two times larger than others", 629),
    Planet(6, "Saturn", "many icy rings", 1275),
    Planet(7, "Uranus", "27 moons, rotates on its side", 2273),
    Planet(8, "Neptune", "dark, cold, supersonic winds", 4351)
]