from flask import Flask

from api.access import access
from api.user import user


def init_app(app: Flask):
    app.register_blueprint(access)
    app.register_blueprint(user)
