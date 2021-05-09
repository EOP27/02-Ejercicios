'''
Genera un fichero .out que indica el usuario y la fecha en la que se ejecuta
'''


from getpass import getuser
from datetime import date

usuario = getuser()
fecha = date.today()

fichero = "005.out"


with open(fichero, "w") as out:

    out.write("#!/bin/bash\n") #Lanza el terminal
    out.write(f"Usaurio actual: {usuario}, Fecha: {fecha}\n")
