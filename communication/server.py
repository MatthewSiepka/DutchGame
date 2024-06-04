import socket
import threading

from communication.ProTooCool.pro_too_cool_utils import get_data_from_socket, send_data


class Server:
    host: str
    port: int
    sock: socket.socket
    connections: list[socket.socket]
    event_listener: any
    specific_event_listener: dict

    def __init__(self, event_listener, host="", port=0):
        self.event_listener = event_listener
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        sock.listen()
        data_about_socket = sock.getsockname()
        self.host = data_about_socket[0]
        self.port = data_about_socket[1]


    def start(self):
        threading.Thread(target=self.server_listen)

    def server_listen(self):
        while True:
            conn, addr = self.sock.accept()
            thread = threading.Thread(target=self.handler_client_connection, args=(self, conn, addr))
            thread.start()

    def handler_client_connection(self, conn, addr):
        while True:
            self.connections.append(conn)
            data = get_data_from_socket(conn)
            if addr in self.specific_event_listener:
                self.specific_event_listener[addr](conn, addr, data)
            else:
                self.event_listener(conn, addr, data)



    def bind_evnet_listener(self, addr, event_listener):
        self.specific_event_listener[addr] = event_listener
