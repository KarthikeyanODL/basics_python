from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY             = "goldapi-724936db914b460708f7151fc7e8c925-io"
TROY_OUNCE_IN_GRAMS = 31.1035


def get_price(metal):
    url     = f"https://www.goldapi.io/api/{metal}/INR"
    headers = {"x-access-token": API_KEY}
    data    = requests.get(url, headers=headers).json()
    return data["price"]


def to_10gram(price_per_ounce):
    return round((price_per_ounce / TROY_OUNCE_IN_GRAMS) * 10, 2)


def to_kg(price_per_ounce):
    return round((price_per_ounce / TROY_OUNCE_IN_GRAMS) * 1000, 2)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/rates')
def rates():
    gold_per_ounce   = get_price("XAU")
    silver_per_ounce = get_price("XAG")

    metal_rates = {
        "gold_24k": to_10gram(gold_per_ounce),
        "gold_22k": round(to_10gram(gold_per_ounce) * 0.916, 2),
        "silver":   to_kg(silver_per_ounce)
    }

    print(f"Gold 24K : ₹{metal_rates['gold_24k']} per 10g")
    print(f"Gold 22K : ₹{metal_rates['gold_22k']} per 10g")
    print(f"Silver   : ₹{metal_rates['silver']} per kg")

    return render_template('rates.html', rates=metal_rates)


if __name__ == '__main__':
    app.run(debug=True)
