import keyboard as kb
import time as t
import threading

SLEEP = 5
HALT = 0
time = 3600
iteration = 0


def sleep():
    print(f'Sleeping for {SLEEP} seconds')
    t.sleep(5)
    print(f'Awake')


def write():
    global iteration
    string = f"[MSG {iteration}]: Test\r"
    kb.write(string)
    # kb.send('enter')
    iteration = iteration + 1


def listener():
    global HALT
    print(f'Listening for key')
    while HALT != 1:
        if kb.is_pressed('ctrl + space'):
            print('pressed')
            HALT = 1
    print(f'listener done')


def printer():
    global HALT
    print_ctr = 0
    while HALT == 0:
        if print_ctr % 16 == 0:
            print('\n', end='')
        print('.', end=' ')
        print_ctr = print_ctr + 1
        t.sleep(1)
    print(f'printer done')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sleep()

    x = threading.Thread(target=listener)
    y = threading.Thread(target=printer)
    x.start()
    y.start()

    while HALT == 0:
        write()
        t.sleep(.1)
