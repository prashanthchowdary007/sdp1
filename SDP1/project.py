from flask import *

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/signin')
def Registration():
    return render_template("signin.html")


if __name__ == "__main__":
    # app is a file name of the project
    app.run()
