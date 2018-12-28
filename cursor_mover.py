import sys, time, getopt
from random import randint
from pynput.mouse import Controller
from screeninfo import get_monitors
def print_help():
    print 'cursor_mover.py -s <timeInSeconds>'
    sys.exit(2)

def main(argv):
    wait_seconds = 30
    distance = 100
    random_position = False
    try:
        opts, args = getopt.getopt(argv, "hrs:d:", ['seconds=', 'distance='])
    except getopt.GetoptError:
        print_help()
    for opt, arg in opts:
        if opt == '-h':
            print_help()
        elif opt == '-r':
            random_position = True
        elif opt == '-d':
            try:
                wait_seconds = int(arg)
            except ValueError:
                print_help()
        elif opt == '-s':
            try:
                wait_seconds = int(arg)
            except ValueError:
                print_help()
    mouse = Controller()
    monitor = get_monitors()[0]
    while (True):
        time.sleep(wait_seconds)
        if not random_position:
            mouse.move(randint(-distance, distance), randint(-distance, distance))
        else:
            mouse.position = (randint(0, monitor.width), randint(0, monitor.height))

if __name__ == "__main__":
    main(sys.argv[1:])
