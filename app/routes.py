from urllib import response
from flask import Blueprint, jsonify, request, abort, make_response
from .models.planet import Planet
from app import db


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST"])
def create_one_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body['name'],description=request_body['description'],dist_from_earth_in_million_km=request_body['dist_from_earth_in_million_km'])
    db.session.add(new_planet)
    db.session.commit()
    return {
        'id': new_planet.id,
        'msg': f'New planet {new_planet.name} added. The planet id is: {new_planet.id}'
    }, 201

@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all() # this will get all Planet instances
    planet_list = []
    for planet in planets:
        planet_list.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'dist_from_earth_in_million_km': planet.dist_from_earth_in_million_km
        })
    return jsonify(planet_list), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet: {planet_id} is not a valid planet id"}, 400))
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"Planet: #{planet_id} not found"}, 404))
    return planet

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    response = {
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'dist_from_earth_in_million_km': planet.dist_from_earth_in_million_km
        }
    return jsonify(response), 200

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    try:
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.dist_from_earth_in_million_km = request_body['dist_from_earth_in_million_km']
    except KeyError:
        return {"message": "Planet name, description, and distance from Earth all required to update planet"}, 400

    db.session.commit()

    response = {"message": f"Planet {planet.name} successfully updated"}
    return jsonify(response), 200




# class Planet:
#     def __init__(self, id, name, description, dist_from_earth):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.dist_from_earth = dist_from_earth # million km

# planet_list = [
#     Planet(1, "Mercury", "smallest, closest to Sun", 92),
#     Planet(2, "Venus", "hottest, spins opposite direction", 41),
#     Planet(3, "Earth", "home, liquid water on surface, known living things", 0),
#     Planet(4, "Mars", "dusty, cold, thin atmospher", 78),
#     Planet(5, "Jupiter", "more than two times larger than others", 629),
#     Planet(6, "Saturn", "many icy rings", 1275),
#     Planet(7, "Uranus", "27 moons, rotates on its side", 2273),
#     Planet(8, "Neptune", "dark, cold, supersonic winds", 4351)
# ]

# @planet_bp.route("", methods=['GET'])
# def get_all_planets():
#     planet_response = []
#     for planet in planet_list:
#         planet_response.append({
#             'id': planet.id,
#             'name': planet.name,
#             'description': planet.description,
#             'average distance from earth (million km)': planet.dist_from_earth
#         })
#     return jsonify(planet_response), 200

# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return jsonify({'message': 'Invalid input. Enter planet id number'}), 400
#     for planet in planet_list:
#         if planet.id == planet_id:
#             response = {
#                 'id': planet.id,
#                 'name': planet.name,
#                 'description': planet.description,
#                 'average distance from earth (million km)': planet.dist_from_earth
#             }
#             return jsonify(response), 200

#     return jsonify({"message": f"Invalid planet_id: {planet_id}. Could not find planet"}), 404

