# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import config
#
# db = SQLAlchemy()
#
#
# def create_app():
#     """Construct the core application."""
#     app = Flask(__name__, instance_relative_config=False)
#     app.config.from_object('config.DevConfig')
#
#     db.init_app(app)
#     # db.drop_all()
#     with app.app_context():
#         db.create_all()
#
#     return app