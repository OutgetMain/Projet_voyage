from random import randint
import time
import extract
from flask import Flask, render_template, request, redirect, url_for, session
#source venv/bin/activate

app = Flask(__name__)
cur = extract.conn.cursor()

@app.route("/Accueil", methods=["GET", "POST"])
def accueil():
    if request.method == "POST":
        if "connexion" in request.form:
            return render_template("Accueil.html", show_form=True, form_type="connexion")
        elif "inscription" in request.form:
            return render_template("Accueil.html", show_form=True, form_type="inscription")
        
        if "validation_connexion" in request.form :
            username = request.form.get("username")
            password = request.form.get("password")
            cur.execute("SELECT courriel,mdp FROM client;")
            liste_client = cur.fetchall()
            if (username,password) in liste_client:
                return render_template("Accueil.html",show_form=True,form_type = "connexion_succes",liste_client=liste_client)
            return render_template("Accueil.html",show_form=True,form_type = "connexion_fail",liste_client=liste_client)
        
        if "validation_inscription" in request.form :
            Nom = request.form.get("nom")
            Prenom = request.form.get("prenom")
            Sexe = request.form.get("sexe")
            Age = request.form.get("age")
            Nationalite = request.form.get("nationalite")
            Adresse = request.form.get("adresse")
            Tel= request.form.get("telephone")
            Mail= request.form.get("mail")
            password = request.form.get("password")
            
            insert_query = """
                INSERT INTO client(nom, prenom, sexe, courriel, tel, adresse,mdp,age,nationalite)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cur.execute(insert_query, (Nom, Prenom, Sexe, Mail, Tel, Adresse, password,Age,Nationalite))
            extract.conn.commit()
            return render_template("Accueil.html",show_form=True, form_type = "inscription_reussie")
            
    return render_template("Accueil.html", show_form=False)

@app.route("/page_recherche")
def liste_voyage():
    cur.execute("SELECT id_ville,date_depart,date_arrivée FROM Etape;")
    information = cur.fetchall()
    

    if list_id_ville:
        query = "SELECT nom FROM Ville WHERE id_ville = %s;"
        cur.execute(query, (tuple(information[0]),))
        #ajouter les horaire a faire
        liste_voyage = [row[0] for row in cur.fetchall()]
    else:
        liste_voyage = []
    return render_template("page_recherche.html",liste_voyage = liste_voyage)



if __name__ == '__main__':
    app.run(debug=True)
