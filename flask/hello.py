from flask import Flask, redirect, url_for, render_template
import requests

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route("/")
def hello_world():
    return 'Hello, World'

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello {} as Guest" .format(guest)

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest = name))
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/respon')
def respon():
    return render_template('respon.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
