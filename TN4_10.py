#*************** ZONA DE FUNCION *************#
def pedir_unidades():
    unidades = int(input("cantidad de unidades producidas del lote "))
    return unidades

def pedir_estado():
    estado = input("estado (D defectuosa / O ok) ")
    return estado

def calcular():
    defectuosa = 0
    ok = 0
    seguir = input("digite stop para terminar o enter para continuar: ")

    while seguir != "stop":
        unidades = pedir_unidades()

        contador = 0
        while contador < unidades:
            estado = pedir_estado()

            if estado == "D":
                defectuosa = defectuosa + 1
            else:
                if estado == "O":
                    ok = ok + 1
                else:
                    print("Estado inválido")
                    contador = contador - 1

            contador = contador + 1

        seguir = input("escriba  stop para terminar o ente para continuar: ")

    return defectuosa, ok

def mostrar(defectuosa, ok):
    total = defectuosa + ok

    if total > 0:
        porcentaje = (defectuosa * 100) / total
    else:
        porcentaje = 0

    print("defectuosa", defectuosa)
    print("ok:", ok)
    print("porcentaje defectuosa ", porcentaje)

#************* ZONA DE CODIGO PRINCIPAL ************#
D, O = calcular()
mostrar(D, O)
