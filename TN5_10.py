#********** ZONA DE FUNCION ***********#
def pedir_precio():
    precio = float(input("el precio del producto: "))
    return precio

def pedir_cantidad():
    cantidad = int(input("digite la cantidad: "))
    return cantidad

def calcular_compra():
    subtotal = 0
    seguir = input("agregar producto (si/no): ")
    while seguir != "no":
        precio = pedir_precio()
        cantidad = pedir_cantidad()
        subtotal = subtotal + (precio * cantidad)
        seguir = input("agregar otro producto (si/no): ")
    return subtotal

def calcular_descuento(subtotal):
    if subtotal > 1000:
        descuento = subtotal * 0.10
    else:
        if subtotal > 500:
            descuento = subtotal * 0.05
        else:
            descuento = 0
    total = subtotal - descuento
    return total, descuento

def imprimir_total(total, descuento):
    print("descuento aplicado:", descuento)
    print("monto final a pagar:", total)

#************* ZONA DE CODIGO PRINCIPAL ***********#
subtotal = calcular_compra()
total, descuento = calcular_descuento(subtotal)
imprimir_total(total, descuento)
