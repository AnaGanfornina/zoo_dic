"""
1. Calcular precio y tipo en función de la edad y guardarlo para luego

2.Pedir la edad
    Validar  que sea entero positivo
    pedir edades hasta que se introduzca

3. Calcular el precio total del grupo

"""
from enum import Enum

class Entradas(Enum):
    FREE = 0
    CHILD = 1
    ADULT = 2
    YAYO = 3


def calculate_ticket(age:int)->int:
    """
    Calcula el preico de la entrada en función de la edad
    """
    price = 0

    ticket = Entradas.FREE.value
   
    if 3 <= age <= 12:
        price = 14
        ticket = Entradas.CHILD.value
    elif 13 > age < 65:
        price = 23
        ticket = Entradas.ADULT.value
    elif age <= 65:
        price = 18
        ticket = Entradas.YAYO.value
 
    
    

    return price,ticket



def is_int(age:int)-> bool:
    """
    Predicado que comprueba si es un entero positivo
    """
    result = True
    try:
        int(age)
        result = True
    except ValueError:
        result = False

    return result 


def validate(age:int)-> bool:
    """
    Predicado que comprueba si es un entero positivo
    """
    new_age = is_int(age)
    
    return new_age > 0

def ask_age()->list:
    """
    Pedir la edad hasta que el usuario introduzca una cadena vacía
    """
    ages = []
   
    
    while True:
        age = (input("¿Que edad tiene?: ")) 
        if age == "":
            break
        else:
            if validate(age):
                new_age = calculate_ticket(int(age)) 
                ages.append(new_age)

    return ages


def to_print(precio_total,count_ticket,total_ticket ):
    

    #prueba a usar un enumerate en función de los tipos del enum
  
    
    for num in range(3):
        print(f"{count_ticket[num]} entradas {Entradas(num).name} = {total_ticket[num]}€ ")
    
    print(f"Precio total del grupo....{precio_total}€")

      
def calculate_total(ages:list):
    """
    Recibe una lista de edades y tipos, y calcula el total de entradas
    """
    precio_total = 0

    count_ticket = [0,0,0,0]
    total_ticket = [0,0,0,0]

    for precio,tipo in ages:
        precio_total += precio

        count_ticket[tipo] += 1
        total_ticket[tipo] += precio
 
    return to_print(precio_total,count_ticket,total_ticket)   #revisa que devuelve esto para poder pasarselo a  to_print



    
    

#comienza el programa

while True :

    ages = ask_age()
    calculate_total(ages)

    go_on = input("¿Desea continuar?[s/n] ").strip().lower()

    if go_on == "n":
        print("Gracias por su visita")
        break



