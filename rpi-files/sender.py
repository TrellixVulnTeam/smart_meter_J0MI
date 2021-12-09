# Program file for Sender Module of Local Operations System
# ECD109
# Denis Nakazawa

import socket

def establish_connection():
    web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '000.000.0.000'
    port = 0000
    web_socket.connect((host, port))