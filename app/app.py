from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto
app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    result = RejestrKont.findKonto(dane["pesel"])
    if(result != "There is no such an account"):
        return jsonify(error="There is already account with such a pesel"),400
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.addKonto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print(f"Request o liczbe kont")
    count = RejestrKont.kontoCount()
    return jsonify(accounts_count=count), 201


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.findKonto(pesel)
    if(type(konto) != str):
        return jsonify(imie=konto.imie), 200
    else: 
        return jsonify(error=konto), 401

@app.route("/konta/usun_konto/<pesel>", methods=["DELETE"])
def usun_konto(pesel):
    print(pesel)
    result = RejestrKont.kontoDelete(pesel)
    if(result == None):
        return jsonify(error="There is no such account"), 404
    else: 
        return jsonify("Konto usunięte"), 204

@app.route("/konta/konto/zmien_konto/<pesel>", methods=["POST"])
def zmien_konto(pesel):
    dane = request.get_json()
    result = RejestrKont.kontoUpdate(pesel,dane["imie"],dane["nazwisko"])
    if(result == None):
        return jsonify(error="There is no such an account"), 404
    else:
        return jsonify(imie=result.imie, nazwisko=result.nazwisko, saldo=result.saldo), 201