from flask import Flask
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    try:
        nifty = yf.Ticker("^NSEI")
        data = nifty.history(period="1d", interval="1m")
        price = round(data['Close'].iloc[-1], 2)
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return f"""
        <h1>NIFTY 50 LIVE - {price}</h1>
        <p>Time: {time}</p>
        <p>Status: ALGO RUNNING ON RENDER</p>
        <p>Updated every minute</p>
        <script>setTimeout(()=>location.reload(), 60000)</script>
        """
    except Exception as e:
        return f"<h1>NIFTY ALGO LIVE</h1><p>Error: {e}</p><p>Retrying...</p><script>setTimeout(()=>location.reload(), 10000)</script>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
