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
