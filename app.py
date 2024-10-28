from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello DevOps!'

@app.route('/error')
def error():
    abort(500, 'Opps something went wrong')

# some comment for testing
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
