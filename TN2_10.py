#*********** ZONA DE FUNCION ***********#
def pedir_codigo():
    code = input("ingrese su codigo de identificacion ")
    return code

def validar_codigo(code, acceso_especial):
    if code == acceso_especial:
        return True
    else:
        return False
    
def calcular_accesos():
    codigo_especial = "1234"
    acceso_permitido = 0
    acceso_denegado = 0
    while True:
        cod = pedir_codigo()
        if cod == "salir":
            break
        if validar_codigo(cod, codigo_especial):
            print("accceso permitido")
            acceso_permitido = acceso_permitido + 1
        else:
            print("Acceso denegado.")
            acceso_denegado = acceso_denegado + 1
    return acceso_permitido, acceso_denegado

def imprimir_resultados(acceso_permitido, acceso_denegado):
    print("acceso permitido", acceso_permitido)
    print("Acceso denegado", acceso_denegado)





#************* ZONA DE CODIGO PRINCIPAL *************#
acceso_permitido, acceso_denegado = calcular_accesos()
imprimir_resultados(acceso_permitido, acceso_denegado)
