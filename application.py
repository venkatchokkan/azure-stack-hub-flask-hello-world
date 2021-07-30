from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello this is my second web service bt prabha"

if __name__ == '__main__':
    app.run()
