import sys
import threading
from concurrent.futures import thread
import socket

from communication.ProTooCool.pro_too_cool_utils import get_data_from_socket, send_data


class Client:
    sock: socket
    host: str
    port: int
    data_thread: thread
    event_handler: any

    def __init__(self, host: str, port: int, event_handler):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.event_handler = event_handler

    def server_data_handler(self):
        while True:
            data = get_data_from_socket(self.sock)
            self.event_handler(data)

    def start_data_handler(self):
        self.data_thread = threading.Thread(target=self.server_data_handler)
        self.data_thread.start()

    def send_message_to_server(self, data):
        print(data, file=sys.stderr)
        send_data(self.sock, data)

