import binascii
from enum import Enum
from socket import socket

ENCODINGS = {
    "UTF-8": 0,
    "UTF-16": 1,
}

ENCODINGS_REVERSED = ["UTF-8", "UTF-16"]

HEADER_LENGTH = 16
MAX_PACKAGE_LENGTH = 1024
MAX_DATA_LENGTH = MAX_PACKAGE_LENGTH - HEADER_LENGTH


def generate_header(witch_package: int, how_many_packages: int, protocol_version="0.1", data_encoding="UTF-8"):
    encoding = chr(ENCODINGS[data_encoding])
    witch_package_bytes = chr(witch_package)
    how_many_packages = chr(how_many_packages)
    header = f'PTC;{protocol_version};{encoding};{witch_package_bytes};{how_many_packages};\r\n'
    return header


def generate_protocol(data, protocol_version="0.1", data_encoding="UTF-8"):
    max_data_in_encoding = ((MAX_DATA_LENGTH // (1 if data_encoding == "UTF-8" else 2)) -
                            (0 if data_encoding == "UTF-8" else 1))
    how_many_packages_to_send = len(data) * (1 if data_encoding == "UTF-8" else 2) // MAX_DATA_LENGTH
    packages = []
    for i in range(how_many_packages_to_send + 1):
        header_len = generate_header(i, how_many_packages_to_send, protocol_version, data_encoding).encode("UTF-8")
        data_to_send = data[i * max_data_in_encoding:(i + 1) * max_data_in_encoding].encode(data_encoding)
        packages.append(header_len + data_to_send)
    return packages


class ProTooCoolPackage:
    version: str
    which_package: int
    how_many_packages: int
    encoding: str
    data: str

    def __init__(self, data: bytes):
        self.read_header(data)
        self.data = data[16:].decode(self.encoding)

    def read_header(self, data: bytes):
        header = data[:16].decode("UTF-8").split(";")
        if header[0] == "PTC" and header[1] == "0.1":
            self.version = header[1]
            self.encoding = ENCODINGS_REVERSED[ord(header[2])]
            self.which_package = ord(header[3])
            self.how_many_packages = ord(header[4])

    def __str__(self):
        data = (f'version: {self.version}, '
                f'encoding: {self.encoding}, '
                f'which_package: {self.which_package}, '
                f'how_many_packages: {self.how_many_packages}, '
                f'data: {self.data}')
        return data


class CapturePackages:
    how_many_packages: int
    how_many_captured: int
    data: str
    encoding: str

    def __init__(self, package: ProTooCoolPackage):
        self.how_many_packages = package.how_many_packages
        self.how_many_captured = 1
        self.data = package.data
        self.encoding = package.encoding

    def insert(self, package: ProTooCoolPackage | bytes):
        if isinstance(package, ProTooCoolPackage):
            self.how_many_captured += 1
            self.data += package.data
        else:
            package = ProTooCoolPackage(package)
            self.insert(package)

    def get_data(self):
        return self.data


def get_data_from_socket(sock: socket):
    data = sock.recv(1024)
    if not data:
        return None
    first_package = ProTooCoolPackage(data)
    all_data = CapturePackages(first_package)
    while all_data.how_many_captured <= all_data.how_many_packages:
        data = sock.recv(1024)
        if not data:
            continue
        all_data.insert(data)
    return all_data.data


def send_data(sock: socket, data: str):
    data_to_send = generate_protocol(data, data_encoding="UTF-16")
    for i in data_to_send:
        sock.send(i)
