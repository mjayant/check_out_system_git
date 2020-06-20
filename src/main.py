from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
_log = logging.getLogger(__name__)
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    db.init_app(app)
    # db.drop_all()
    with app.app_context():
        db.create_all()

    return app

# def main(host, port):
#     _log.info("Starting flask server")
#     application = create_app()
#     application.run(host=host, port=port, debug=True)
#     _log.info("Successfully started server")