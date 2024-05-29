import os

from flask import Blueprint, jsonify, request
from config import db
from models import trainData, predictionModel, nullDataSolution
from models.redWine import get_red_wine_data_as_dataframe
from static.trainPreprocessUtils import shuffle_data
from static.trainModelUtils import train_model_with_strategy
from static.trainAfterProcessUtils import save_model

train_data_blueprint = Blueprint('train_data_blueprint', __name__)


def train_model(train_data_id):
    train_data = trainData.TrainData.query.get(train_data_id)
    if not train_data:
        print("TrainData not found")
        return None

    wine_dataframe = get_red_wine_data_as_dataframe(train_data.number_of_train_row)  # DataFrame
    wine_dataframe = shuffle_data(wine_dataframe) if train_data.is_shuffle else wine_dataframe  # Shuffle

    model = train_model_with_strategy(wine_dataframe, train_data.kpi_column_name, train_data.prediction_model)
    model_path = save_model(train_data_id, model)
    return model_path


@train_data_blueprint.route('/train-data', methods=['POST'])
def create_train_data():
    data = request.json
    new_train_data = trainData.TrainData(
        prediction_model=data['prediction_model'],
        null_data_solution=data['null_data_solution'],
        number_of_train_row=data['number_of_train_row'],
        kpi_column_name=data.get('kpi_column_name'),
        is_shuffle=data.get('is_shuffle', False),
        is_normalize=data.get('is_normalize', False),
        is_standardization=data.get('is_standardization', False),
        is_sum_column=data.get('is_sum_column', False),
        sum_column_name=data.get('sum_column_name'),
        is_average_column=data.get('is_average_column', False),
        average_column_name=data.get('average_column_name')
    )
    db.session.add(new_train_data)
    db.session.commit()

    path = train_model(new_train_data.id)

    return jsonify({
        "message": "Train data added successfully.",
        "train_data": {
            "id": new_train_data.id,
            "path": path,
            "prediction_model": new_train_data.prediction_model,
            "null_data_solution": new_train_data.null_data_solution,
            "number_of_train_row": new_train_data.number_of_train_row,
            "kpi_column_name": new_train_data.kpi_column_name,
            "is_shuffle": new_train_data.is_shuffle,
            "is_normalize": new_train_data.is_normalize,
            "is_standardization": new_train_data.is_standardization,
            "is_sum_column": new_train_data.is_sum_column,
            "sum_column_name": new_train_data.sum_column_name,
            "is_average_column": new_train_data.is_average_column,
            "average_column_name": new_train_data.average_column_name
        }
    }), 201


@train_data_blueprint.route('/train-data', methods=['GET'])
def get_all_train_data():
    train_data = trainData.TrainData.query.all()
    result = []

    for data in train_data:
        null_solution = nullDataSolution.NullDataSolution.query.filter_by(id=data.null_data_solution).first()
        prediction_model = predictionModel.PredictionModel.query.filter_by(id=data.prediction_model).first()

        result.append({
            "id": data.id,
            "prediction_model": {
                "id": data.prediction_model,
                "name": prediction_model.name,
                "description": prediction_model.description,
            } if prediction_model else None,
            "null_data_solution": {
                "id": data.null_data_solution,
                "name": null_solution.name,
                "description": null_solution.description
            } if null_solution else None,
            "number_of_train_row": data.number_of_train_row,
            "kpi_column_name": data.kpi_column_name,
            "is_shuffle": data.is_shuffle,
            "is_normalize": data.is_normalize,
            "is_standardization": data.is_standardization,
            "is_sum_column": data.is_sum_column,
            "sum_column_name": data.sum_column_name,
            "is_average_column": data.is_average_column,
            "average_column_name": data.average_column_name
        })

    return jsonify(result), 200


@train_data_blueprint.route('/train-data/<int:id>', methods=['GET'])
def get_train_data_by_id(id):
    data = trainData.TrainData.query.get_or_404(id)
    null_solution = nullDataSolution.NullDataSolution.query.filter_by(id=data.null_data_solution).first()
    prediction_model = predictionModel.PredictionModel.query.filter_by(id=data.prediction_model).first()
    return jsonify({
        "id": data.id,
        "prediction_model": {
            "id": data.prediction_model,
            "name": prediction_model.name,
            "description": prediction_model.description,
        } if prediction_model else None,
        "null_data_solution": {
            "id": data.null_data_solution,
            "name": null_solution.name,
            "description": null_solution.description
        } if null_solution else None,
        "number_of_train_row": data.number_of_train_row,
        "kpi_column_name": data.kpi_column_name,
        "is_shuffle": data.is_shuffle,
        "is_normalize": data.is_normalize,
        "is_standardization": data.is_standardization,
        "is_sum_column": data.is_sum_column,
        "sum_column_name": data.sum_column_name,
        "is_average_column": data.is_average_column,
        "average_column_name": data.average_column_name
    }), 200


@train_data_blueprint.route('/train-data/<int:id>', methods=['DELETE'])
def delete_train_data(id):
    train_data = trainData.TrainData.query.get_or_404(id)
    db.session.delete(train_data)
    db.session.commit()
    os.remove(f"prediction-model-saves/model-{id}.pickle")
    return jsonify({"message": "Train data deleted successfully."}), 200
