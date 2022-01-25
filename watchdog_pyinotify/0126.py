import sys, os, pyinotify
import time
import argparse
import asyncore
import threading


class FileHandler(pyinotify.ProcessEvent):

    def process_IN_MODIFY(self, event):
        print("Modify event:", event.pathname)


# the event handlers:
class DirHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        print("Create file event:", event.pathname)
        # if event.pathname == '/tmp/test/b.log':


def main():
    # To specify two or more events codes just orize them
    # pyinotify_flags = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
    # Or if you want to be notified for all events just use this shortcut
    
    print(f"Start: {threading.active_count()}")

    pyinotify_flags = pyinotify.ALL_EVENTS
    # watch manager
    watch_manager = pyinotify.WatchManager()
    # watch_path = '/tmp/test'
    watch_path = '/tmp/test/aa.log'
    wdd = watch_manager.add_watch(watch_path, pyinotify_flags, rec=True)  # rec = recursive

    # notifier
    # notifier = pyinotify.ThreadedNotifier(watch_manager, DirHandler())
    notifier = pyinotify.ThreadedNotifier(watch_manager, FileHandler())
    notifier.start()
    print(f"Third: {threading.active_count()}")

    print(wdd[watch_path]) 
    # time.sleep(2)
    # watch_manager.rm_watch(wdd[watch_path])

if __name__ == "__main__":
    main()
