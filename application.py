from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from app.extensions import db
from app.routes import register_routes
from manage import add_command

app = Flask(__name__)
migrate = Migrate()
app.config.from_object('config.ProductionConfig')


api = Api(app=app, version="v1.0.1", title="Driving School Management API",
          description="This is th API collection of the driving school management system")

register_routes(api)
db.init_app(app)
migrate.init_app(app, db)

add_command(app)
app.app_context().push()
if __name__ == "__main__":
    app.run(debug=True)
