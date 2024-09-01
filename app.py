from flask import Flask, request, render_template, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    sender_id = request.form['sender_id']
    
    # Save the message to a CSV file
    with open('messages.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([sender_id, message])
    
    return jsonify({'status': 'Message received!'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages = []
    if os.path.exists('messages.csv'):
        with open('messages.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            messages = list(reader)
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
