import threading
import time

from app.function import selenium_task

# Assuming you have a list to store threads
threads = []

def get(threads):
    action = "Email"  # Specify the action you're interested in

    # Check if a thread with the specified action is already running
    for t in threads:
        if t['Action'] == action and t['Thread'].is_alive():
            print("Thread is running.")
            return "Thread is running."

    # Remove threads that have completed their tasks
    # threads = [t for t in threads if not t['Thread'].is_alive()]

    # If no running thread found, create a new one
    th = threading.Thread(target=selenium_task, args=())
    threads.append({"Action": action, "Thread": th})
    th.start()
    print("Thread is not running. Creating a new thread.")
    print(threads)
    return "Thread is not running. Creating a new thread."

# Replace 'selenium_task' with the actual function you want to run in a thread

for i in range(20):
    get(threads)
    
