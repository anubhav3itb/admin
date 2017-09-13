from flask import sessions, jsonify, Flask, render_template
import requests
import os
import ast


app = Flask(__name__)


@app.route('/')
def index():
    data = requests.get('http://128.199.240.195:5000/getAllIntentReport').content
    data = ast.literal_eval(data)
    x = zip(data['user_name'], data['user_query'], data['user_intent'], data['reported_intent'], data['link'], data['approved'], data['message'])
    return render_template('index.html',
                            title='Intent Reports',
                            x=x)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)