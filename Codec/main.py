import os
import numpy as np
# importamos funcion de conversion de bit
import valor_8_bit as b8
import valor_10_bit as b10
import valor_12_bit as b12
# fin0,amarillo1,verde2,rojo3,morado4,cian5,azul6,blanco7
color = {
    "fin": "\033[0;m",
    "amarillo":  "\033[;33m",
    "verde": "\033[;32m",
    "rojo": "\033[;31m",
    "morado": "\033[;35m",
    "cian": "\033[;36m",
    "azul": "\033[;34m",
    "blanco": "\033[;37m"
}
# ! Limpiar consola segun Sistema operativo


def clear():
    if os.name == "nt":
        os.system("cls")  # Todo: windows
    else:
        os.system("clear")  # Todo: linux


# ? variables manejando con un banda base en hz
b = 4000  # banda Base en Hz
fs = 2*b  # Frecuencia de muestreo en Hz
ts = 1/fs  # periodo de muestreo en seg
a = 5  # amplitud en V
fo = 2  # frecuencia de oscilación en hz
# creamos un arreglo con el valor de las frecuencia de muestreo y lo multiplicamos por 2 para dos segundos
s = 1
n = np.arange(fs/s)
eje_t = n*ts
# creamos la señal
y = a*np.cos(2*np.pi*fo*n*ts)
# creamos la listas de datos convertidos a bits
bit8 = b8.pasar_v_a_b(y)
bit10 = b10.pasar_v_a_b(y)
bit12 = b12.pasar_v_a_b(y)

r = "1"
e = 1
clear()
while r != "0":
    if e == 1:
        print(color["amarillo"], "Frecuencia de muestreo: ",
              fs, "*", s, "= ", (fs*int(s)), color["fin"])
    elif e == 2:
        print(color["amarillo"], "Frecuencia de muestreo: ",
              fs, "/", s, "= ", fs/int(s), color["fin"])
    print(color["blanco"], "|:----------------------------:|")
    print(" | Bienvenido al menu Principal |")
    print(" |:----------------------------:|\n", color["fin"])
    print(color["verde"], "1.bit8", color["fin"])
    print(color["morado"], "2. Imprimir bit10")
    print(color["azul"], "3. Imprimir bit12")
    print(color["blanco"], "4. Dividir Tiempo del Segundo")
    print(color["blanco"], "5. Multiplicar Tiempo del Segundo")
    print(color["blanco"], "0. Salir")
    r = input("Opcion: ")
    if r == '1':
        b8.menu_8_Bit(eje_t, y, bit8)  # menu bit 8
    if r == '2':
        b10.menu_10_Bit(eje_t, y, bit10)  # menu bit 10
    if r == '3':
        b12.menu_12_Bit(eje_t, y, bit12)  # menu bit 8
    elif r == '4':
        e = 2
        s = input(" Cuanto quiere dividir la frecuencia de muestreo: ")
        n = np.arange(fs/int(s))
        eje_t = n*ts
        # creamos la señal
        y = a*np.cos(2*np.pi*fo*n*ts)
        # creamos la listas de datos convertidos a bits
        bit8 = b8.pasar_v_a_b(y)
        bit10 = b10.pasar_v_a_b(y)
        bit12 = b12.pasar_v_a_b(y)
    elif r == '5':
        e = 1
        s = input(" Cuanto quiere Multiplicar la frecuencia de muestreo: ")
        n = np.arange(fs*int(s))
        eje_t = n*ts
        # creamos la señal
        y = a*np.cos(2*np.pi*fo*n*ts)
        # creamos la listas de datos convertidos a bits
        bit8 = b8.pasar_v_a_b(y)
        bit10 = b10.pasar_v_a_b(y)
        bit12 = b12.pasar_v_a_b(y)
    clear()
