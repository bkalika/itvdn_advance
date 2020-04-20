import gevent


def task():
    print("Gevent sleep")
    gevent.sleep(1)
    print("Givent finished")


jobs = [
    gevent.spawn(task),
    gevent.spawn(task),
    gevent.spawn(task),
]

gevent.joinall(jobs)
