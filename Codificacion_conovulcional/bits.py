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


def printGraph(G, w=[], ref=[], pal=[], d="0", b=0):
    # Crear la figura y los ejes
    fig = plt.figure(figsize=(10, 5))
    root = plt.get_current_fig_manager().window
    root.title("Datos de "+str(b)+" Bits")
    # Tabla con datos de w en el lado izquierdo superior
    tabla_ax = fig.add_subplot(2, 3, 1)
    datos = w
    tabla = tabla_ax.table(cellText=datos, loc='center')
    tabla.auto_set_font_size(True)
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
    # print(len(ref))
    datos1 = ref
    tabla1 = tabla_ax1.table(cellText=datos1, loc='center')
    tabla1.auto_set_font_size(True)
    tabla_ax1.axis('off')
    tabla_ax2 = fig.add_subplot(2, 3, (3, 6))
    datos2 = pal
    tabla2 = tabla_ax2.table(cellText=datos2, loc='center', cellLoc='center')
    tabla2.auto_set_font_size(True)
    tabla_ax2.axis('off')

    plt.show(block=False)


def tabla(t1, d, r, ref):
    pal = ""
    pal1 = [["Palabra Original"], [r], ["Palabra Codificada"]]
    ref = [["Ent", "Ini", "Sig", "Sal"]]
    inicial = "0"*int(d)
    palabra = list(r)
    # print("{:<2} {:<4} {:<2} {:<6} {:<2} {:<6} {:<2} {:<11} {:<2}".format("|", "Ent", "|", "Inicial", "|", "Siguiente", "|", "Salidas", "|"))
    for i in reversed(palabra):
        ent = i
        aux = list(inicial)
        aux.insert(0, ent)
        sig = ''.join(aux)
        aux1 = list(inicial)
        aux1.insert(0, ent)
        act = ''.join(aux1)
        ss = ""
        for k in range(len(t1)):
            au = t1[k].split(",")
            y3 = []
            for h in range(len(au)):
                k1 = int(au[h])
                y3.append(aux1[k1])
            resul = int(y3[0])
            for elemento in y3[1:]:
                resul ^= int(elemento)
            ss += str(resul)
            if k != len(t1)-1:
                ss += ","
        # print("{:<2} {:<4} {:<2} {:<7} {:<2} {:<7} {:<2} {:<11} {:<2}".format("|", ent, "|", act[1:], "|", sig[1:], "|", ss, "|"))
        ref.append([ent, act[1:], sig[:len(sig)-1], ss])
        pal += ss
        inicial = sig[:len(sig)-1]
    pal = pal.replace(",", "")
    pal1.append([pal])
    return ref, pal1


def menu_bits(G, t, t1, d, s, w):
    m = "-1"
    ref = []
    clear()
    while m != "0":
        re = ""
        if d != "-1":
            for i in range(int(d)):
                if i == int(d)-1:
                    re += color["rojo"]+"D"+str((i+1))+" "
                else:
                    re += color["rojo"]+"D"+str((i+1))+","
        re += "\n"
        if s != "-1":
            for i in range(int(s)):
                re += color["azul"]+"S"+str((i+1))+": "
                if len(t1) > 0:
                    r1 = ""
                    aux = t1[i].split(",")
                    for j in range(len(aux)):
                        if aux[j] == "0":
                            if j == len(aux)-1:
                                r1 += color["morado"]+"E"+""
                            else:
                                r1 += color["morado"]+"E"+","
                        else:
                            if j == len(aux)-1:
                                r1 += color["morado"]+"D"+aux[j]+""
                            else:
                                r1 += color["morado"]+"D"+aux[j]+","

                    re += r1
                re += " | "
        print(color["cian"], "|:----------------------------:|")
        print(" |   Bienvenido al menu bits    |")
        print(" |:----------------------------:|", color["fin"])
        print(re+"\n")

        print(color["verde"], "1. 8 Bit.")
        print(color["rojo"],  "2. 10 bit.")
        print(color["morado"],  "3. 12 bit.")
        print(color["blanco"], "0. Salir")
        m = input(color["cian"]+"Opcion: ")
        clear()
        if m == "1":
            r = ""
            while len(r) != 8:
                r = input(color["verde"]+"Ingrese la palabra de 8 bits: ")
                clear()
            ref, pal = tabla(t1, d, r, ref)
            printGraph(G, w, ref, pal, d, 8)
            input()
        if m == "2":
            r = ""
            while len(r) != 10:
                r = input(color["verde"]+"Ingrese la palabra de 10 bits: ")
                clear()
            ref, pal = tabla(t1, d, r, ref)
            printGraph(G, w, ref, pal, d, 10)
            input()
        if m == "3":
            r = ""
            while len(r) != 12:
                r = input(color["verde"]+"Ingrese la palabra de 12 bits: ")
                clear()
            ref, pal = tabla(t1, d, r, ref)
            printGraph(G, w, ref, pal, d, 12)
            input()
        if m == "0":
            plt.close(1)
        clear()
