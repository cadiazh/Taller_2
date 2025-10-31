import random, socket, copy
from flask import Blueprint, jsonify, render_template
from .models import POKENEAS

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/pokenea-json")
def pokenea_json():
    p = copy.deepcopy(random.choice(POKENEAS))
    p["container_id"] = socket.gethostname()
    return jsonify({
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": p["container_id"],
    })

@app_routes.route("/pokenea-imagen")
def pokenea_imagen():
    p = random.choice(POKENEAS)
    container_id = socket.gethostname()
    return render_template("pokenea.html", pokenea=p, container_id=container_id)
