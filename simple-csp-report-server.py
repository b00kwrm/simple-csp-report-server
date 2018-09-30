from flask import Flask, jsonify
app = Flask(__name__)

root_message = {'greeting': 'hello, world'}

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(root_message)

if __name__ == '__main__':
    app.run()
