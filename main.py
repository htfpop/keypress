import keyboard as kb
import time as t
import threading

SLEEP = 5
HALT = 0
time = 3600
iteration = 0
HALT_FLAG = threading.Event()


def sleep():
    print(f'Sleeping for {SLEEP} seconds')
    t.sleep(SLEEP)
    print(f'Awake')


def write():
    global iteration
    while not HALT_FLAG.is_set():
        string = f"[MSG {iteration}]: Test\r"
        kb.write(string)
        iteration += 1
        printer()
        t.sleep(0.2)


def listener():
    print('Listening for key (Press CTRL + SPACE to stop)')
    while not HALT_FLAG.is_set():
        if kb.is_pressed('ctrl + C'):
            print('Keyboard Interrupt')
            HALT_FLAG.set()
        else:
            t.sleep(0.01)  # Shorter sleep time to check more frequently


def printer():
    global iteration
    if iteration % 16 == 0:
        print('\n', end='')
    print('.', end=' ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        sleep()

        # Start threads
        x = threading.Thread(target=listener)
        z = threading.Thread(target=write)
        x.start()
        z.start()

        # Wait for threads to finish

        x.join()
        print("Listener Joined")

        z.join()
        print("Printer Joined")

    except KeyboardInterrupt:
        # Handle CTRL+C to exit gracefully
        print('Interrupted. Stopping threads...')
        HALT_FLAG.set()
        x.join()
        z.join()
