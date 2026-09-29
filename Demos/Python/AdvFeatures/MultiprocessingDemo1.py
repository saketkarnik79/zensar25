from multiprocessing import Process
import os

def calculate_square(number):
    print(
        f"Square of {number} = {number * number}, "
        f"Process ID = {os.getpid()}"
    )

if __name__ == "__main__":

    p1 = Process(target=calculate_square, args=(10,))
    p2 = Process(target=calculate_square, args=(20,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Processing completed")