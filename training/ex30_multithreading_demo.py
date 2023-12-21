from threading import Thread, current_thread


class MyThread(Thread):
    def run(self) -> None:
        for i in range(15):
            print(f'{i} --> doing the job for thread - {current_thread().name}')


def some_task(msg):
    for i in range(15):
        print(f'{i} --> {msg} - {current_thread().name}')


if __name__ == '__main__':
    t1 = Thread(name='t1', target=some_task, args=('hello world', ))
    t2 = Thread(name='thread-2', target=some_task, args=('welcome to python multithreading', ))
    t1.start()  # at some point in time, t1.run() will be called, which in turn calls the `target` supplied with `args`
    t2.start()
    for i in range(15):
        print(f'{i} - doing the job for thread - {current_thread().name}')

if __name__ == '__main__0':
    mt1 = MyThread()
    mt1.start()
    for i in range(15):
        print(f'{i} - doing the job for thread - {current_thread().name}')
