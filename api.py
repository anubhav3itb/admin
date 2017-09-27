from flask import sessions, jsonify, Flask, render_template
import requests
import os
import ast


app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/intentreport.html')
def intentReport():
    data = requests.get('http://128.199.240.195:5000/getAllIntentReport').content
    data = ast.literal_eval(data)
    x = zip(data['user_name'], data['user_query'], data['user_intent'], data['reported_intent'], data['link'], data['approved'], data['message'])
    return render_template('intentreport.html',
                            title='Intent Reports',
                            x=x)



@app.route('/productreport.html')
def productReport():
    data = requests.get('http://128.199.240.195:5000/getAllProductReport').content
    data = ast.literal_eval(data)
    x = zip(data['user_name'], data['user_query'], data['reported_product'], data['link'], data['approved'], data['message'])
    return render_template('productreport.html',
                            title='Product Reports',
                            x=x)

@app.route('/analytics.html')
def analyticsReport():
	return render_template('analytics.html', title='Analytics')
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
