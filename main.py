from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name', 'world')
    name = input("What is your name? ")
    message = f"Hello, {name}!"
    return message


if __name__ == '__main__':
    app.run(port(5500), debug=True)
