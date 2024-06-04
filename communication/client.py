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
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

    def server_data_handler(self):
        while True:
            data = get_data_from_socket(self.sock)
            self.event_handler(data)

    def start_server(self):
        thread = threading.Thread(target=self.server_data_handler())
        thread.start()

    def send_message_to_server(self, data):
        send_data(self.sock, data)

