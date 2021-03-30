import pyvisa

timeout:float = 3;

### FOR PSS3203
def GetVoltage(channel:int , res: pyvisa.resources.Resource):
    command = ":CHAN"+ str(channel) + ":VOLT?"
    vol = float(res.query(command))
    return vol

def SetVoltage(channel:int,  voltage:float ,res: pyvisa.resources.Resource):
    command = ":CHAN"+ str(channel) + ":VOLT " + str(voltage)
    res.write(command)
    vol = 0.00
    c = time.time()
    #while voltage != round(vol,5):
    #    vol = GetVoltage(channel,res)
    #    print(vol)
    #    print(voltage)
    #    if (c + timeout) <= time.time(): return False
    return True

def OutVoltage(status:bool,res:pyvisa.resources.Resource):
    if status:
        command = ":OUTP:STAT 1"
    else :
        command = ":OUTP:STAT 0"
    res.write(command)

    c = time.time()
    while int(status) != int(res.query(":OUTP:STAT?")):
        print(status)
        print(int(res.query(":OUTP:STAT?")))
        if (c + timeout) <= time.time(): return False
    return True