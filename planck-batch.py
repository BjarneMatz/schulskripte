import db_handle as jh
import constants as c
import math as m
import matplotlib.pyplot as plt

"""Dieses Skript habe ich geschrieben, um mir für mehrere Messwerte schnell die Planck-Konstante ausrechnen zu lassen."""

def calculate_planck(voltage: float, theta: float, distance: float) -> float:
    planck = (c.elementary_charge() * voltage * 2 * distance * m.sin(m.radians(theta))) / (c.speed_of_light())
    return planck


def draw_graph():
    plt.


if __name__ == "__main__":
    for voltage in jh.get_keys("planck"):
        theta = jh.get_value("planck", voltage)
        
        #Konvertierung von String zu Float
        voltage = float(voltage)
        theta = float(theta)
        
        calculate_planck(voltage, theta, 2.015e-24)
        print(f"Voltage: {voltage}V, Theta: {theta}°, Planck: {calculate_planck(voltage, theta, 2.015e-24)}")
    