from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timeseries.db'
db = SQLAlchemy(app)
api = Api(app)
swagger = Swagger(app)

class TimeSeries(db.Model):
    date = db.Column(db.Date, primary_key=True)
    kwh = db.Column(db.Float)

class TimeSeriesResource(Resource):
    @swagger.doc({
        'tags': ['time-series'],
        'description': 'Get the time-series data',
        'responses': {
            '200': {
                'description': 'List of time-series data',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'date': {
                                'type': 'string',
                                'format': 'date',
                                'description': 'Date of the data point'
                            },
                            'kwh': {
                                'type': 'number',
                                'description': 'Consumption in kWh'
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        data = TimeSeries.query.all()
        result = [{'date': entry.date.strftime('%Y-%m-%d'), 'kwh': entry.kwh} for entry in data]
        return jsonify(result)

api.add_resource(TimeSeriesResource, '/api/time-series')

if __name__ == '__main__':
    app.run(debug=True)
