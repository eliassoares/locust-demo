from flask import Blueprint

access = Blueprint('access', __name__)

from . import views
