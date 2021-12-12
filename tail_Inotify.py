import sys, os, pyinotify

# from optparse import OptionParser
import argparse


def get_argument():
    parser = argparse.ArgumentParser(description="my description")
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument(
        "--debug", help="print debug messages", action="store_true", dest="debug"
    )
    return vars(parser.parse_args())


# watched events on the directory, and parse $path for file_of_interest:
# dirmask = pyinotify.IN_MODIFY | pyinotify.IN_DELETE | pyinotify.IN_MOVE_SELF | pyinotify.IN_CREATE

already_print_num = 0


def get_last_line():
    filepath = get_argument()["file"]
    global already_print_num
    if not os.path.exists(filepath):
        print(f"no such file {filepath}")
        sys.exit()
        return
    readfile = open(filepath, "r")
    lines = readfile.readlines()
    if len(lines) > 20 and already_print_num == 0:
        already_print_num = len(lines) - 20

    if already_print_num < len(lines):
        print_lines = lines[already_print_num - len(lines) :]
        for line in print_lines:
            print(len(lines), already_print_num, line.replace("\n", ""))
        already_print_num = len(lines)
    readfile.close()


# the event handlers:
class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        get_last_line()

    def process_IN_CREATE(self, event):
        get_last_line()
        return


def main(file_dic: dict):
    # To specify two or more events codes just orize them
    # pyinotify_flags = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
    # Or if you want to be notified for all events just use this shortcut
    if file_dic["debug"]:
        print(f"I am totally opening {myfile}")

    dirmask = (
        pyinotify.IN_MODIFY
        | pyinotify.IN_DELETE
        | pyinotify.IN_MOVE_SELF
        | pyinotify.IN_CREATE
    )
    pyinotify_flags = pyinotify.ALL_EVENTS
    # watch manager
    watch_manager = pyinotify.WatchManager()
    # watch_path = '/var/log/syslog'
    index = file_dic["file"].rfind("/")
    watch_manager.add_watch(file_dic["file"][:index], dirmask)  # rec = recursive

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(watch_manager, eh)
    notifier.loop()


if __name__ == "__main__":
    main(get_argument())
