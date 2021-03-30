import pyvisa
import time


class PSS3203:

    _timeout: float = 3
    _res: pyvisa.resources.Resource = []

    def __init__(self, resource: pyvisa.resources.Resource, timeout: int):
        _res = resource
        _timeout = timeout

    # FOR PSS3203
    def GetVoltage(channel: int):
        command = ":CHAN" + str(channel) + ":VOLT?"
        vol = float(res.query(command))
        return vol

    def SetVoltage(channel: int,  voltage: float):
        command = ":CHAN" + str(channel) + ":VOLT " + str(voltage)
        _res.write(command)
        vol = 0.00
        c = time.time()
        while voltage != round(vol, 5):
            vol = GetVoltage(channel, res)
            print(vol)
            print(voltage)
            if (c + _timeout) <= time.time():
                return False
        return True

    def OutVoltage(status: bool):
        if status:
            command = ":OUTP:STAT 1"
        else:
            command = ":OUTP:STAT 0"
        _res.write(command)

        c = time.time()
        while int(status) != int(res.query(":OUTP:STAT?")):
            print(status)
            print(int(res.query(":OUTP:STAT?")))
            if (c + _timeout) <= time.time():
                return False
        return True
