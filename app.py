from flask import Flask
import yfinance as yf
import os

app = Flask(__name__)

def get_price():
    try:
        data = yf.Ticker("^NSEI").history(period="1d")
        if data.empty:
            return "Market Closed - Last Price: 24800"
        return round(float(data['Close'].iloc[-1]), 2)
    except Exception as e:
        return f"Loading... {e}"

@app.route("/")
def home():
    price = get_price()
    return f"""
    <html>
    <head><title>NIFTY ALGO LIVE</title></head>
    <body style="font-family:Arial; text-align:center; margin-top:100px; background:black; color:white;">
        <h1>NIFTY ALGO LIVE</h1>
        <h2 style="color:lime; font-size:50px;">{price}</h2>
        <p>Your Algo is LIVE on Render!</p>
        <p>Auto refresh in 5 sec</p>
        <script>setTimeout(()=>location.reload(),5000)</script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
