#********* ZONA DE FUNCION *********#
def pedir_edad():
    edad = int(input("digite la edad del participante: "))
    return edad

def calcular_edades():
    publico = 0
    suma_edades = 0
    total_personas = 0

    edad = pedir_edad()

    while edad != 0:
        total_personas = total_personas + 1
        suma_edades = suma_edades + edad

        if edad >= 25 and edad <= 45:
            publico = publico + 1
            print("Registrado dentro del publico objetivo")

        edad = pedir_edad()

    return publico, suma_edades, total_personas

def imprimir_edades(publico, suma_edades, total_personas):
    if total_personas > 0:
        promedio = suma_edades / total_personas
    else:
        promedio = 0

    print("Publico objetivo:", publico)
    print("Promedio de edad:", promedio)

#********** ZONA DE CODIGO PRINCIPAL **********#

publico_objetivo, suma_total_edades, personas_encuestadas = calcular_edades()
imprimir_edades(publico_objetivo, suma_total_edades, personas_encuestadas)