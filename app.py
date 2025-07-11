from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# In-memory stores
balances = {}
allowed_tags = set()

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/api/enroll', methods=['POST'])
def enroll():
    data = request.get_json() or {}
    tagId = data.get('tagId')
    if not tagId:
        return jsonify(error='Missing tagId'), 400
    allowed_tags.add(tagId)
    balances.setdefault(tagId, 0)
    return '', 204

@app.route('/api/balance/<tagId>', methods=['GET'])
def get_balance(tagId):
    if tagId not in allowed_tags:
        return jsonify(error='Tag not enrolled'), 403
    return jsonify(points=balances.get(tagId, 0))

@app.route('/api/update', methods=['POST'])
def update():
    data = request.get_json() or {}
    tagId = data.get('tagId')
    delta = data.get('delta', 0)
    if tagId not in allowed_tags:
        return jsonify(error='Tag not enrolled'), 403
    try:
        delta = int(delta)
    except ValueError:
        return jsonify(error='Invalid delta'), 400
    balances[tagId] = balances.get(tagId, 0) + delta
    return jsonify(points=balances[tagId])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
