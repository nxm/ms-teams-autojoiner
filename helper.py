import time

class Colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    LIGHT_GREY = '\033[37m'

def wait(secs):
    i = 0

    while True:
        if i >= secs:
            print('{}Done!{}'.format(Colors.GREEN, Colors.RESET))
            break

        print('{}Waiting {} secs...{}'.format(Colors.YELLOW, (secs-i), Colors.RESET))
        i += 1
        time.sleep(1)