import queue
import time
import threading

q = queue.Queue(maxsize=5)


def callback_fcn():
    print("Current Thread is finished")


def dummyfunction(index, q):
    while not q.empty():
        q.get()
        # acts like its doing something for 2 seconds, then is finished
        time.sleep(2)
        q.task_done()
        callback_fcn()


# add 5 different "processes" to this queue
for index in range(5):
    q.put(index)

    # in args is where i will send data for each thread - daemon so itll run in the background
    thread_worker = threading.Thread(target=dummyfunction, args=(index, q), daemon=True)

    # starts the thread
    thread_worker.start()


q.join()

print("all tasks done")
