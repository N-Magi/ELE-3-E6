import pyvisa
### FOR KEITHLEY 2000

timeout:float = 3;

def SetMode(mode:str, continus: bool , res:pyvisa.resources.Resource):
    """[summary]

    Args:
        mode (str): VOLT:DC or VOLT:AC CURR:DC FREQ
        continus (bool): ture on Enable
        res (pyvisa.resources.Resource): Resrouce instance

    Returns:
        bool: Success or Failed
    """
    command = ":SENS:FUNC '" + mode + "'"
    res.write(command)

    c = time.time()
    while mode != res.query(":SENS:FUNC?"):
        if (c + timeout) <= time.time(): return False
    return True

    command = ":INIT:CONT" + str(int(continus))
    res.write(command)

    c = time.time()
    while int(continus) != int(res.query(":INIT:CONT?")):
        if (c + timeout) <= time.time(): return False
    return True

def GetValue(res:pyvisa.resources.Resource):
    value = res.query(":FETC?")
    return float(value)