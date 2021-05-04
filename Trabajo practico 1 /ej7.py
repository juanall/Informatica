#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.

CANTIDAD_VENTAS = 4
COMISION        = 0.10
totalComision   = 0.0

sueldoBase = float(input('Ingrese sueldo base $'))
for venta in range(CANTIDAD_VENTAS):
    print('Ingrese monto de la venta No. {0} '.format(venta+1),end='$')
    venta = float(input())
    totalComision += (COMISION)*venta
    print('Las ganancias de comision son ${0}, y el total es ${1}'.format(totalComision,(totalComision+sueldoBase)))



