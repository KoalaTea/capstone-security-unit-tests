from flask import Flask
def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    from exampleapp.views import views as views_blueprint
    app.register_blueprint(views_blueprint)
    app.config.update(config_overrides)
    return app

