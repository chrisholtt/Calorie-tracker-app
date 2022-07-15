from flask import Flask, render_template
from controllers.users_controller import users_blueprint
from controllers.days_controller import days_blueprint
app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(days_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
