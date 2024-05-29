from flask import Blueprint, request, jsonify, abort
from config import db
from models.validationData import ValidationData, ValidationRow

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
    return jsonify({"id": new_validation_data.id}), 201


@validation_blueprint.route('/validation-data/<int:id>', methods=['GET'])
def get_validation_data(id):
    validation_data = ValidationData.query.get(id)
    if validation_data is None:
        abort(404)
    return jsonify({
        "id": validation_data.id,
        "train_data": validation_data.train_data,
        "percentage": validation_data.percentage
    })


@validation_blueprint.route('/validation-data/<int:id>', methods=['PUT'])
def update_validation_data(id):
    data = request.get_json()
    validation_data = ValidationData.query.get(id)
    if validation_data is None:
        abort(404)
    validation_data.train_data = data.get('train_data', validation_data.train_data)
    validation_data.percentage = data.get('percentage', validation_data.percentage)
    db.session.commit()
    return jsonify({"message": "ValidationData updated"})


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
