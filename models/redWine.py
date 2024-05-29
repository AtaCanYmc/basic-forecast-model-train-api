import pandas as pd
from sqlalchemy.orm import sessionmaker

from config import db


class RedWine(db.Model):
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


def get_red_wine_data_as_dataframe(row_limit):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    red_wine_data = session.query(RedWine).limit(row_limit).all()
    data = []

    for row in red_wine_data:
        data.append({
            'id': row.id,
            'fixed_acidity': row.fixed_acidity,
            'volatile_acidity': row.volatile_acidity,
            'citric_acid': row.citric_acid,
            'residual_sugar': row.residual_sugar,
            'chlorides': row.chlorides,
            'free_sulfur_dioxide': row.free_sulfur_dioxide,
            'total_sulfur_dioxide': row.total_sulfur_dioxide,
            'density': row.density,
            'pH': row.pH,
            'sulphates': row.sulphates,
            'alcohol': row.alcohol,
            'quality': row.quality
        })

    df = pd.DataFrame(data)
    session.close()
    return df
