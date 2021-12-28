from flask import Flask
from models import db
from views import user_view
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(user_view.bp)
CORS(app)

db.init_app(app)

if __name__ == '__main__':
  app.run(port=8000, debug=True)