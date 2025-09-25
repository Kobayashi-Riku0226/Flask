from flask import Flask
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route("/")
def hello_world():
        app.logger.info('default access')
        return "<p>Hello, World!</p>", 200

@app.route("/info")
def stdout_log():
        app.logger.info('test info access')
        return "<p>Logged to info</p>", 200

@app.route("/err")
def stderr_log():
        app.logger.error('test err access')
        return "<p>Logged to err</p>", 500

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)