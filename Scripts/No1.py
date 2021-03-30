import pyvisa
import time
import re
from common import PSS3203

timeout:float = 3;

rm = pyvisa.ResourceManager()
instruments = rm.list_resources()

for inst in instruments:
    print(inst)
print("a")
fg = rm.open_resource(instruments[0])
o_vin = rm.open_resource(instruments[1])
vc = rm.open_resource(instruments[2])
vin = rm.open_resource(instruments[3])
Va = rm.open_resource(instruments[4])
print("a")
import csv
print("a")
count = 51
step = 0.1
print("a")
SetMode('VOLT:DC',False,vc)
SetMode('VOLT:DC',False,vin)
print("a")
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

    
