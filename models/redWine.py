from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WineQuality(db.Model):
    __tablename__ = 'red_wine_quality'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fixed_acidity = db.Column(db.Float, nullable=False)
    volatile_acidity = db.Column(db.Float, nullable=False)
    citric_acid = db.Column(db.Float, nullable=False)
    residual_sugar = db.Column(db.Float, nullable=False)
    chlorides = db.Column(db.Float, nullable=False)
    free_sulfur_dioxide = db.Column(db.Float, nullable=False)
    total_sulfur_dioxide = db.Column(db.Float, nullable=False)
    density = db.Column(db.Float, nullable=False)
    pH = db.Column(db.Float, nullable=False)
    sulphates = db.Column(db.Float, nullable=False)
    alcohol = db.Column(db.Float, nullable=False)
    quality = db.Column(db.Integer, nullable=False)
