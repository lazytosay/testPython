from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is the index"

@app.route('/about')
def about():
    return "This is the about page."

if __name__ == "__main__":
    app.run()
