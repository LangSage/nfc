# NFC Points App

A simple Flask + Web NFC application to track points on NFC tags.

## Features
- Register NFC tags as "allowed"
- Add or subtract 5 points per tag
- Plays a fun beep on each point change
- Responsive, modern design with CSS

## Quick Start
```bash
# Clone the repo
git clone https://github.com/yourusername/nfc-points-app.git
cd nfc-points-app

# Install dependencies
pip install -r requirements.txt

# Run the server
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```

Open `http://<your-ip>:5000` in Chrome on Android, tap your NFC tag to register or modify points.
