from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo"

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    msg = request.form.get('Body')

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Você é um assistente debochado e espirituoso."},
            {"role": "user", "content": msg}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=body, headers=headers)
        data = response.json()

        reply = data['choices'][0]['message']['content']
    except Exception as e:
        reply = f"Erro ao falar com o OpenRouter: {str(e)}"

    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
