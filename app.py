from flask import Flask, request, jsonify, render_template
from weather import get_weather_by_city

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        cidade = request.form.get("cidade")
        resultado = get_weather_by_city(cidade)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
