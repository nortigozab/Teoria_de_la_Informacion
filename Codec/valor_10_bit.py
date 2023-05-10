import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from reedsolo import RSCodec
import random
matplotlib.use('TkAgg')
x = 0.0097656
inter = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
         "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"]
seg = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
       "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
segv = [[0, 0.3125], [0.3125, 0.625], [0.625, 0.9375], [0.9375, 1.25], [1.25, 1.5625], [1.5625, 1.875], [1.875, 2.1875], [2.1875, 2.5], [
    2.5, 2.8125], [2.8125, 3.125], [3.125, 3.4375], [3.4375, 3.75], [3.75, 4.0625], [4.0625, 4.375], [4.375, 4.6875], [4.6875, 5]]
orden = [1, 5, 10]
# * Limpiar pantalla


def clear():
    if os.name == "nt":
        os.system("cls")  # Todo: windows
    else:
        os.system("clear")  # Todo: linux


# * Colores de impresion
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


def valor_10_bit(c):
    def encontar_seg(t):
        for i in range(len(segv)):
            if (t >= segv[i][0] and t <= segv[i][1]):
                if (t == segv[i][1]):
                    if (i == (len(segv)-1)):
                        return i
                    else:
                        return i+1
                else:
                    return i

    def encontrar_int(t, c):
        a = 0
        i = segv[t][0]
        j = i+x
        for k in range(len(inter)):
            if (k == (len(inter)-1) and c >= j):
                return k
            else:
                if (c >= i and c <= j):
                    if (c == j):
                        if (k == (len(inter)-1)):
                            return k
                        else:
                            return k+1
                    else:
                        return k
                else:
                    i = i+x
                    j = j+x
    sig = 0
    if (c < 0):
        sig = 1
        c = c*-1
    else:
        sig: 0
    se = encontar_seg(c)
    ine = encontrar_int(se, c)
    return str(sig)+seg[se]+inter[ine]


def pasar_b_a_v(x1):
    lista = []
    for i in range(len(x1)):
        lista.append(valor_v(x1[i]))
    return lista


def valor_v(x1):
    val = [x1[orden[0]:orden[1]], x1[orden[1]:orden[2]], x1[0:orden[0]]]
    val1 = [0, 0]
    for i in range(len(val)-1):
        sum = 0
        tam = len(val[i])-1
        for j in range(len(val[i])):
            x2 = val[i]
            sum = sum+(int(x2[j])*pow(2, tam))
            tam = tam-1
        val1[i] = sum
    i = segv[int(val1[0])][0]
    j = i+(x*val1[1])
    i = j-x
    valor = (i+j)/2
    if val[2] == "1":
        valor = valor*-1
    return valor


def pasar_v_a_b(x):
    lista = []
    for i in range(len(x)):
        lista.append(valor_10_bit(round(x[i].tolist(), 3)))
    return lista


def imprimir_bit10_V(eje_t, y, bit10):
    fig = plt.figure(figsize=(15, 15))
    fig.tight_layout()
    f1 = fig.add_subplot(1, 2, 1)
    f2 = fig.add_subplot(1, 2, 2)
    v = pasar_b_a_v(bit10)
    f1.plot(eje_t, y, "r")
    f2.plot(eje_t, v, "b")
    f1.set_title("Grafica 1(cos)")
    f1.set_xlabel("Tiempo (s)")
    f1.set_ylabel("Amplitud (V)")
    f1.set_yticks(np.arange(-5, 6, 1))
    f2.set_title("Grafica 2(Cod)")
    f2.set_xlabel("Tiempo (s)")
    f2.set_ylabel("Amplitud (V)")
    f2.set_yticks(np.arange(-5, 6, 1))
    plt.show()
    """
    f2 = fig.add_subplot(1, 4, 2)
    f3 = fig.add_subplot(1, 4, 3)
    f4 = fig.add_subplot(1, 4, 4)
    f2.plot(eje_t, np.array(bit8))
    v = pasar_b_a_v(bit8)
    f3.plot(eje_t, v, "b")
    f4.stem(eje_t, np.array(v), "g")
    f2.invert_yaxis()
    f1.set_title("Grafica 1(cos)")
    f1.set_xlabel("Tiempo (s)")
    f1.set_ylabel("Amplitud (V)")
    f1.set_yticks(np.arange(-5, 6, 1))
    f2.set_title("Grafica 2( 8 bit)")
    f2.set_xlabel("Tiempo (s)")
    f2.set_ylabel("Amplitud (bit)")
    f2.set_yticks(np.arange(0, pow(2, 8), 8))
    f3.set_title("Grafica 3( 8 bit, Discriminada)")
    f3.set_xlabel("Tiempo (s)")
    f3.set_ylabel("Amplitud (v)")
    f3.set_yticks(np.arange(-5, 6, 1))
    f4.set_title("Grafica 4( 8 bit, Discriminada)")
    f4.set_xlabel("Tiempo (s)")
    f4.set_ylabel("Amplitud (v)")
    f4.set_yticks(np.arange(-5, 6, 1))"""
    plt.show()


def imprimir_bit10_Codi(eje_t, bit10, titulo):
    fig = plt.figure(figsize=(15, 15))
    fig.tight_layout()
    f1 = fig.add_subplot(1, 1, 1)
    f1.plot(eje_t, np.array(bit10))
    f1.invert_yaxis()
    f1.set_title("Grafica("+titulo+")")
    f1.set_xlabel("Tiempo (s)")
    f1.set_ylabel("Amplitud (bit)")
    f1.set_yticks(np.arange(0, pow(2, 5), 5))
    plt.show()


def imprimir_bit10_Deco(eje_t, bit10, titulo):
    fig = plt.figure(figsize=(15, 15))
    fig.tight_layout()
    f1 = fig.add_subplot(1, 1, 1)
    v = pasar_b_a_v(bit10)
    f1.plot(eje_t, v, "b")
    f1.set_title("Grafica("+titulo+")")
    f1.set_xlabel("Tiempo (s)")
    f1.set_ylabel("Amplitud (V)")
    f1.set_yticks(np.arange(-5, 6, 1))
    plt.show()

# ! Seccion Reed_Solomon

# * Codificador Reed-solomon


def encoder(bit10, encod, eje_t, rsc):
    encod = [rsc.encode(word.encode('utf-8'))for word in bit10]
    print("-> Palabras Codificadas")
    p = ""
    for i in range(len(encod)):
        bit10[i] = str(encod[i])[12:20]
        p += str(i+1)+": |"+str(encod[i])+" |"
        if i % 10 == 0:
            p += "\n\n"
    print(p)
    imprimir_bit10_Codi(eje_t, bit10, "Codificacion Reed-Solomon")
    input()
    return bit10, encod

# * Decodificador Reed-solomon


def dencoder(bit10, encod, eje_t, rsc):
    decod = []
    for i in range(len(encod)):
        decoded_bytes = rsc.decode(encod[i])[0]
        decoded_word = decoded_bytes.decode('utf-8')
        decod.append(decoded_word)
    print("-> Palabras Decodificadas")
    p = ""
    for i in range(len(decod)):
        bit10[i] = str(decod[i])
        p += str(i+1)+": |"+str(decod[i])+" |"
        if i % 10 == 0:
            p += "\n\n"
    print(p)
    imprimir_bit10_Codi(eje_t, bit10, "Decodificacion Reed-Solomon")
    input()
    return bit10


def generar_errores(bit10, eje_t, encod, num_errors):
    for i in range(len(encod)):
        # Generar num_errors posiciones aleatorias para cambiar (flip) bits
        error_positions = random.sample(range(len(encod[i])), num_errors)

        # Cambiar (flip) los bits en esas posiciones
        if isinstance(encod[i], str):
            encod[i] = bytearray(encod[i], 'utf-8')
        for j in error_positions:
            encod[i][j] ^= 1
        bit10[i] = str(encod[i])[12:20]
    imprimir_bit10_Codi(eje_t, bit10, "Errores")
    return encod, bit10


def menu_10_Bit(eje_t, y, bit10):
    r = "-1"
    rsc = RSCodec(12)
    encoder_list = []
    en = 0  # *Variable para saber si esta codificado en reed_solomon
    er = 0  # *Variable para saber si ingreso Errores en reed_solomon
    de = 0  # *Variable para saber si decodifico en reed_solomon
    while r != "0":
        clear()
        print(color["rojo"]+str(rsc.gen)+color["fin"])
        print(color["morado"], "|:---------------------------:|")
        print(" | Bienvenido al menu de bit10 |")
        print(" |:---------------------------:|\n")
        print(color["morado"], "1. Imprimir Señal", color["fin"])
        print(color["morado"], "2. Imprimir Codificacion", color["fin"])
        print(color["morado"], "3. Encode Reed-Solomon", color["fin"])
        print(color["morado"], "4. Ruido", color["fin"])
        print(color["morado"], "5. Decode Reed-Solomon", color["fin"])
        print(color["morado"], "6. Imprimir Decodificacion", color["fin"])
        print(color["morado"], "0. Salir", color["fin"])
        r = input(color["morado"]+"Opcion: ")
        print(color["fin"])
        if r == "1":
            imprimir_bit10_V(eje_t, y, bit10)
        if r == "2":
            imprimir_bit10_Codi(eje_t, bit10, "Codificacion")
        if r == "3":
            bit10, encoder_list = encoder(bit10, encoder_list, eje_t, rsc)
            en = 1
        if r == "4":
            if en != 1:
                print(color["rojo"],
                      "No a Codificado con Reed-Solomon", color["fin"])
                input()
            else:
                if er != 1:
                    er = 1
                    encoder_list, bit10 = generar_errores(
                        bit10, eje_t, encoder_list, 5)
                else:
                    print(color["rojo"],
                          "Ya ingreso Errores", color["fin"])
        if r == "5":
            if en != 1:
                print(color["rojo"],
                      "No a Codificado con Reed-Solomon", color["fin"])
                input()
            else:
                if er != 1:
                    bit10 = dencoder(bit10, encoder_list, eje_t, rsc)
                    print(color["rojo"],
                          "No a ingresado Errores", color["fin"])
                else:
                    bit10 = dencoder(bit10, encoder_list, eje_t, rsc)
                    print(color["rojo"], "Si Ingresos Errores", color["fin"])
                    er = 0
                    en = 0
                de = 1
        if r == "6":
            if en != 1:
                print(color["rojo"],
                      "No a Codificado con Reed-Solomon", color["fin"])
                imprimir_bit10_Deco(eje_t, bit10, "Decodificación Sin errores")
            else:
                if er != 1:
                    print(color["rojo"],
                          "No a ingresado Errores", color["fin"])
                    imprimir_bit10_Deco(
                        eje_t, bit10, "Decodificación Sin errores")
                    input()
                else:
                    print(color["morado"], "Si Ingresos Errores", color["fin"])
                    if de == 1:
                        imprimir_bit10_Deco(
                            eje_t, bit10, "Decodificación con correción errores")
                        en = 0
                        er = 0
                        de = 0
                        input()
                    else:
                        print(color["rojo"],
                              "no ha Decodificado", color["fin"])
                        input()
        clear()
