from flask import Flask, render_template, jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify(message="Hello, Flask!")

@app.route('/index')
def index():
   return jsonify(message="Hello, From Index!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
