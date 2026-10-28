from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json()

    if not data or "numbers" not in data:
        return jsonify({"error": "Please provide a numbers list."}), 400

    numbers = data["numbers"]

    if not isinstance(numbers, list):
        return jsonify({"error": "Numbers must be a list."}), 400

    try:
        total = sum(numbers)
        return jsonify({"sum": total})
    except TypeError:
        return jsonify({"error": "All items must be numbers."}), 400


if __name__ == "__main__":
    app.run(port=5000)