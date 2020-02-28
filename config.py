import queue

# can have 20 processes in queue
q = queue.Queue(maxsize=20)

# identification # for each process running
index = 0

# list of processes that are added to the queue
queuedJobs = []
