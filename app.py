from flask import Flask
from config import Config
from config import db
from routes import redWineRoute, predictionModelRoute, nullDataSolutionRoute, trainDataRoute, validationRoute

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(redWineRoute.red_wines, url_prefix='/api/v1')
app.register_blueprint(predictionModelRoute.prediction_models, url_prefix='/api/v1')
app.register_blueprint(nullDataSolutionRoute.null_data_solutions, url_prefix='/api/v1')
app.register_blueprint(trainDataRoute.train_data_blueprint, url_prefix='/api/v1')
app.register_blueprint(validationRoute.validation_blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()
