# Program file for the Flask server that runs on the
# Local Operations System
# ECD210
# Jennifer Thakkar

import sqlite3

from energy_information_database import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def render_local_interface():
    time_stamp, real_power_avg, apparent_power_avg, voltage_avg, ccurrent_avg = retrieve_last_database_entry()
    
    template_data = {
        'timeStamp'        : time_stamp,
        'realPowerAvg'     : real_power_avg,
        'apparentPowerAvg' : apparent_power_avg,
        'voltageAvg'       : voltage_avg,
        'currentAvg'       : current_avg,
    }
    
    return render_template('index.html', **template_data)

if __name__ == "__main__":
    app.run(host = '192.168.1.91', port = 24, debug = True)
