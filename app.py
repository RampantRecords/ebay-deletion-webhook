from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Rampant Records Webhook is live.'

@app.route('/ebay-deletion', methods=['POST'])
def ebay_deletion():
    data = request.get_json()
    print("📬 eBay Deletion Notice Received:")
    print(data)
    return '', 200
