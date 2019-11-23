import sdnotify
from flask import Flask
from waitress import serve

notifier = sdnotify.SystemdNotifier()

app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello world!"

notifier.notify('READY=1')
notifier.notify('STATUS=Running')

if __name__ == "__main__":
  serve(app, host='0.0.0.0', port=5000)

