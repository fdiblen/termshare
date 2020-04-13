#!/usr/bin/python
from pathlib import Path

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
user_home = str(Path.home())

@app.route('/')
def content(histfile=user_home+'/.bash_history'):
    with open(histfile, "r") as f:
        content = f.readlines()

    return render_template('display.html', size=len(content), text=content)


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=80)
    socketio.run(app, debug=True, host='0.0.0.0', port=80)
