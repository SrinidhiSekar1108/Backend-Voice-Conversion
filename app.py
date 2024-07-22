from flask import Flask, request, render_template
from recognizer import recognize_speech_from_mic
from tts import text_to_speech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    text = recognize_speech_from_mic()
    print(f"You said: {text}")
    text_to_speech(text)
    return text

@app.route('/submit-text', methods=['POST'])
def submit_text():
    response_text = request.form['text']
    print(f"User typed: {response_text}")
    text_to_speech(response_text)
    return 'Text submitted and spoken.'

if __name__ == '__main__':
    app.run(debug=True)
