from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Rampant Records Webhook is live.'

@app.route('/ebay-deletion', methods=['POST'])
def ebay_deletion():
    # Respond to eBay's verification challenge
    challenge = request.args.get("challengeCode") or request.args.get("challenge_code")
    if challenge:
        print(f"🔐 Responding to eBay challenge: {challenge}")
        return challenge, 200

    # Handle actual deletion notifications
    data = request.get_json()
    print("📬 eBay Deletion Notice Received:")
    print(data)
    return '', 200
