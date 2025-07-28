from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/telnyx-inbound', methods=['POST'])
def webhook():
    data = request.json
    print("Received:", data)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run()
