import pyvisa
import time


class PSS3203:

    _timeout: float = 3
    _res: pyvisa.resources.Resource = []

    def __init__(self, resource: pyvisa.resources.Resource, timeout: int):
        _res = resource
        _timeout = timeout

    # FOR PSS3203
    def GetVoltage(self, channel: int):
        command = ":CHAN" + str(channel) + ":VOLT?"
        vol = float(_res.query(command))
        return vol

    def SetVoltage(self, channel: int,  voltage: float):
        command = ":CHAN" + str(channel) + ":VOLT " + str(voltage)
        _res.write(command)
        vol = 0.00
        c = time.time()
        while voltage != round(vol, 5):
            vol = GetVoltage(channel)
            print(vol)
            print(voltage)
            if (c + _timeout) <= time.time():
                return False
        return True

    def OutputEnable(self, status: bool):
        if status:
            command = ":OUTP:STAT 1"
        else:
            command = ":OUTP:STAT 0"
        _res.write(command)

        c = time.time()
        while int(status) != int(_res.query(":OUTP:STAT?")):
            print(status)
            print(int(_res.query(":OUTP:STAT?")))
            if (c + _timeout) <= time.time():
                return False
        return True
