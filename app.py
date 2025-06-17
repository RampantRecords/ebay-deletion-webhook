from flask import Flask, request

app = Flask(__name__)

# EXACT 32-char token
VERIFICATION_TOKEN = "RampantWebhookTokenABC123456789012"

@app.route('/')
def home():
    return '✅ Rampant Records Webhook is live.'

@app.route('/ebay-deletion', methods=['POST'])
def ebay_deletion():
    # eBay verification challenge
    if request.args.get("challengeCode"):
        challenge = request.args.get("challengeCode")
        print(f"🔐 Responding to eBay challenge: {challenge}")
        return challenge, 200

    # Handle real deletion events
    data = request.get_json()
    print("📬 eBay Deletion Notice Received:")
    print(data)
    return '', 200
