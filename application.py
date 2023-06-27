from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from app.routes import register_routes
from manage import add_command

app = Flask(__name__)

app.config.from_object('config.ProductionConfig')

db = SQLAlchemy(app)

api = Api(version="1.0", title="Driving School Management API",
          description="This is th API collection of the driving school management system")


api.init_app(app)
register_routes(api)

add_command(app)


if __name__ == "__main__":
    app.run(debug=True)
