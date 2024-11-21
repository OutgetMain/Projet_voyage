from random import randint
import time
import extract
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
cur = extract.conn.cursor()

@app.route("/Accueil", methods=["GET", "POST"])
def accueil():
    if request.method == "POST":
        if "connexion" in request.form:
            return render_template("Accueil.html", show_form=True, form_type="connexion")
        elif "inscription" in request.form:
            return render_template("Accueil.html", show_form=True, form_type="inscription")
    return render_template("Accueil.html", show_form=False)

@app.route("/page_recherche")
def liste_voyage():
    cur.execute("SELECT * FROM voyage")
    voyage = cur.fetchall()
    print(type(voyage[1][2]))
    return render_template("page_recherche.html",voyage=voyage)



if __name__ == '__main__':
    app.run(debug=True)
