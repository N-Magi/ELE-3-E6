import csv
import pyvisa
import time
import re
from .lib import PSS3203
from .lib import Keithley2000

timeout: float = 3

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
o_vin = PSS3203.PSS3203(rm.open_resource(instruments[1]), timeout)
vc = Keithley2000.Keithley2000(rm.open_resource(instruments[2]), timeout)
vin = Keithley2000.Keithley2000(rm.open_resource(instruments[3]), timeout)
Va = Keithley2000.Keithley2000(rm.open_resource(instruments[4]), timeout)

count = 51
step = 0.1

vc.SetMode("VOLT:DC",False)
vin.SetMode("VOLT:DC",False)

o_vin.SetVoltage(1,0)
o_vin.OutputEnable(True)

with open("test.csv","w",newline="") as f:
    wrt = csv.writer(f)
    for itr in range(count):
        iitr = itr * step
        o_vin.SetVoltage(1,iitr)
        time.sleep(1)
        wrt.writerow([vc.GetValue(),vin.GetValue()])
        
o_vin.SetVoltage(1,0)
o_vin.OutputEnable(False)

# SetVoltage(1,0,o_vin)
# OutVoltage(True,o_vin)
# print("a")
# with open("test.csv","w",newline="") as f:
#     www = csv.writer(f)
#     print("a")
#     for Itr in range(count):
#         itr = step * Itr
#         SetVoltage(1,itr,o_vin)
#         time.sleep(1)
#         vin_value = GetValue(vin)
#         c_value = GetValue(vc)
#         www.writerow([vin_value,c_value])
# SetVoltage(1,0,o_vin)
# OutVoltage(False,o_vin)
