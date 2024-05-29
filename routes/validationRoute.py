from flask import Blueprint, request, jsonify, abort
from config import db
from models.validationData import ValidationData, ValidationRow
from models.trainData import TrainData

validation_blueprint = Blueprint('validation_blueprint', __name__)


# ValidationData Routes
@validation_blueprint.route('/validation-data', methods=['POST'])
def create_validation_data():
    data = request.get_json()
    new_validation_data = ValidationData(
        train_data=data['train_data'],
        percentage=data['percentage']
    )
    db.session.add(new_validation_data)
    db.session.commit()
    train_data = TrainData.query.filter_by(id=new_validation_data.train_data).first()
    return jsonify({
        "id": new_validation_data.id,
        "percentage": new_validation_data.percentage,
        "train_data": {
            "id": train_data.id,
            "prediction_model": train_data.prediction_model,
            "null_data_solution": train_data.null_data_solution,
            "number_of_train_row": train_data.number_of_train_row,
            "kpi_column_name": train_data.kpi_column_name,
            "is_shuffle": train_data.is_shuffle,
            "is_normalize": train_data.is_normalize,
            "is_standardization": train_data.is_standardization,
            "is_sum_column": train_data.is_sum_column,
            "sum_column_name": train_data.sum_column_name,
            "is_average_column": train_data.is_average_column,
            "average_column_name": train_data.average_column_name
        } if train_data else None
    }), 201


@validation_blueprint.route('/validation-data', methods=['GET'])
def get_all_validation_data():
    validation_data_list = ValidationData.query.all()
    result = []
    for validation_data in validation_data_list:
        train_data = TrainData.query.get(validation_data.train_data)

        result.append({
            "id": validation_data.id,
            "train_data": {
                "id": train_data.id,
                "prediction_model": train_data.prediction_model,
                "null_data_solution": train_data.null_data_solution,
                "number_of_train_row": train_data.number_of_train_row,
                "kpi_column_name": train_data.kpi_column_name,
                "is_shuffle": train_data.is_shuffle,
                "is_normalize": train_data.is_normalize,
                "is_standardization": train_data.is_standardization,
                "is_sum_column": train_data.is_sum_column,
                "sum_column_name": train_data.sum_column_name,
                "is_average_column": train_data.is_average_column,
                "average_column_name": train_data.average_column_name
            } if train_data else None,
            "percentage": validation_data.percentage
        })
    return jsonify(result)


@validation_blueprint.route('/validation-data/<int:id>', methods=['GET'])
def get_validation_data(id):
    validation_data = ValidationData.query.get(id)
    if validation_data is None:
        abort(404)

    train_data = TrainData.query.filter_by(id=validation_data.train_data).first()
    validation_rows = ValidationRow.query.filter_by(validation_data=validation_data.id).all()
    validation_rows_list = [{
        "id": row.id,
        "train_data": row.train_data,
        "validation_data": row.validation_data,
        "actual": row.actual,
        "prediction": row.prediction,
        "error": row.error
    } for row in validation_rows]
    return jsonify({
        "id": validation_data.id,
        "train_data": {
            "id": train_data.id,
            "prediction_model": train_data.prediction_model,
            "null_data_solution": train_data.null_data_solution,
            "number_of_train_row": train_data.number_of_train_row,
            "kpi_column_name": train_data.kpi_column_name,
            "is_shuffle": train_data.is_shuffle,
            "is_normalize": train_data.is_normalize,
            "is_standardization": train_data.is_standardization,
            "is_sum_column": train_data.is_sum_column,
            "sum_column_name": train_data.sum_column_name,
            "is_average_column": train_data.is_average_column,
            "average_column_name": train_data.average_column_name
        } if train_data else None,
        "percentage": validation_data.percentage,
        "validation_rows": validation_rows_list
    })


@validation_blueprint.route('/validation-data/<int:id>', methods=['DELETE'])
def delete_validation_data(id):
    validation_data = ValidationData.query.get(id)
    if validation_data is None:
        abort(404)
    db.session.delete(validation_data)
    db.session.commit()
    return jsonify({"message": "ValidationData deleted"})


@validation_blueprint.route('/validation-row/<int:id>', methods=['GET'])
def get_validation_row(id):
    validation_row = ValidationRow.query.get(id)
    if validation_row is None:
        abort(404)
    return jsonify({
        "id": validation_row.id,
        "train_data": validation_row.train_data,
        "validation_data": validation_row.validation_data,
        "actual": validation_row.actual,
        "prediction": validation_row.prediction,
        "error": validation_row.error
    })
