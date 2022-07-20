import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

from projects.content.views import content_tool

app.register_blueprint(content_tool)
