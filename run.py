from flask import Flask, jsonify
import Repositories.interventionRepository as interventionController
import Repositories.technicienRepository as technicienController
from DataBase.manageDatabase import create_databse

app = Flask(__name__)


@app.route('/interventions', methods=["GET"])
def get_interventions():
    interventions = interventionController.get_interventions()
    return jsonify(interventions)


@app.route('/intervention/<int:idInter>', methods=["GET"])
def get_intervention_by_id(idInter):
    intervention = interventionController.get_by_id(idInter)
    return jsonify(intervention)


@app.route('/techniciens', methods=["GET"])
def get_techiciens():
    techniciens = technicienController.get_techniciens()
    return jsonify(techniciens)


@app.route('/technicien/<int:idTech>', methods=["GET"])
def get_techicien_by_id(idTech):
    technicien = technicienController.get_by_id(idTech)
    return jsonify(technicien)


if __name__ == '__main__':
    app.debug = True
    create_databse()
    app.run()
