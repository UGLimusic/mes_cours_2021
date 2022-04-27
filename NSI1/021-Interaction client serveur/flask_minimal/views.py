from flask import Flask, render_template, request

# on importe Flask qui permet de créer le serveur
# render_template permet d'afficher des pages déjà crées
# en remplaçant chaque élément noté {{element}} par la valeur
# de la variable element correspondants


app = Flask(__name__)  # on crée le serveur


@app.route('/')  # on définit ce qui se passe à la connexion
def index():
    return render_template("index.html")


@app.route('/resultat', methods=['post'])  # que se passe-t-il pour resultat ?
# on traite un formulaire avec la méthode POST
def resultat():
    result = request.form  # on récupère les infos du formulaire
    # sous la forme d'un dictionnaire Python dont les clés
    # sont les noms des variables.
    valeur_nom = result['nom']
    return render_template("resultat.html", nom=valeur_nom)


app.run(debug=True)  # on démarre le serveur
