"""Flask web app exposing an emotion detection endpoint."""
from flask import Flask, jsonify, request

from .detector import WatsonEmotionDetector

app = Flask(__name__)
_detector = WatsonEmotionDetector()


@app.route("/emotion", methods=["POST"])
def emotion():
    """Return detected emotion for posted JSON text."""
    data = request.get_json(silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400
    try:
        result = _detector.detect(data["text"])
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
