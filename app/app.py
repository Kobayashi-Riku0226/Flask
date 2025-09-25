from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"

@app.route("/stdout")
def stdout_log():
        # stdoutにログを出力
        print("test access", file=sys.stdout, flush=True)
        return "<p>Logged to stdout</p>"

@app.route("/stderr")
def stderr_log():
        # stderrにログを出力
        print("test err access", file=sys.stderr, flush=True)
        return "<p>Logged to stderr</p>"

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)