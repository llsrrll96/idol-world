from flask import Flask
from extensions import db

from routes.root_world_routes import world_bp, comment_bp
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(world_bp, url_prefix='/way')
app.register_blueprint(comment_bp, url_prefix='/comment')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=9000, debug=True)