import time

with open("example.txt", mode="w", encoding="utf-8") as file:
    message:str = "Hello World!\n"
    written_char: int = file.write(message)
    print(f"Written characters: {written_char}")

class Stopwatch:

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:8f} seconds")

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        
        return False
    
with Stopwatch():

    test_array = [38, 27, 43, 3, 9, 92, 10] * 10000
    sorted_array = sorted(test_array)
    print(f"Original array:{test_array}")
    print(f"Sorted array: {sorted_array}")