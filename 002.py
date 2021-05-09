path_file='../../../data/shell/Finn.txt'

def contar_palabras(path_file, n_lineas=5):
    '''
    Programa para contar nº de palabras según:
    - nº líneas indicadas por: n_lineas
    - Dirección del fichero: path_file
    '''
    cont_palabras=0
    with open(path_file, 'r') as fichero:
        for i in range (n_lineas):
            linea=fichero.readline()
            n_palabras_linea=len(linea.split())
            print("Nº palabras linea ", i+1,"=", n_palabras_linea)
            cont_palabras+=n_palabras_linea
            
        
        print(f"El total de palabras dentro de las {n_lineas} primeras lineas es: {cont_palabras}")         
        

contar_palabras(path_file,5)
