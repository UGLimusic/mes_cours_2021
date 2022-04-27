from flask import Flask, render_template, request

# on importe Flask qui permet de créer le serveur
# render_template permet d'afficher des pages déjà crées
# en remplaçant chaque élément noté {{element}} par la valeur
# de la variable element correspondants


app = Flask(__name__)  # on crée le serveur


@app.route('/')  # on définit ce qui se passe à la connexion
def index():  # on peut donner le nom que l'on veut à la fonction
    return render_template("index.html")


@app.route('/resultat', methods=['post'])  # que se passe-t-il pour resultat ?
# on traite un formulaire avec la méthode POST
def resultat():  # on peut donner le nom que l'on veut à la fonction

    result = request.form  # on récupère les infos du formulaire
    # sous la forme d'un dictionnaire Python dont les clés
    # sont les noms des variables.

    user_name = result['username']  # voilà comment on récupère le username fourni dans le formulaire



    annee_naissance = int(result['dateNaissance'][:4])  # on ne garde que l'année de naissance, on convertit en int

    age = 2020 - annee_naissance  # voici donc UNE LIGNE de traitement des données

    if age < 18: # et son issue
        return render_template("mineur.html", nom=user_name, age_actuel=age)
    else:
        return render_template("majeur.html", nom=user_name, age_actuel=age)


app.run(debug=True)  # on démarre le serveur
