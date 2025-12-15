#*************** ZONA DE FUNCION **************#
def pedir():
 tipo = input(" 'D' para deposito 'R' para retiro o FIN: ")
 return tipo

def monto():
    monto2 = float(input("monto "))
    return monto2

def calcular():
    saldo = 1000
    transaccion = 0
    tipo_transaccion = pedir()
    while tipo_transaccion != "FIN":
        if tipo_transaccion == "D":
            monto2 = monto()
            saldo = saldo + monto2
            transaccion = transaccion + 1
        else:
            if tipo_transaccion == "R":
                monto2 = monto()
                if saldo - monto2 >= 0:
                    saldo = saldo - monto2
                    transaccion = transaccion + 1
                else:
                    print("su retiro fue denegado, saldo insuficiente")
            else:
                print("tipo no valido")

        tipo_transaccion = pedir()
    return saldo, transaccion

def imprimir(saldo, transaccion):
    print("saldo final:", saldo)
    print("transacciones validas:", transaccion)

#************* ZONA DE CODIGO PRINCIPAL **************#
saldo, transaccion = calcular()
imprimir(saldo, transaccion)
