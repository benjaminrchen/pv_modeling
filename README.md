# pv_modeling

This project is to build modeling skills. Two models are envisioned:
1) A dynamic model of a residential PV and battery system, to simulate the system's response and behavior over a length of time
2) A cost model of a residential PV and battery system, to optimize costs and estimate payback period

Outline:
Dynamic model:
* User defines system characteristics such as panel area, efficiency, battery capacity, max charge/discharge rate, inverter efficiency, etc.
* User inputs the following time series to run the model: solar profile, residential loads, perhaps electricity costs
* Include potential for addition of system controller which decides how much the battery charges and when
* Model outputs plots of interest: solar power, battery current, battery SOC, etc.