from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    today = date.today()
    d = "Today's date : " + str(today)
    return "Hello world!" + "<br><br>" + d

if __name__ == "__main__":
    app.run(host="0.0.0.0")