from flask import Flask, request, jsonify, current_app, Blueprint
from models import redWine

red_wines = Blueprint('red-wines', __name__)
app = current_app


@red_wines.route('/red-wines/columns', methods=['GET'])
def get_wine_columns():
    columns = []
    for column in redWine.RedWine.__table__.columns:
        columns.append({
            "name": column.name,
            "type": str(column.type)
        })
    return jsonify({"columns": columns}), 200


# READ (GET): List all red wines
@red_wines.route('/red-wines', methods=['GET'])
def get_wines():
    wines = redWine.RedWine.query.all()
    result = [
        {
            "id": wine.id,
            "fixed_acidity": wine.fixed_acidity,
            "volatile_acidity": wine.volatile_acidity,
            "citric_acid": wine.citric_acid,
            "residual_sugar": wine.residual_sugar,
            "chlorides": wine.chlorides,
            "free_sulfur_dioxide": wine.free_sulfur_dioxide,
            "total_sulfur_dioxide": wine.total_sulfur_dioxide,
            "density": wine.density,
            "pH": wine.pH,
            "sulphates": wine.sulphates,
            "alcohol": wine.alcohol,
            "quality": wine.quality
        } for wine in wines
    ]
    return jsonify(result)


# READ (GET): Get a specific red wine by ID
@red_wines.route('/red-wines/<int:id>', methods=['GET'])
def get_wine_by_id(id):
    wine = redWine.RedWine.query.get(id)
    if wine:
        result = {
            "id": wine.id,
            "fixed_acidity": wine.fixed_acidity,
            "volatile_acidity": wine.volatile_acidity,
            "citric_acid": wine.citric_acid,
            "residual_sugar": wine.residual_sugar,
            "chlorides": wine.chlorides,
            "free_sulfur_dioxide": wine.free_sulfur_dioxide,
            "total_sulfur_dioxide": wine.total_sulfur_dioxide,
            "density": wine.density,
            "pH": wine.pH,
            "sulphates": wine.sulphates,
            "alcohol": wine.alcohol,
            "quality": wine.quality
        }
        return jsonify(result), 200
    else:
        return jsonify({"error": "Red wine not found."}), 404


# CREATE (POST): Add a new red wine
@red_wines.route('/red-wines', methods=['POST'])
def create_wine():
    data = request.json
    wine = redWine.RedWine(**data)
    redWine.db.session.add(wine)
    redWine.db.session.commit()
    return jsonify({"message": "Red wine added successfully."}), 201


# UPDATE (PUT): Update a specific red wine
@red_wines.route('/red-wines/<int:id>', methods=['PUT'])
def update_wine(id):
    wine = redWine.RedWine.query.get(id)
    if wine:
        data = request.json
        for key, value in data.items():
            setattr(wine, key, value)
        redWine.db.session.commit()
        return jsonify({"message": "Red wine updated successfully."}), 200
    else:
        return jsonify({"error": "Red wine not found."}), 404


# DELETE: Delete a specific red wine
@red_wines.route('/red-wines/<int:id>', methods=['DELETE'])
def delete_wine(id):
    wine = redWine.RedWine.query.get(id)
    if wine:
        redWine.db.session.delete(wine)
        redWine.db.session.commit()
        return jsonify({"message": "Red wine deleted successfully."}), 200
    else:
        return jsonify({"error": "Red wine not found."}), 404
