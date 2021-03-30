import pyvisa
import time
# FOR KEITHLEY 2000


class Keithley2000:

    _timeout: float = 3
    _res:pyvisa.resources.Resource = []

    def __init__(self, resource: pyvisa.resources.Resource, timeout: int):
        _res = resource
        _timeout = timeout

    def SetMode(self, mode: str, continus: bool):
        """[summary]
        Args:
            mode (str): VOLT:DC or VOLT:AC CURR:DC FREQ
            continus (bool): ture on Enable
        Returns:
            bool: Success or Failed
        """
        command = ":SENS:FUNC '" + mode + "'"
        _reswrite(command)

        c = time.time()
        while mode != _resquery(":SENS:FUNC?"):
            if (c + _timeout) <= time.time():
                return False
        return True

        command = ":INIT:CONT" + str(int(continus))
        _reswrite(command)

        c = time.time()
        while int(continus) != int(_resquery(":INIT:CONT?")):
            if (c + _timeout) <= time.time():
                return False
        return True

    def GetValue(self):
        value = _resquery(":FETC?")
        return float(value)
