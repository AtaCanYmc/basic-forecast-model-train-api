from config import db


class TrainData(db.Model):
    __tablename__ = 'train_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prediction_model = db.Column(db.Integer, db.ForeignKey('prediction_model.id'), nullable=False)
    null_data_solution = db.Column(db.Integer, db.ForeignKey('null_data_solutions.id'), nullable=False)
    validation_percentage = db.Column(db.Float, nullable=False)
    number_of_train_row = db.Column(db.Integer, nullable=False)
    kpi_column_name = db.Column(db.String(255), default=None)
    is_shuffle = db.Column(db.Boolean, default=False)
    is_normalize = db.Column(db.Boolean, default=False)
    is_standardization = db.Column(db.Boolean, default=False)
    is_sum_column = db.Column(db.Boolean, default=False)
    sum_column_name = db.Column(db.String(255), default=None)
    is_average_column = db.Column(db.Boolean, default=False)
    average_column_name = db.Column(db.String(255), default=None)
