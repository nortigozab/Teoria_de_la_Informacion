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


def printGraph(G, pos, color):
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
    plt.show()


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


G = nx.DiGraph()  # crear un grafo
# Añadir nodos
e = False
while e == False:
    d = input(color["rojo"]+"cuantos Elementos de Memoria quiere: ")
    if int(d) == 5 or int(d) == 6:
        e = True
    clear()
e = False
while e == False:
    s = input(color["morado"]+"Cuantas suma mod 2 quiere: ")
    if int(s) >= 3 and int(s) <= 5:
        e = True
    clear()
t = ["E"]
for i in range(0, int(d)):
    t.append("D"+str((i+1)))
for i in range(0, int(s)):
    t.append("S"+str((i+1)))
G.add_nodes_from(t)
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
print(t1)
# !toca evaluar si los datos estan en la cantidad de S y si no volver a preguntar, y unir los nodos
# Añadir aristas
for i in range(len(t)):
    if t[i] == "E" or t[i][0] == "D":
        if t[i+1][0] != "S":
            G.add_edges_from([(t[i], t[i+1])])
    elif t[i][0] == "S":
        j = int(t[i][1])
        aux = t1[j-1].split(",")
        for k in range(len(aux)):
            G.add_edges_from([(t[int(aux[k])], t[i])])
print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)

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
# dibujo el grafo
printGraph(G, pos, color)
