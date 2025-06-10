<!-- CI trigger -->

# Cloud Sentinel

Cloud Sentinel is a Python-based lightweight tool designed to monitor AWS infrastructure, detect misconfigurations, and alert on suspicious activity in real-time.

## 🚀 Features

- ✅ Continuous AWS resource monitoring (EC2, S3, IAM, etc.)
- 📄 Logging of all detected events
- 🔔 Real-time alerting via email/Slack
- 🌐 Optional lightweight web interface (Flask/FastAPI)
- 🐳 Dockerized for easy deployment

## 🛠️ Tech Stack

- Python 3.x
- Boto3 (AWS SDK)
- Flask (optional Web UI)
- Docker, Docker Compose

## 🐳 Getting Started (Docker)

```bash
git clone https://github.com/yourusername/cloud-sentinel.git
cd cloud-sentinel
docker-compose up --build
```

## 🐍 Local Run (without Docker)

```bash
pip install -r requirements.txt
python src/main.py
```

## 📁 Directory Structure

```bash
src/
├── main.py       # AWS monitoring logic
├── logger.py     # Logging setup
├── alerts.py     # Alert logic
├── web.py        # (optional) Flask web app
```

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
Trigger CI manually

## Watson NLP Emotion Detection Web App

This repository also contains a simple emotion detection service built with Flask.
It uses IBM Watson Natural Language Understanding to analyze text and return the
detected emotion in JSON format. A fallback heuristic is provided when Watson
credentials are not configured.

Run locally:

```bash
pip install -r requirements.txt
python -m emotion_detection.webapp
```

Send a request:

```bash
curl -X POST -H 'Content-Type: application/json' \
    -d '{"text": "I am very happy"}' http://localhost:5000/emotion
```
