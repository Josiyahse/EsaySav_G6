from flask import Flask, jsonify
import Repositories.interventionRepository as interventionController
from DataBase.manageDatabase import create_databse

app = Flask(__name__)


@app.route('/interventions', methods=["GET"])
def get_interventions():
    return jsonify(interventionController.get_interventions())


@app.route('/intervention/<int:idInter>', methods=["GET"])
def get_intervention_by_id(idInter):
    intervention = interventionController.get_by_id(idInter)
    return jsonify(intervention)


if __name__ == '__main__':
    create_databse()
    app.run()
