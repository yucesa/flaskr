import os
from flask import Flask

def create_app(test_config=None):
    # create and confiure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRECT_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)

    else:
        # load the instance_config from py file
        app.config.from_mapping(test_config)


    #ensure instance folder is exists
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    #a simple page to say hi
    @app.route('/hello')
    def hello():
        return 'Hello'

    @app.route('/test')
    def test():
        return app.config['DATABASE']

    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app