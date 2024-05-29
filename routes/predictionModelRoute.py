from flask import Blueprint, jsonify, request
from models import predictionModel

prediction_models = Blueprint('prediction_models', __name__)

# READ (GET): Get all prediction models
@prediction_models.route('/prediction-models', methods=['GET'])
def get_prediction_models():
    models = predictionModel.PredictionModel.query.all()
    result = [
        {
            "id": model.id,
            "name": model.name,
            "description": model.description
        } for model in models
    ]
    return jsonify(result), 200

# READ (GET): Get a single prediction model by ID
@prediction_models.route('/prediction-models/<int:id>', methods=['GET'])
def get_prediction_model(id):
    model = predictionModel.PredictionModel.query.get_or_404(id)
    return jsonify({
        "id": model.id,
        "name": model.name,
        "description": model.description
    }), 200
