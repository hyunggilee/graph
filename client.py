import time
from random import randrange
from socketIO_client import SocketIO, LoggingNamespace

'''
Sending data format:
    data= {
        'e': value,
        'latency': value,
    }
'''

if __name__ == '__main__':
    with SocketIO('127.0.0.1', 80, LoggingNamespace) as socketIO:
        while True:
            # Data for testing
            send_data = {
                'latency': randrange(50),
            }

            # Send
            socketIO.emit('mode-change', send_data)
            time.sleep(0.1)
