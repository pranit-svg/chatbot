from flask import Flask, request, jsonify
from flask_cors import CORS
import cohere

# Replace with your API key
API_KEY = "3KQbrqcqXPDAeUyPvVEpqnHUiis7eiyR39X8W5UX"
co = cohere.Client(API_KEY)

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = co.chat(message=prompt, model="command-r-plus")
    return jsonify({"reply": response.text})

if __name__ == '__main__':
    app.run(debug=True)
