# spinner.py
# Creates a spinner to use


# Imports
from threading import Thread
from time import sleep, time, gmtime, strftime


# Classes
class Spinner:
    """Creates a simple spinner"""
    # Variables
    is_end = False # Tells the thread to end


    # Methods
    def __init__(self):
        self.start = time()
        self.thrd = Thread(target=self.__spin)
    

    # Public
    def __enter__(self):
        """Starts the thread"""
        self.thrd.start()
    
    
    def __exit__(self, exc_type, exc_value, tb):
        """Ends the thread"""
        self.is_end = True
        self.thrd.join()
    
    
    # Private
    def __spin(self):
        """Spinner method itself"""
        while True:
            for c in '\|/-':
                print(strftime('%M:%S', gmtime(time() - self.start)), c, end='\r')
                sleep(0.5)
                if self.is_end:
                    break
            
            if self.is_end:
                    print(strftime('%M:%S', gmtime(time() - self.start)), "Done!")
                    break