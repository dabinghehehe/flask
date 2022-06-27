import webbrowser
from flask import Flask, redirect, render_template

app = Flask(__name__, static_url_path='/',
            static_folder='static', template_folder='templates')


@ app.route("/")
def direct_show():
    return render_template("post-1.html")


if __name__ == "__main__":
    app.run(debug=True)
