from config import db


class PredictionModel(db.Model):
    __tablename__ = 'prediction_model'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<RegressionModel {self.name}>'
