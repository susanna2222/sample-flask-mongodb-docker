#!./env/bin/python3
from flask import render_template, Flask, jsonify, make_response
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from app.api import request_api
from app.config import flask_env

if flask_env == 'production':
    config = 'config.production'
else:
    config = 'config.development'

app = Flask(__name__)
app.config.from_object(config)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.register_blueprint(request_api.get_blueprint())

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('index.html')

if __name__ == '__main__':    
    CORS = CORS(app)
    app.run(host='0.0.0.0', port='5000')