import os
import json
import sys
import traceback
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7535602401:AAFQR-bWvtX2Im9xwwknWCx93iETzDSKulg")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "988359901")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


def format_alert_message(alert):
    """Форматирует сообщение алерта для Telegram"""
    status_obj = alert.get("status", {})
    if isinstance(status_obj, dict):
        status = status_obj.get("state", "unknown").upper()
    else:
        status = "FIRING"
    
    labels = alert.get("labels", {})
    annotations = alert.get("annotations", {})
    
    alertname = labels.get("alertname", "Unknown")
    severity = labels.get("severity", "unknown")
    summary = annotations.get("summary", "")
    description = annotations.get("description", "")
    
    message = f"*{status}*: {alertname}\n"
    message += f"*Severity*: {severity}\n"
    
    if summary:
        message += f"*Summary*: {summary}\n"
    if description:
        message += f"*Description*: {description}\n"
    
    return message


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        sys.stderr.write(f"Received data: {json.dumps(data, indent=2)}\n")
        sys.stderr.flush()
        
        if not data:
            sys.stderr.write("No data received\n")
            return jsonify({"error": "No data"}), 400
        
        alerts = data.get("alerts", [])
        
        if not alerts:
            sys.stderr.write("No alerts in data\n")
            return jsonify({"error": "No alerts"}), 400
        
        for alert in alerts:
            try:
                message = format_alert_message(alert)
                sys.stderr.write(f"Formatted message: {message}\n")
                sys.stderr.flush()
                
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "Markdown"
                }
                
                response = requests.post(TELEGRAM_API_URL, json=payload, timeout=10)
                sys.stderr.write(f"Telegram response: {response.status_code} - {response.text}\n")
                sys.stderr.flush()
                
                if response.status_code != 200:
                    sys.stderr.write(f"Error sending to Telegram: {response.status_code} - {response.text}\n")
                    sys.stderr.flush()
                    return jsonify({"error": "Failed to send to Telegram", "details": response.text}), 500
            except Exception as e:
                sys.stderr.write(f"Error processing alert: {e}\n")
                sys.stderr.write(traceback.format_exc())
                sys.stderr.flush()
                return jsonify({"error": str(e)}), 500
        
        return jsonify({"status": "ok"}), 200
        
    except Exception as e:
        sys.stderr.write(f"Error processing webhook: {e}\n")
        sys.stderr.write(traceback.format_exc())
        sys.stderr.flush()
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

