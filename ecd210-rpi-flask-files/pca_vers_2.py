# Simulated Power Calculation Algorithm File
# ECD 109
# Denis Nakazawa

import random

#
# @brief This is a simulated function that returns random values
#        that the power calculation algorithm would return. The
#        values saved in the list are: realPower, reactivePower
#        voltage, current, and energy.
#
# @return A list containing all of these values.
#
def get_energy_information():
    energy_information = []
    for i in range(0, 13):
        energy_information.append(round(random.uniform(800, 1500), 2))
        
    return energy_information