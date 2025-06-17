from flask import Flask, request

app = Flask(__name__)  # ✅ This is the missing piece

@app.route('/')
def home():
    return '✅ Rampant Records Webhook is live.'

@app.route('/ebay-deletion', methods=['POST'])
def ebay_deletion():
    # ✅ Handle both challengeCode and challenge_code (eBay sends different formats)
    challenge = request.args.get("challengeCode") or request.args.get("challenge_code")
    if challenge:
        print(f"🔐 Respo
