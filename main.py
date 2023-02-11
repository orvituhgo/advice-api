from flask import Flask, jsonify, render_template, url_for
import requests


requisition = requests.get("https://api.adviceslip.com/advice")
advice_json = requisition.json()
advice_showed = advice_json['slip']['advice']
advice_id = advice_json['slip']['id']

app = Flask(__name__)


@app.route("/")
def advice():
    return render_template("index.html", advice_showed=advice_showed,
                           advice_id=advice_id)


# with app.test_request_context():
#     print(url_for('advice/id=', id=advice_id))

if __name__ == "__main__":
    app.run(debug=True)
