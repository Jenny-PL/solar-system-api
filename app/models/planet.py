from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    dist_from_earth_in_million_km = db.Column(db.Integer)




# class Planet:
#     def __init__(self, id, name, description, dist_from_earth):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.dist_from_earth = dist_from_earth # million km
