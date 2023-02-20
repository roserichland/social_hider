# Print random integers with the same number of digits as a social security number until the
# unlikely even that y and x become equal
# Version 2/11/2021 keyboard listener wonky and enters infinite loop. Expect a lot of numbers!

import random
from pynput import keyboard
from threading import Thread

def on_press(key, abortKey='esc'):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print('pressed %s' % (k))
    if k == abortKey:
        print('end loop ...')
        return False  # stop listener

def loop_social():
    while True:
        r = random.randrange(0, 9)
        s = random.randrange(0, 9)
        t = random.randrange(0, 9)
        u = random.randrange(0, 9)
        v = random.randrange(0, 9)
        w = random.randrange(0, 9)
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        z = random.randrange(0, 9)
        formatted = f"{r}{s}{t}-{u}{v}-{w}{x}{y}{z}"
        print(formatted)

if __name__ == '__main__':
    abortKey = 't'
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
    listener.start()  # start to listen on a separate thread
    # start thread with loop
    Thread(target=loop_social, args=(), name='loop_social', daemon=True).start()
    listener.join # wait for abortKey