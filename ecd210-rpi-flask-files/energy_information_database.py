# Program file for database creation and logging 
# ECD 109
# Denis Nakazawa

import sqlite3
import sys
import time

database_name = 'energy_calculations.db'

def get_database_name():
    return database_name

def create_database_table():
    connection = sqlite3.connect(get_database_name())
    with connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS PCA_calculations")
        cursor.execute("CREATE TABLE PCA_calculations(timestamp DATETIME, real_power_min NUMERIC, real_power_max NUMERIC, real_power_avg NUMERIC, reactive_power_min NUMERIC, reactive_power_max NUMERIC, reactive_power_avg NUMERIC, voltage_min NUMERIC, voltage_max NUMERIC, voltage_avg NUMERIC, current_min NUMERIC, current_max NUMERIC, current_avg NUMERIC, energy NUMERIC)")

def log_information(pca_calculation_values):
    connection = sqlite3.connect(database_name)
    cursor     = connection.cursor()
    
    cursor.execute("INSERT INTO PCA_calculations values(datetime('now'), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?))",
        (pca_calculation_values[0], pca_calculation_values[1], pca_calculation_values[2],
         pca_calculation_values[3], pca_calculation_values[4], pca_calculation_values[5],
         pca_calculation_values[6], pca_calculation_values[7], pca_calculation_values[8],
         pca_calculation_values[9], pca_calculation_values[10], pca_calculation_values[11],
         pca_calculation_values[12]))
    
    connection.commit()
    connection.close()
    
def retrieve_last_database_entry():
    connection = sqlite3.connect(get_database_name())
    cursor = connection.cursor()
    
    for entry in cursor.execute("SELECT * FROM PCA_calculations ORDER BY timestamp DESC LIMIT 1"):
        time_stamp         = str(entry[0])
        real_power_min     = entry[1]
        real_power_max     = entry[2]
        real_power_avg     = entry[3]
        reactive_power_min = entry[4]
        reactive_power_max = entry[5]
        reactive_power_avg = entry[6]
        voltage_min        = entry[7]
        voltage_max        = entry[8]
        voltage_avg        = entry[9]
        current_min        = entry[10]
        current_max        = entry[11]
        current_avg        = entry[12]
        energy             = entry[13]
        
    connection.close()
    
    return (time_stamp,
            real_power_min, real_power_max, real_power_avg,
            reactive_power_min, reactive_power_max, reactive_power_avg,
            voltage_min, voltage_max, voltage_avg,
            current_min, current_max, current_avg,
            energy)

