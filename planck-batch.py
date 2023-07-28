"""Dieses Skript habe ich geschrieben, um mir für mehrere Messwerte schnell die Planck-Konstante ausrechnen zu lassen."""

from db_handle.database import Database as DB
import constants as c
import math as m
import matplotlib.pyplot as plt

# Datenbank initialisieren
db = DB("planck")
    
# 1/sin(thau) berechnen
def calc_h(d: float):
    measurements = db.get_value("measurements")
    calc = {}
    for voltage in measurements.keys():
        volt = float(voltage)
        h = (c.elementary_charge() * volt) * 2 * d * m.sin(m.radians(measurements[voltage])) / c.speed_of_light()
        calc[voltage] = h
    db.set_value("h", calc)
    

    

if __name__ == "__main__":
    db.delete_all()
    
    measurements = {
        "15000": 12.4,
        "20000": 9.0,
        "25000": 7.4,
        "30000": 5.4,
        "35000": 4.8,
    }
    
    db.set_value("measurements", measurements)
    
    calc_h(2)
    


    