import sys, os, pyinotify
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--debug", help="print debug messages", action="store_true", dest="debug")
(options, args) = parser.parse_args()

myfile = args[0] 
if options.debug:
    print (f"I am totally opening {myfile}")

wm = pyinotify.WatchManager()
    
# watched events on the directory, and parse $path for file_of_interest:
dirmask = pyinotify.IN_MODIFY | pyinotify.IN_DELETE | pyinotify.IN_MOVE_SELF | pyinotify.IN_CREATE
    
# open file, skip to end..
#global fh 
#fh = open(myfile, 'r')
#fh.seek(0,2)
#   
already_print_num = 0


def get_last_line(filepath):
    global already_print_num
    if not os.path.exists(filepath):
        print (f'no such file {filepath}')
        sys.exit()
        return
    readfile = open(filepath, 'r')
    lines = readfile.readlines()
    if len(lines) > 20 and already_print_num == 0:
        already_print_num = len(lines) - 20

    if already_print_num < len(lines):
        print_lines = lines[already_print_num - len(lines):]
        for line in print_lines:
            print(len(lines), already_print_num, line.replace('\n',''))
        already_print_num = len(lines)
    readfile.close()





# the event handlers:
class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if myfile not in os.path.join(event.path, event.name):
            return
        else:
            get_last_line(myfile)
            # print(fh.readline().rstrip())
    
    def process_IN_MOVE_SELF(self, event):
        if options.debug:
            print("The file moved! Continuing to read from that, until a new one is created..")

    def process_IN_CREATE(self, event):
        if myfile in os.path.join(event.path, event.name):
            # yay, I exist, umm.. again!
            #global fh
            #fh.close
            #fh = open(myfile, 'r')
            # catch up, in case lines were written during the time we were re-opening:
            if options.debug:
                print ("My file was created! I'm now catching up with lines in the newly created file." )
            #for line in fh.readlines():
            get_last_line(myfile)
            # then skip to the end, and wait for more IN_MODIFY events
            # fh.seek(0,2)
        return
    
    #def get_last_line(self,filepath):
    #    global already_print_num
    #    if not os.path.exists(filepath):
    #        print (f'no such file {filepath}')
    #        sys.exit()
    #        return
    #    readfile = open(filepath, 'r')
    #    lines = readfile.readlines()
    #    if len(lines) > 20 and already_print_num == 0:
    #        already_print_num = len(lines) - 20
    #
    #    if already_print_num < len(lines):
    #        print_lines = lines[already_print_num - len(lines):]
    #        for line in print_lines:
    #            print(len(lines), already_print_num, line.replace('\n',''))
    #        already_print_num = len(lines)
    #    readfile.close()


def main():
    # To specify two or more events codes just orize them
    # pyinotify_flags = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY 
    # Or if you want to be notified for all events just use this shortcut
    pyinotify_flags = pyinotify.ALL_EVENTS

    # watch manager
    watch_manager  = pyinotify.WatchManager()
    # watch_path = '/var/log/syslog'
    index = myfile.rfind('/')
    watch_manager.add_watch(myfile[:index], dirmask) # rec = recursive

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(watch_manager, eh) 
    notifier.loop()
    

if __name__ == '__main__':
    main()


#notifier = pyinotify.Notifier(wm, PTmp())
#
## watch the directory, so we can get IN_CREATE events and re-open the file when logrotate comes along.
## if you just watch the file, pyinotify errors when it moves, saying "can't track, can't trust it.. watch 
##  the directory".
#index = myfile.rfind('/')
#wm.add_watch(myfile[:index], dirmask)
#
#while True:
#    try:
#        notifier.process_events()
#        if notifier.check_events():
#            notifier.read_events()
#    except KeyboardInterrupt:
#        break
#
## cleanup: stop the inotify, and close the file handle:
#notifier.stop()
#fh.close()
#
#sys.exit(0)
