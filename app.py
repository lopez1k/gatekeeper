from flask import Flask, request, jsonify, redirect, render_template
import requests

app = Flask(__name__)

CHANNEL_LINK = "https://t.me/MyTokenCommunity"

def is_uk_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print(data)
        return data.get("countryCode") == "GB"
    except Exception as e:
        return False  # Якщо не вдалося визначити — допускаємо

@app.route("/")
def verify():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    print(ip)
    if is_uk_ip(ip):
        return render_template('index.html', user_ip = ip)
    else:
        return f"Your IP: {ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)