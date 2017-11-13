from flask import Flask
from application.database import db_session
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import application.views