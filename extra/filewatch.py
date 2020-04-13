
#!/usr/bin/python

import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
user_home = str(Path.home())

class FileWatch(FileSystemEventHandler):
    def __init__(self, filename=user_home+'/.bash_history', modfun=None):
        self.filename = filename
        self.modfun = modfun

    def on_modified(self, event):
        if event.src_path == self.filename:
            print(f'event type: {event.event_type}  path : {event.src_path}')
            self.modfun()
        else:
            print('Some other change')

def test():
    print('Test function')


if __name__ == "__main__":
    event_handler = FileWatch(modfun=test)
    observer = Observer()
    observer.schedule(event_handler, path=user_home, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
