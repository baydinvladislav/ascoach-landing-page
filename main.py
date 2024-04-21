from flask import Flask, render_template


application = Flask(__name__)


@application.route("/")
def get_root_page():
   return render_template('index.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0')
