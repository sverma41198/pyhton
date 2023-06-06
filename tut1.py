from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sourabh")
def hello_world_2():
    return "<p>Hello, World,i Am Sourabh!</p>"
app.run()