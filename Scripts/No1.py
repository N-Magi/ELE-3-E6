import pyvisa
import time
import re
from common import PSS3203
from common import Keithley2000

timeout:float = 3;

value = float("3")

print(value)

rm = pyvisa.ResourceManager()
instruments = rm.list_resources()

if len(instruments) < 4:
    print("This Mesurement Need Over 4 Instruments \n (DcPowerSupply*2,DMM*2)")
    exit()

print("Find These Instruments...")

for inst in instruments:
    print(inst)

fg = rm.open_resource(instruments[0])
o_vin = rm.open_resource(instruments[1])
vc = rm.open_resource(instruments[2])
vin = rm.open_resource(instruments[3])
Va = rm.open_resource(instruments[4])

import csv

count = 51
step = 0.1

vc = Keithley2000(vc)
vin = Keithley2000(vin)
va = Keithley2000(va)

o_vin = PSS3203(o_vin)


SetMode('VOLT:DC',False,vc)
SetMode('VOLT:DC',False,vin)


SetVoltage(1,0,o_vin)
OutVoltage(True,o_vin)
print("a")
with open("test.csv","w",newline="") as f:
    www = csv.writer(f)
    print("a")
    for Itr in range(count):
        itr = step * Itr
        SetVoltage(1,itr,o_vin)
        time.sleep(1)
        vin_value = GetValue(vin)
        c_value = GetValue(vc)
        www.writerow([vin_value,c_value])
SetVoltage(1,0,o_vin)
OutVoltage(False,o_vin)

    
