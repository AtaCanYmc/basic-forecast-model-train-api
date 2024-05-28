from flask import Flask, request, jsonify, current_app, Blueprint
from models import redWineModel
from config import Config

red_wines = Blueprint('red-wines', __name__)
app = current_app

@red_wines.route('/wines', methods=['GET'])
def get_wines():
    wines = redWineModel.WineQuality.query.all()
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
