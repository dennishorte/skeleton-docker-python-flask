
from os import environ

from flask import Flask
from flask_login import LoginManager
from flask_login import current_user
from flask_login import login_required
from user import User


app = Flask(__name__)
app.secret_key = environ.get('FLASK_SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'


@app.route("/")
@login_required
def root():
    return "Hello, {}!".format(current_user)


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
