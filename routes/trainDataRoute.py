from flask import Blueprint, jsonify, request, current_app
from config import db
from models import trainData, predictionModel, nullDataSolution
from models.redWine import get_red_wine_data_as_dataframe
from static.trainPreprocessUtils import shuffle_data

train_data_blueprint = Blueprint('train_data_blueprint', __name__)


def train_model(train_data_id):
    train_data = trainData.TrainData.query.get(train_data_id)
    if not train_data:
        print("TrainData not found")
        return

    wine_dataframe = get_red_wine_data_as_dataframe(train_data.number_of_train_row)
    wine_dataframe = shuffle_data(wine_dataframe) if train_data.is_shuffle else wine_dataframe
    print(wine_dataframe)


@train_data_blueprint.route('/train-data', methods=['POST'])
def create_train_data():
    data = request.json
    new_train_data = trainData.TrainData(
        prediction_model=data['prediction_model'],
        null_data_solution=data['null_data_solution'],
        model_path=data.get('model_path'),
        validation_percentage=data['validation_percentage'],
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

    train_model(new_train_data.id)

    return jsonify({
        "message": "Train data added successfully.",
        "train_data": {
            "id": new_train_data.id,
            "prediction_model": new_train_data.prediction_model,
            "null_data_solution": new_train_data.null_data_solution,
            "model_path": new_train_data.model_path,
            "validation_percentage": new_train_data.validation_percentage,
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
            "prediction_model_id": data.prediction_model,
            "prediction_model_name": prediction_model.name if prediction_model else None,
            "null_data_solution": data.null_data_solution,
            "null_data_solution_name": null_solution.name if null_solution else None,
            "model_path": data.model_path,
            "validation_percentage": data.validation_percentage,
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
        "prediction_model": data.prediction_model,
        "prediction_model_name": prediction_model.name if prediction_model else None,
        "null_data_solution": data.null_data_solution,
        "null_data_solution_name": null_solution.name if null_solution else None,
        "model_path": data.model_path,
        "validation_percentage": data.validation_percentage,
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

    return jsonify({"message": "Train data deleted successfully."}), 200
