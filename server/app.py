from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
app =Flask(__name__)

# mpesa details
consumer_key='bHGaxRG5tOFHLdeGhuZiTGphNMmxPfqL'
consumer_secret='Ze8CbLSJ80aP7dz6'

@app.route('/')
def home():
    return "Hello World!"

# access token
@app.route('/access_token')
def token():
    data= ac_token
    return data


def ac_token(){
    mpesa_auth_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    data =(requests.get(mpesa_auth_url, HTTPBasicAuth(consumer_key, consumer_secret))).json()
    return data['access_token']
}
if __name__=="__main__":
    app.run(port=555, debug=True)