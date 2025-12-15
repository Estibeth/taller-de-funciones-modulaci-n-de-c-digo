#******* ZONA DE FUNCION ********#
def pedir():
    horas = int(input("Horas extra trabajadas: "))
    return horas

def procesar():
    total_bonificacion = 0
    empleados = 0
    horas = pedir()
    while horas >= 0:
        if horas > 5:
            bono = horas * 15
            total_bonificacion = total_bonificacion + bono
            empleados = empleados + 1
        else:
            if horas > 0:
                bono = horas * 10
                total_bonificacion = total_bonificacion + bono
                empleados = empleados + 1
        horas = pedir()
    return total_bonificacion, empleados

def imprimir(total_bonificacion, empleados):
    print("Bonificacion total:", total_bonificacion)
    print("Empleados con bonificacion:", empleados)

#****** ZONA DE CODIGO PRINCIPAL ********#
total_bonificacion, empleados = procesar()
imprimir(total_bonificacion, empleados)
