import os
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
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


def clear():
    if os.name == "nt":
        os.system("cls")  # Todo: windows
    else:
        os.system("clear")  # Todo: linux


def printGraph(G, w=[], ref=[], d="0"):
    # Crear la figura y los ejes
    fig = plt.figure(figsize=(10, 5))

    # Tabla con datos de w en el lado izquierdo superior
    tabla_ax = fig.add_subplot(2, 3, 1)
    datos = w
    tabla = tabla_ax.table(cellText=datos, loc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)
    tabla.scale(1, 1)
    tabla_ax.axis('off')

    # Gráfico nx en el lado izquierdo inferior
    graph_ax = fig.add_subplot(2, 3, 4)
    pos = nx.shell_layout(G)
    x1 = 0.0
    x2 = 3.0
    color = ["green"] * len(G.nodes)
    for posicion, clave in enumerate(pos):
        if clave[0] == "E":
            pos[clave][0] = x1
            pos[clave][1] = 0.0
            x1 += 3
        elif clave[0] == "D":
            pos[clave][0] = x1
            pos[clave][1] = 0.0
            x1 += 3
            color[posicion] = "red"
        else:
            pos[clave][0] = x2
            pos[clave][1] = -4.0
            x2 += 3
            color[posicion] = "purple"
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos, node_size=500,
                           node_color=color, ax=graph_ax)
    nx.draw_networkx_edges(G, pos, width=1.5, arrowstyle='->', ax=graph_ax)
    nx.draw_networkx_labels(
        G, pos, font_size=10, font_family='sans-serif', font_color="white", ax=graph_ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=graph_ax)
    graph_ax.axis('off')

    # Tabla con datos de ref dividida en dos en el lado derecho completo
    tabla_ax1 = fig.add_subplot(2, 3, (2, 5))
    titulo = ref[0]
    # print(len(ref))
    datos1 = [titulo] + ref[1:(len(ref)-1)//2]
    datos2 = [titulo] + ref[(len(ref)-1)//2:]
    # print("datos1: ", datos1)
    # print("datos2: ", datos2)
    # print("ref: ", ref)
    tabla1 = tabla_ax1.table(cellText=datos1, loc='center')
    tabla1.auto_set_font_size(False)
    if int(d) > 4:
        tabla1.set_fontsize(8)
        tabla1.scale(0.8, 0.8)
    else:
        tabla1.set_fontsize(10)
        tabla1.scale(1, 1)
    tabla_ax1.axis('off')

    tabla_ax2 = fig.add_subplot(2, 3, (3, 6))
    tabla2 = tabla_ax2.table(cellText=datos2, loc='center')
    tabla2.auto_set_font_size(False)
    if int(d) > 4:
        tabla2.set_fontsize(8)
        tabla2.scale(0.8, 0.8)
    else:
        tabla2.set_fontsize(10)
    tabla_ax2.axis('off')
    plt.show(block=False)


def evaluarDir(a, n):
    e = False
    b = a.split(",")
    if len(b) > 1:
        c = 0
        for i in range(len(b)):
            if int(b[i]) <= int(n):
                c += 1
        if c == len(b):
            e = True
    return e


def agregarNodos(t, n, a, G):
    if a == 0:
        for i in range(0, int(n)):
            t.append("D"+str((i+1)))
    else:
        for i in range(0, int(n)):
            t.append("S"+str((i+1)))
    G.add_nodes_from(t)
    return G


def ingresarRelaciones(d, t):
    t1 = []
    for i in range(int(d)+1, len(t)):
        e = False
        while e == False:
            print(color["morado"], "*Si es la entrada ingrese",
                  color["verde"], " 0")
            print(color["morado"], "*Dividir los caracteres con una coma")
            print(color["morado"], "* Recordar que son "+color["rojo"] +
                  d+" Elementos de memoria y "+color["verde"]+"la entrada")
            print("_____________________________________")
            r = input(color["morado"] +
                      " que valores estan direccionados a "+t[i]+": ")
            e = evaluarDir(r, d)
            clear()
        t1.append(r)
    return t1


def crearRelaciones(G, t, t1, a):
    for i in range(len(t)):
        if a == 1:
            if t[i] == "E" or t[i][0] == "D":
                if t[i+1][0] != "S":
                    G.add_edges_from([(t[i], t[i+1])])
        elif a != 1:
            if t[i] == "E" or t[i][0] == "D":
                if t[i+1][0] != "S":
                    G.add_edges_from([(t[i], t[i+1])])
            elif t[i][0] == "S":
                j = int(t[i][1])
                aux = t1[j-1].split(",")
                for k in range(len(aux)):
                    G.add_edges_from([(t[int(aux[k])], t[i])])
    return G


def imprimirTablaCon(t, t1):
    # Filtrar elementos que comienzan con "E" o "D" y luego los que comienzan con "S"
    e_d_elements = [node for node in t if node.startswith(
        "E") or node.startswith("D")]
    s_elements = [node for node in t if node.startswith("S")]

    # Crear una tabla con los elementos de "E" y "D"
    table_data = [[node, ""] for node in e_d_elements]

    # Agregar los elementos de "S" en la misma columna si hay una correspondiente en t1
    for s_node in s_elements:
        index = int(s_node[1]) - 1
        if index < len(t1):
            related_data = [e_d_elements[int(i)] for i in t1[index].split(",")]
            table_data.append([s_node, ",".join(related_data)])
        else:
            table_data.append([s_node, ""])

    # Imprimir la tabla
    max_node_length = max(len(node) for node, _ in table_data)
    max_data_length = max(len(data) for _, data in table_data)

    # print("Node" + " " * (max_node_length - 4) +" | Related Data" + " " * (max_data_length - 12))
    # print("-" * (max_node_length + max_data_length + 15))
    ss = [["Nodo", "Valores"]]
    for node, data in table_data:
        ss.append([node, data])
        # print(node + " " * (max_node_length - len(node) + 1) +"|" + data + " " * (max_data_length - len(data)))
    return ss


def imprimir_tabla_verdad(n):
    total_filas = 2**n  # Calcula el número total de filas

    # Generar las filas de la tabla de verdad
    filas = []
    for i in range(total_filas):
        fila = []
        for j in range(n):
            # Obtiene el valor del bit correspondiente
            bit = (i >> (n - j - 1)) & 1
            fila.append(str(bit))
        filas.append("".join(fila))

    # Imprimir los bits en una cadena
    return filas


def tabla(t1, d, ref):
    val = imprimir_tabla_verdad(int(d))
    ref = [["Ent", "Ini", "Sig", "Sal"]]
    # print("{:<2} {:<4} {:<2} {:<6} {:<2} {:<6} {:<2} {:<11} {:<2}".format( "|", "Ent", "|", "Inicial", "|", "Siguiente", "|", "Salidas", "|"))
    for i in range(len(val)):
        inicial = val[i]
        ent = "0"
        sig = "0"
        for j in range(2):
            aux = list(inicial)
            aux.insert(0, ent)
            aux[1] = ent
            sig = ''.join(aux)
            ss = ""
            for k in range(len(t1)):
                au = t1[k].split(",")
                y3 = []
                for h in range(len(au)):
                    k1 = int(au[h])
                    y3.append(aux[k1])
                resul = int(y3[0])
                for elemento in y3[1:]:
                    resul ^= int(elemento)
                ss += str(resul)
                if k != len(t1)-1:
                    ss += ","
            # print("{:<2} {:<4} {:<2} {:<7} {:<2} {:<7} {:<2} {:<11} {:<2}".format("|", ent, "|", inicial, "|", sig[1:], "|", ss, "|"))
            ref.append([ent, inicial, sig[1:], ss])
            if ent == "1":
                ent = "0"
            else:
                ent = "1"
    return ref


G = nx.DiGraph()    # crear un grafo
t = ["E"]  # Creamos un arreglo de nodos
t1 = []  # creamos un arreglo de relaciones
d = "-1"
s = "-1"
m = "-1"
ref = []
clear()
while m != "0":
    print(color["blanco"], "|:----------------------------:|")
    print(" | Bienvenido al menu Principal |")
    print(" |:----------------------------:|\n", color["fin"])
    if d != "-1" and s != "-1" and len(t1) > 0:
        print(color["verde"], "1.Imprimir Modelamiento.")
    print(color["rojo"],  "2. Ingresar Elementos de memoria.")
    print(color["azul"],  "3. Ingresar suma mod 2.")
    print(color["morado"], "4. Ingresar Relaciones.")
    print(color["amarillo"], "5. Reiniciar.")
    if d != "-1" and s != "-1" and len(t1) > 0:
        print(color["cian"], "6. Ingresar palabras.")
    print(color["blanco"], "0. Salir")
    m = input("Opcion: ")
    clear()
    if m == "1":
        if d != "-1" and s != "-1" and len(t1) > 0:
            w = imprimirTablaCon(t, t1)
            ref = tabla(t1, d, ref)
            printGraph(G, w, ref, d)
        else:
            print("No se puede imprimir nada, ingrese Elementos y sumas")
        input()
        clear()
        plt.close(1)
    if m == "2":
        if d == "-1":
            e = False
            while e == False:
                d = input(color["rojo"] +
                          "cuantos Elementos de Memoria quiere[<=6]: ")
                if int(d) >= 2 and int(d) <= 6:
                    e = True
                clear()
            G = agregarNodos(t, d, 0, G)
    if m == "3":
        if d != "-1":
            if s == "-1":
                e = False
                while e == False:
                    s = input(color["azul"] +
                              "Cuantas suma mod 2 quiere[3,4,5]: ")
                    if int(s) >= 3 and int(s) <= 5:
                        e = True
                    clear()
                G = agregarNodos(t, s, 1, G)
        else:
            print(
                color["amarillo"]+"Ingrese valor para Elementos de memoria primero"+color["fin"])
            input()
    if m == "4":
        if d != "-1" and s != "-1":
            t1 = ingresarRelaciones(d, t)
            G = crearRelaciones(G, t, t1, 2)
        else:
            print("No se puede Relacionar nada, ingrese Elementos y sumas")
            input()
    if m == "5":
        H = nx.DiGraph()    # crear un grafo
        G = H
        t = ["E"]  # Creamos un arreglo de nodos
        t1 = []  # creamos un arreglo de relaciones
        d = "-1"
        s = "-1"
        ref = []
        plt.close(1)
        print(color["verde"], " Reinicio Efectivo ", color["fin"])
        input()
    if m == "5":
        H = nx.DiGraph()    # crear un grafo
        G = H
        t = ["E"]  # Creamos un arreglo de nodos
        t1 = []  # creamos un arreglo de relaciones
        d = "-1"
        s = "-1"
        ref = []
        plt.close(1)
        print(color["verde"], " Reinicio Efectivo ", color["fin"])
        input()
    clear()
# Añadir nodos
# Añadir aristas


"""print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)
"""
