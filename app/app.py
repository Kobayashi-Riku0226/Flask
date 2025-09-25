from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
        app.logger.info('default access')
        return "<p>Hello, World!</p>"

@app.route("/stdout")
def stdout_log():
        # stdoutにログを出力
        app.logger.info('test stdout access')
        return "<p>Logged to stdout</p>"

@app.route("/stderr")
def stderr_log():
        # stderrにログを出力
        app.logger.error('test stderr access')
        return "<p>Logged to stderr</p>"

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)