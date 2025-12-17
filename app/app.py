from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Charger data JSON (ajoute plus d'infos si besoin)
with open('static/data/gabon_data.json', 'r') as f:
    gabon_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/province/<province>')
def get_province_info(province):
    return jsonify(gabon_data.get(province, {}))

@app.route('/api/park/<park>')
def get_park_info(park):
    # Simule un parcours biodiversité avec data
    park_data = gabon_data['parks'].get(park, {})
    return jsonify(park_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)