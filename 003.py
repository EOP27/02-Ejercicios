path_file="/home/dsc/data/shell/Text_example.txt"
n_lineas=3

def imprimir_lineascontar_palabras(path_file, n_lineas=5):
    '''
    Imprime por pantalla las línes indicadas por variable:
    - nº líneas indicadas por: n_lineas
    - Dirección del fichero: path_file
    '''

    with open(path_file, 'r') as fichero:
        for i in range (n_lineas):
            linea=fichero.readline()
            print(i+1,":", linea)
            
            
imprimir_lineascontar_palabras(path_file,n_lineas)
