from flask import Flask

from myapi.routes import api
from mysite.routes import site



def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)

    return app

app = create_app()

app.run()
