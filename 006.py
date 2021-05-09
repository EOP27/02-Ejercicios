'''
Programa que calcula que te sucederá cuando tengás 5 años más
'''

edad=input("Introducir su edad: ")

if not edad.isdigit():
    print("Por favor, introducir una edad numérica:")
    edad=input()
    
futuro=int(edad)+5

print(f"Dentro de 5 años, usted tendrá {futuro} años y a saber donde estará! :)")
