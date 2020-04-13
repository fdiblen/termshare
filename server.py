#!/usr/bin/python

import time
from pathlib import Path
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
user_home = str(Path.home())

@app.route('/')
def content(histfile=user_home+'/.bash_history'):
    with open(histfile, "r") as file_in:
        content = []
        time_stamp = ''
        for line in file_in:
            if line.startswith('#'):
                time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(line[1:])))
                continue
            content.append([time_stamp, line.strip()])
    return render_template('display.html', size=len(content), text=content)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=80)
