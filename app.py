from flask import Flask, render_template, request, jsonify

from mathutils import add, subtract, multiply

app = Flask(__name__)

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calculate", methods=["POST"])
def calculate():
    data = request.get_json(force=True)
    operation = data.get("operation")
    if operation not in OPERATIONS:
        return jsonify({"error": f"Unknown operation: {operation}"}), 400

    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
    except (TypeError, ValueError):
        return jsonify({"error": "a and b must be numbers"}), 400

    result = OPERATIONS[operation](a, b)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
