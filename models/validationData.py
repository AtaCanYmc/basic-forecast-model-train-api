from config import db


class ValidationData(db.Model):
    __tablename__ = 'validation_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    train_data = db.Column(db.Integer, db.ForeignKey('train_data.id'), nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    validation_rows = db.relationship('ValidationRow', backref='validation_data', cascade='all, delete-orphan')


class ValidationRow(db.Model):
    __tablename__ = 'validation_row'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    train_data = db.Column(db.Integer, db.ForeignKey('train_data.id'), nullable=False)
    validation_data = db.Column(db.Integer, db.ForeignKey('validation_data.id'), nullable=False)
    actual = db.Column(db.Float, nullable=False)
    prediction = db.Column(db.Float, nullable=False)
    error = db.Column(db.Float, nullable=False)
