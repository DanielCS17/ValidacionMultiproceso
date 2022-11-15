import os
import time
from time import sleep

def CrearProcesos():
    numProcesos = 10

    while numProcesos > 0:
        
        pid = os.fork()
        numProcesos = numProcesos - 1

        if pid == 0:
            ProcesoHijo()
        else: 
            print("\n \n -> Iniciando el proceso: ", pid, " a las : ", time.strftime('%H:%M:%S', time.localtime()))

        sleep(10)

def ProcesoHijo():
    print("\n -> Iniciando el proceso con PID: %d " % os.getpid())
    sleep(3)
    print("\n -> Terminando el proceso con PID: %d " % os.getpid())
    os._exit(0)

if __name__ == "__main__": 
    CrearProcesos()