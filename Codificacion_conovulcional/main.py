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


def printGraph(G):
    pos = nx.shell_layout(G)
    x1 = 0.0
    x2 = 3.0
    color = ["green"]*len(G.nodes)
    for posicion, clave in enumerate(pos):
        # Hacer algo con esa clave
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
    # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color=color)
    # edges
    nx.draw_networkx_edges(G, pos, width=1.5, arrowstyle='->')
    # labels
    nx.draw_networkx_labels(G, pos, font_size=10,
                            font_family='sans-serif', font_color="white")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
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


def ingresarRelaciones(d, t, t1):
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

    print("Node" + " " * (max_node_length - 4) +
          " | Related Data" + " " * (max_data_length - 12))
    print("-" * (max_node_length + max_data_length + 15))
    for node, data in table_data:
        print(node + " " * (max_node_length - len(node) + 1) +
              "|" + data + " " * (max_data_length - len(data)))


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


def tabla(t, t1, d, s):
    val = imprimir_tabla_verdad(int(d))

    for i in range(len(val)):
        inicial = val[i]
        ent = "0"
        sig = "0"
        for j in range(2):
            aux = list(inicial)
            aux.pop()
            aux.insert(0, ent)
            sig = ''.join(aux)
            print(ent+"|"+inicial+"|"+sig)
            inicial = sig
            if ent == "1":
                ent = "0"
            else:
                ent = "1"
    return


G = nx.DiGraph()    # crear un grafo
t = ["E"]  # Creamos un arreglo de nodos
t1 = []  # creamos un arreglo de relaciones
d = "-1"
s = "-1"
m = "-1"
clear()
while m != "0":
    print(color["blanco"], "|:----------------------------:|")
    print(" | Bienvenido al menu Principal |")
    print(" |:----------------------------:|\n", color["fin"])
    print(color["verde"], "1.Imprimir Modelamiento.")
    print(color["rojo"],  "2. Ingresar Elementos de memoria.")
    print(color["azul"],  "3. Ingresar suma mod 2.")
    print(color["morado"], "4. Ingresar Relaciones.")
    print(color["blanco"], "0. Salir")
    m = input("Opcion: ")
    clear()
    if m == "1":
        if d != "-1" and s == "-1":
            imprimirTablaCon(t, t1)
            printGraph(G)
        elif d != "-1" and s != "-1":
            imprimirTablaCon(t, t1)
            printGraph(G)
            tabla(t, t1, d, s)
        else:
            print("No se puede imprimir nada, ingrese Elementos y sumas")
        input()
        clear()
    if m == "2":
        e = False
        while e == False:
            d = input(color["rojo"] +
                      "cuantos Elementos de Memoria quiere[5-6]: ")
            if int(d) == 5 or int(d) == 6:
                e = True
            clear()
        G = agregarNodos(t, d, 0, G)
    if m == "3":
        if d != "-1":
            e = False
            while e == False:
                s = input(color["morado"]+"Cuantas suma mod 2 quiere[3,4,5]: ")
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
            t1 = ingresarRelaciones(d, t, t1)
            G = crearRelaciones(G, t, t1, 2)
        else:
            print("No se puede Relacionar nada, ingrese Elementos y sumas")
            input()
    clear()
# Añadir nodos
# Añadir aristas


"""print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)
"""
