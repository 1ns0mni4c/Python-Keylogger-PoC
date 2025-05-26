from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def log():
	key = request.data

	with open("log.txt", "ab") as f:
		f.write(key)

	return "", 200

app.run("0.0.0.0")