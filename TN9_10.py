#********** ZONA DE FUNCION ***********#
def pedir_vendido():
    vendido = int(input("Cantidad vendida del dia de  hoy: "))
    return vendido

def calcular_inventario():
    stock = 50
    punto = 10

    vendido = pedir_vendido()

    while vendido >= 0:
        stock = stock - vendido

        if stock <= punto:
            print("AVISO DE REPOSICION URGENTE")
            break

        vendido = pedir_vendido()

    return stock

def imprimir_inventario(stock):
    print("Stock final de inventario:", stock)
    print(f"stock final:{stock}")

#******** ZONA DE CODIGO PRINCIPAL *********#
stock_final = calcular_inventario()
imprimir_inventario(stock_final)
