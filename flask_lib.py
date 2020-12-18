from flask import Flask, request, send_from_directory
import json

class FlaskLib:
	def __init__(self):
		self.app = Flask(__name__)
		self.name_counter = 0
		self.serve_directory()

	def run(self, port):
		self.app.run(port=port, debug=True)

	def api(self, route):
		def decorator(f):
			def g():
				url_args = dict(request.args)
				if 'json' in url_args:
					request_input = json.loads(url_args['json'])
				else:
					request_input = request.json or request_input
				return json.dumps(f(request_input))
			g.__name__ = "api_" + str(self.name_counter)
			self.name_counter += 1
			self.app.route(route, methods=['POST', 'GET'])(g)
		return decorator

	def serve_directory(self):
		@self.app.route('/<path:path>')
		def serve_files(path):
		    print("Path = ", path)
		    return send_from_directory('.', path)
