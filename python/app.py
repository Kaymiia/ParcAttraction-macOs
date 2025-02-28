from flask import Flask, jsonify, request
from flask_cors import CORS

import request.request as req
import controller.auth.auth as user
import controller.attraction as attraction
import controller.critique as critique

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

# Attraction
@app.post('/attraction')
def addAttraction():
    print("okok", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    retour = attraction.add_attraction(json)
    if (retour):
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500

@app.get('/attraction')
def getAllAttraction():
    result = attraction.get_all_attraction()
    return result, 200

@app.get('/attraction/<int:index>')
def getAttraction(index):
    result = attraction.get_attraction(index)
    return result, 200

@app.delete('/attraction/<int:index>')
def deleteAttraction(index):

    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    
    if (attraction.delete_attraction(index)):
        return "Element supprimé.", 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500

@app.post('/login')
def login():
    json = request.get_json()

    if (not 'name' in json or not 'password' in json):
        result = jsonify({'messages': ["Nom ou/et mot de passe incorrect"]})
        return result, 400
    
    cur, conn = req.get_db_connection()
    requete = f"SELECT * FROM users WHERE name = '{json['name']}' AND password = '{json['password']}';"
    cur.execute(requete)
    records = cur.fetchall()
    conn.close()

    result = jsonify({"token": user.encode_auth_token(list(records[0])[0]), "name": json['name']})
    return result, 200

@app.post('/critique')
def addCritique():
    checkToken = user.check_token(request)
    if checkToken != True:
        return checkToken

    data = request.get_json()

    # Validation des champs obligatoires
    if not all(k in data for k in ('crit', 'note', 'attraction_id')):
        return jsonify({"message": "Données incomplètes"}), 400
    if not (1 <= data['note'] <= 5):
        return jsonify({"message": "La note doit être entre 1 et 5."}), 400

    # Ajouter la critique
    result = critique.add_critique(data)
    if result:
        return jsonify({"message": "Critique ajoutée.", "result": result}), 200
    return jsonify({"message": "Erreur lors de l'ajout."}), 500

# Récupérer les critiques pour une attraction spécifique
@app.get('/critique/<int:attraction_id>')
def getCritiquesByAttraction(attraction_id):
    result = critique.get_critiques_by_attraction(attraction_id)
    return jsonify(result), 200

# Supprimer une critique spécifique
@app.delete('/critique/<int:critique_id>')
def deleteCritique(critique_id):
    checkToken = user.check_token(request)
    if checkToken != True:
        return checkToken

    if critique.delete_critique(critique_id):
        return jsonify({"message": "Critique supprimée."}), 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500