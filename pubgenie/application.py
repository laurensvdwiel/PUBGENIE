from flask import Flask
from pubgenie.presentation.web.routes import bp

app = Flask(__name__, static_folder='presentation/web/static', static_url_path='/pubgenie/static',
               template_folder='presentation/web/templates')
app.register_blueprint(bp)
