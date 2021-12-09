# Main File and Program Loop for Local Operations System
# of the ECD109 Smart Electric Meter
# ECD 109
# Denis Nakazawa

import socket
import sqlite3
import time

from energy_information_database import *
from pca_vers_2 import *
#from sender_receiver_flask_server import *

sleep_time = (1 * 60) # 1 minute
    
def main():
    create_database_table()
    los_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        pca_calculation_values = get_energy_information()
        log_information(pca_calculation_values)
        
        los_socket.connect(('192.168.1.91', 24))
        los_socket.send(pca_calculation_values)
        los_socket.close()
        
        time.sleep(sleep_time)

# Run main program loop
main()
    




