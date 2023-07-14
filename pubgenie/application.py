from flask import Flask
from pubgenie.presentation.web.routes import bp

app = Flask(__name__)
app.register_blueprint(bp)
