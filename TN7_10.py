#************ ZONA DE FUNCION ***********#
def pedir_venta():
    venta = float(input("monto de ventas alcanzada por vendedor: "))
    return venta

def colcular_ventas():
    meta = 5000
    cumplidos = 0
    total = 0
    venta = pedir_venta()
    while venta > 0:
        total = total + 1
        if venta >= meta:
            cumplidos = cumplidos + 1
            print("meta cumplida")
        venta = pedir_venta()
    return cumplidos, total

def imprimir_ventas(cumplidos, total):
    print("vendedores con 'meta cumplida'", cumplidos)
    print("total de vendedores procesados", total)

#************ ZONA DE CODIGO PRINCIPAL ***********#
cumplidos, total = colcular_ventas()
imprimir_ventas(cumplidos, total)
