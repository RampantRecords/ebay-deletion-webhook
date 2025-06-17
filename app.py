@app.route('/ebay-deletion', methods=['POST'])
def ebay_deletion():
    # Handle challenge with either casing
    challenge = request.args.get("challengeCode") or request.args.get("challenge_code")
    if challenge:
        print(f"🔐 Responding to eBay challenge: {challenge}")
        return challenge, 200

    # Handle actual deletion payloads
    data = request.get_json()
    print("📬 eBay Deletion Notice Received:")
    print(data)
    return '', 200
