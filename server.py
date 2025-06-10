"""Entry point for running the emotion detection web server."""
from emotion_detection.webapp import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
