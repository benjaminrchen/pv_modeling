# import stuff

class Battery:
    # Neglects temperature and degradation
    def __init__(self, max_open_circuit_voltage, internal_resistance,
                 capacity):
        self.max_open_circuit_voltage = max_open_circuit_voltage
        self.internal_resistance = internal_resistance
        self.capacity = capacity

# Things to calculate: SOC, VOC
# How to represent IV curve?

    def calc_open_circuit_voltage(TBD) -> float:
        