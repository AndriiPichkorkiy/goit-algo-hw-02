import queue as Queue
import time
import random

queue = Queue.Queue()


def generate_request() -> None:
    new_request = f"Request №{str(random.randint(100, 999))}"
    queue.put(new_request)
    pass


def process_request():
    if not queue.empty():
        request = queue.get()
        print("Working on: " + request)
        time.sleep(random.uniform(0.5, 2.8))
    else:
        print("Queue is empty")


def main():
    try:
        while True:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        print("Finish the programm")


if __name__ == "__main__":
    main()
