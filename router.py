from flask import Flask
from flask.templating import render_template
import atmos_dao as ad

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", weather=ad.select())  

if __name__ == "__main__":
    app.run(debug=True)