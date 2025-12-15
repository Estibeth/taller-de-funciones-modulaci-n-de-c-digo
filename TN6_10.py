#*********** ZONA DE FUNCION **********#
def pedir_cpu():
    cpu = float(input("uso de cpu del servidor "))
    return cpu

def calcular_cpu():
    alertas = 0
    mediciones = 0
    uso = pedir_cpu()
    while uso >= 0:
        mediciones = mediciones + 1
        if uso > 90:
            print("Alerta Uso Critico")
            alertas = alertas + 1
        uso = pedir_cpu()
    return alertas, mediciones

def imprimir_cpu(alertas, mediciones):
    print("total de medicione", mediciones)
    print("ALERTA CRITICA", alertas)


#********* ZONA DE CODIGO PRINCIPAL ***********#
alertas, mediciones = calcular_cpu()
imprimir_cpu(alertas, mediciones)
