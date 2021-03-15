from flask import Flask, jsonify, request
import main.Repositories.interventionRepository as interventionController
import main.Repositories.technicienRepository as technicienController
from main.DataBase.manageDatabase import create_databse
from main.Models.intervention import Intervention

app = Flask(__name__)


@app.before_first_request
def create_database():
    create_databse()


# ---------------------- Partie Intervention ----------------------------

@app.route('/interventions', methods=["GET"])
def get_interventions():
    interventions = interventionController.get_interventions()
    return jsonify(interventions)


@app.route('/intervention/<int:idInter>', methods=["GET"])
def get_intervention_by_id(idInter):
    intervention = interventionController.get_by_id(idInter)
    return jsonify(intervention)


@app.route('/intervention/add', methods=['POST', 'GET'])
def add_intervention():
    idTech = request.args.get('idTech')
    idClient = request.args.get('idClient')
    piece = request.args.get('piece')
    probleme = request.args.get('probleme')

    if not idTech:
        return "L'id du technicien n'est pas renseigné"
    if not idClient:
        return "L'id du client n'est pas renseigné"
    if not piece:
        return "La piéce n'est pas renseignée"
    if not probleme:
        return "Le problème n'est pas renseigné"

    intervention = Intervention(idTech, idClient, piece, probleme)

    if interventionController.add_intervention(intervention) == 1:
        return "Intervention Créer"
    else:
        return "Erreur lors de la création de l'intervention"


# ---------------------- Partie Technicien ----------------------------


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
    app.run()
