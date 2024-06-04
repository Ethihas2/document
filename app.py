from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'AC820ba02af52eb628f008b80d602051e3'
    TWILIO_SYNC_SERVICE_SID = 'ISc22a6c5c23a7929dc5aa5dc543426c59'
    TWILIO_API_KEY = 'SK900b41c5b99a720060da04dd90b0b56c'
    TWILIO_API_SECRET = 'W9AfTLtwa1VQqIXIcnHrpcC247rbc92j'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

