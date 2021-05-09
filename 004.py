path_file="/home/dsc/data/shell/Text_example.txt"


def generar_fichero(path_file):
    '''
    Copia fichero e incluye nº de línea sobre cada línea:
    - Dirección del fichero: path_file
    '''
    provisional=open("Text_Example.txt",'w')
    with open(path_file, 'r') as fichero:
        print(type(fichero))
        nuevo_fichero=fichero.readlines()
        total_lineas=len(nuevo_fichero) #Sacamos el nº total de líneas para indice

        
        for i in range(total_lineas):
            indice=str(i+1)
            nuevo_fichero[i]=indice+" "+nuevo_fichero[i]
            provisional.write(nuevo_fichero[i]) #Grabamos linea con índice en el nuevo fichero
        
        
        print(nuevo_fichero)
        
    
    provisional.close()
    
    
        
generar_fichero(path_file)
