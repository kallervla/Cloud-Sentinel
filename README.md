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

## 🐍 Local Run (without Docker)

```bash
pip install -r requirements.txt
python src/main.py

src/
├── main.py       # AWS monitoring logic
├── logger.py     # Logging setup
├── alerts.py     # Alert logic
├── web.py        # (optional) Flask web app
