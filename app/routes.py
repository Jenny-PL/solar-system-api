from flask import Blueprint, jsonify

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
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=['GET'])
def get_all_planets():
    planet_response = []
    for planet in planet_list:
        planet_response.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'average distance from earth (million km)': planet.dist_from_earth
        })
    return jsonify(planet_response), 200

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({'message': 'Invalid input. Enter planet id number'}), 400
    for planet in planet_list:
        if planet.id == planet_id:
            response = {
                'id': planet.id,
                'name': planet.name,
                'description': planet.description,
                'average distance from earth (million km)': planet.dist_from_earth
            }
            return jsonify(response), 200

    return jsonify({"message": f"Invalid planet_id: {planet_id}. Could not find planet"}), 404

