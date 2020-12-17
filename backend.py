from flask import Flask, request, send_from_directory
app = Flask(__name__)

import json

@app.route('/bhens_sum_of_sonu')
def sonu_ka_nam():
    return 'Mera Nam Sonu Hai'

@app.route('/padi_sum_of_sonu')
def padi_sonu_ka_nam():
    return 'Mera Nam Sonu Hai'


@app.route('/api/sum2', methods=['POST'])
def sum2():
    print(request.json)
    print(request.data)
    return json.dumps(request.json['x'] + request.json['y'])


@app.route('/<path:path>')
def files(path):
    print("Path = ", path)
    return send_from_directory('.', path)

app.run(port=5502, debug=True)


# curl -i -H "Content-Type: application/json" -X POST -d '{"A": 22}' http://127.0.0.1:5502/sum2
