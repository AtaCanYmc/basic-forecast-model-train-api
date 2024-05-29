from config import db


class NullDataSolution(db.Model):
    __tablename__ = 'null_data_solutions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Null Data Solution: {self.name}>'