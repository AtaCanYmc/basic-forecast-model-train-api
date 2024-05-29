from flask import Blueprint, jsonify
from models import nullDataSolution

null_data_solutions = Blueprint('null_data_solutions', __name__)

@null_data_solutions.route('/null-data-solutions', methods=['GET'])
def get_null_data_solutions():
    all_null_data_solutions = nullDataSolution.NullDataSolution.query.all()
    result = [
        {
            "id": solution.id,
            "name": solution.name,
            "description": solution.description
        } for solution in all_null_data_solutions
    ]
    return jsonify(result), 200

@null_data_solutions.route('/null-data-solutions/<int:solution_id>', methods=['GET'])
def get_null_data_solution(solution_id):
    solution = nullDataSolution.NullDataSolution.query.get_or_404(solution_id)
    return jsonify({
        "id": solution.id,
        "name": solution.name,
        "description": solution.description
    }), 200
