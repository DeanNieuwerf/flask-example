from flask import Flask, render_template, request, jsonify

application = Flask(__name__)

# Store chat messages in a list
chat_messages = []

@application.route('/')
def home():
    return render_template('index.html', chat_messages=chat_messages)

@application.route('/send', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message:
        chat_messages.append(message)
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    application.run(debug=True)