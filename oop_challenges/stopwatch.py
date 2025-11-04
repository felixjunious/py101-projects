import time

class StopWatch:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0

    def start(self):
        if self._start_time is None:
            self._start_time = time.time()

    def stop(self):
        time_passed  = time.time() - self._start_time
        self._elapsed_time += time_passed

    def reset(self):
        self._start_time = None
        self._elapsed_time = 0

    def get_elapsed_time(self):
        return self._elapsed_time

    def display_time(self):
        print(f'Start Time   : {self._start_time}')
        print(f'Elapsed Time : {self.get_elapsed_time()}')

if __name__ == '__main__':
    timer = StopWatch()

    # Start timer
    timer.start()
    print('Timer Started')

    # Example task
    print("Starting a simulated task...")
    time.sleep(2.5)

    # Stop Timer
    timer.stop()
    print('Timer Stopped')

    # Display
    timer.display_time()
    print(f"\nElapsed seconds (numeric): {timer.get_elapsed_time():.2f}")

    # Reset and reuse
    timer.reset()
    print("\nTimer has been reset.")
    timer.display_time()