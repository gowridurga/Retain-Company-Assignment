from flask import Flask
from routes.create_user import create_user_bp
from routes.delete_user import delete_user_bp
from routes.update_user import update_user_bp
from routes.login import login_bp
from routes.user_api import user_bp
from routes.get_user import get_user_bp

app = Flask(__name__)

# Health check route
@app.route("/")
def home():
    return "✅ Flask app is running!"

# Register Blueprints
app.register_blueprint(create_user_bp, url_prefix="/users")
app.register_blueprint(delete_user_bp, url_prefix="/users")
app.register_blueprint(update_user_bp, url_prefix="/users")
app.register_blueprint(login_bp, url_prefix="/users")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(get_user_bp, url_prefix="/users")

if __name__ == '__main__':
    print("🚀 Starting Flask App on http://localhost:5009")
    app.run(host='0.0.0.0', port=5009, debug=True)
