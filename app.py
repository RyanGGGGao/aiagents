from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Webhook is running!"

@app.route("/telnyx-inbound", methods=["POST"])
def handle_webhook():
    data = request.json
    print("Received Telnyx Event:")
    print(data)

    # 可选：做事件分类
    event_type = data.get("data", {}).get("event_type")
    if event_type == "call.initiated":
        print("📞 Incoming call")
    elif event_type == "call.answered":
        print("✅ Call answered")
    elif event_type == "call.hangup":
        print("❌ Call ended or missed")

    return jsonify({"status": "received"})
