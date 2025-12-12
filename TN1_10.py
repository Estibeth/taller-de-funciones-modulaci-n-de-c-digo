#*********** ZONA DE FUNCION ************#
def capturar_productos():
    cantidad_productos = 0 
    suma_calificaciones = 0
    excelente = 0 

    cantidad = int(input("ingrese la cantidad de productos para llevar: "))

    for i in range(cantidad):
        puntuacion = int (input("que puntuacion del 1 a 5 le das: "))

        while puntuacion  < 1 or puntuacion >= 7:
            print("puntuacion incorrecta.")
            puntuacion = int(input("califique el producto del 1 al 5: "))
              
        
        suma_calificaciones = suma_calificaciones + puntuacion
            
        if puntuacion == 5:
            excelente = excelente + 1

        datos = (cantidad_productos, suma_calificaciones, excelente)
        return datos

def imprimir_resultados(datos):
    cantidad_productos, suma_calificaciones, excelente = datos

    print("total de productos:",str(cantidad_productos))
    print("suma de puntuacion:",str(suma_calificaciones))
    print("total excelente:",str(excelente))
    

#**********  ZONA DE CODIGO PRINCIPAL ***********#
datos = capturar_productos()
imprimir_resultados(datos)
