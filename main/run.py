from flask import Flask, jsonify, request
import main.Repositories.interventionRepository as interventionController
import main.Repositories.technicienRepository as technicienController
from main.DataBase.manageDatabase import create_databse, get_db
from main.Models.intervention import Intervention

app = Flask(__name__)


@app.before_first_request
def create_database():
    get_db()
    create_databse()


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


@app.route('/intervention/add', methods=['POST','GET'])
def add_intervention():
    idTech = request.args.get('idTech', int)
    idClient = request.args.get('idClient', int)
    piece = request.args.get('piece', str)
    probleme = request.args.get('probleme', str)

    intervention = Intervention(idTech, idClient, piece, probleme)

    if interventionController.add_intervention(intervention) == 1:
        return "OK"
    else:
        return "Probleme avec la base de donnees"


if __name__ == '__main__':
    app.debug = True
    app.run()
