import time

def stopwatch():
    input("Press Enter to start the stopwatch...")  #input for start
    start_time = time.time()

    input("Press Enter to stop the stopwatch...")  #input for stop
    end_time = time.time()

    duration = end_time - start_time
    print(f"Elapsed time: {duration:.2f} seconds")

stopwatch()