# Pedir al usuario la cantidad de seguidores adicionales y el número de días
seg_adicionales = int(input("Ingrese la cantidad de seguidores adicionales que desea obtener: "))
dias = int(input("Ingrese la cantidad de días que desea esperar para hacer la compra: "))
#Transformamos días a horas; recordar que las variables no pueden llevar acentos ni caracteres como la ñ
horas = dias * 24
#Seguidores perdidos después del tiempo indicado; recordemos que el ** es el operador de potencia
seg_perdidos = 2 ** (horas**0.5)
#Dado que este es el número de seguidores que perdemos en el tiempo indicado
#debemos solicitar la compra de
seg_min_comprar = seg_perdidos + seg_adicionales
#La empresa solo vende en grupos de 100 por lo que se debe calcular cuántos de estos paquetes de 100
#se necesitarían, por ejemplo si necesito 611, tengo que comprar 700
#Si solo divido los 611 en 100 tendríamos 6.11, debemos agregarle 1 a la parte entera dado que existe un resto
#esto se puede solucionar con condicionales o directamente una función, existe igualmente un "truco"
seg_min_comprar = seg_min_comprar + 99
#al sumarle los 99 en nuestro ejemplo 611 pasa a 710 donde la parte entera ahora si es 7, lo que  buscábamos
paquetes_por_comprar = seg_min_comprar // 100
seg_comprar = paquetes_por_comprar * 100
# Calculamos el costo sería
costo_total = paquetes_por_comprar * 2.49
#Finalmente calculamos cuántos seguidores adicionales tendríamos después del tiempo entregado como ejemplo
seg_adicionales_finales = seg_comprar - round(seg_perdidos,0)

#calculamos el descuento
descuento = 0
if seg_comprar < 1000:
    descuento = 0
elif seg_comprar <=9900:
    descuento = 5
elif seg_comprar <= 99900:
    descuento = 15
else:
    descuento = 22
descuento_usd = costo_total*descuento/100
costo_total = costo_total - descuento_usd

#Siendo rigurosos deberíamos no solo redondear los seg_perdidos sino nuevamente
#obtener la parte entera y sumar 1 si la división no es exacta, veremos esto con condicionales
# Imprimir los resultados
print(f"Debe comprar {seg_comprar} seguidores, lo cual cuesta un total de {round(costo_total,2)} $USD. Obtuvo un descuento de {descuento}% correspondiente a {round(descuento_usd,2)}USD")
print(f"Terminaría después de {dias} días con {seg_adicionales_finales} seguidores adicionales aproximadamente.")
