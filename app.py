from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Rampant Records Webhook is live.'

@app.route('/ebay-deletion', methods=['POST'])
def ebay_deletion():
    # This handles the initial eBay verification challenge
    if 'challengeCode' in request.args:
        challenge = request.args.get('challengeCode')
        print(f"🔐 Responding to eBay challenge: {challenge}")
        return challenge, 200

    # This handles actual deletion events
    data = request.get_json()
    print("📬 eBay Deletion Notice Received:")
    print(data)
    return '', 200
