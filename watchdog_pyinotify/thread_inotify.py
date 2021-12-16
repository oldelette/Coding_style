import sys, os, pyinotify
import argparse
import asyncore

# the event handlers:
class MyEventHandler(pyinotify.ProcessEvent):

    def process_IN_ACCESS(self, event):
        print("ACCESS event:", event.pathname)

    def process_IN_ATTRIB(self, event):
        print("ATTRIB event:", event.pathname)

    def process_IN_CLOSE_NOWRITE(self, event):
        print("CLOSE_NOWRITE event:", event.pathname)

    def process_IN_CLOSE_WRITE(self, event):
        print("CLOSE_WRITE event:", event.pathname)

    def process_IN_CREATE(self, event):
        print("CREATE event:", event.pathname)

    def process_IN_DELETE(self, event):
        print("DELETE event:", event.pathname)

    def process_IN_MODIFY(self, event):
        print("MODIFY event:", event.pathname)

    def process_IN_OPEN(self, event):
        print("OPEN event:", event.pathname)

def main():
    # To specify two or more events codes just orize them
    # pyinotify_flags = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
    # Or if you want to be notified for all events just use this shortcut

    pyinotify_flags = pyinotify.ALL_EVENTS
    # watch manager
    watch_manager = pyinotify.WatchManager()
    watch_path = '/tmp'
    watch_manager.add_watch(watch_path, pyinotify_flags, rec=True)  # rec = recursive

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.ThreadedNotifier(watch_manager, MyEventHandler())
    notifier.start()



if __name__ == "__main__":
    main()