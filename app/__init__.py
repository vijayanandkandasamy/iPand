# Required Imports
from flask import Flask

# Initialize Flask Application
app = Flask(__name__)

from app import routes
