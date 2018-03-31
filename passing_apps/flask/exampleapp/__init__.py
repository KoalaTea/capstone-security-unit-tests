from flask import Flask
from flask_talisman import Talisman

def create_app(**config_overrides):
    csp = {
        'default-src': '\'self\''
    }
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    from exampleapp.views import views as views_blueprint
    app.register_blueprint(views_blueprint)
    app.config.update(config_overrides)
    Talisman(app, content_security_policy=csp)

    @app.after_request
    def apply_caching(response):
        response.headers["X-Permitted-Cross-Domain-Policies"] = "master-only"
        response.headers["Expected-CT"] = "enforce"
        return response

    return app
