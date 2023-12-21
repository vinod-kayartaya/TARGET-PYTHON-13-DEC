import time
from threading import Thread


def play_some_music():
    while True:
        print('playing some music...')
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = Thread(target=play_some_music, daemon=True)
    t1.start()
    for _ in range(15):
        print('hello, world')
        time.sleep(0.5)
