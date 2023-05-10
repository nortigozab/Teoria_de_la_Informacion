import os
import math
m = "e"
u = [0.0, 0, 0]
d = -1
e = 0
# fin0,amarillo1,verde2,rojo3,morado4,cian5,azul6,blanco7
color = ["\033[0;m", "\033[;33m", "\033[;32m",
         "\033[;31m", "\033[;35m", "\033[;36m", "\033[;34m","\033[;37m"]
ty = ""  # tiempo
u1 = [["dBT", "Tera ", "TeraWatts ", 12], ["dBG", "Giga ", "GigaWatts ", 9], ["dBM", "Mega ", "MegaWatts ", 6], ["dBK", "Kilo ", "KiloWatts ", 3], [
    "dBW", "Watt ", "Watts     ", 0], ["dBm", "mili ", "miliWatts ", -3], ["dBu", "micro", "microWatts", -6], ["dBn", "nano ", "nanoWatts ", -9], ["dBp", "pico ", "picoWatts ", -12]]
# funcion para limpiar pantalla

def validar_numero(n):
	try:
		float(n)
		return True
	except:
		return False
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# funcion para ingresar valor inicial


def ingresar():
    ty = ""
    q="w"
    while validar_numero (q)==False:
        q = input(color[1]+"Ingrese valor: ")
        clear()        
    u[0] = float(q)
    r = -1
    while r < 1 or r > 2:
        clear()
        print(color[1]+"1. Para ingresar Señal."+color[0])
        print(color[1]+"2. Para ingresar potencia."+color[0])
        r = input(color[1]+"Ingrese opcion: ")
        while validar_numero(r)==False:
            clear()
            print(color[1]+"1. Para ingresar Señal."+color[0])
            print(color[1]+"2. Para ingresar potencia."+color[0])
            r = input(color[1]+"Ingrese opcion: ")
        r=float(r)
    u[1] = r
    if u[1] == 1:
        r = -1
        while r < 1 or r > 9:
            clear()
            for i in range(len(u1)):
                print(color[1], (i+1), ".", u1[i][0], "."+color[0])
            r = input(color[1]+"Ingrese opcion: ")
            while validar_numero(r)==False:
                clear()
                for i in range(len(u1)):
                    print(color[1], (i+1), ".", u1[i][0], "."+color[0])
                r = input(color[1]+"Ingrese opcion: ")
            r=float(r)
        u[2] = int(r-1)
        ty = "->i: "+str(u[0])+u1[u[2]][0]
    elif u[1] == 2:
        r = -1
        while r < 1 or r > 9:
            clear()
            for i in range(len(u1)):
                print(color[1], i+1, ".", u1[i][2], "."+color[0])
            r = input(color[1]+"Ingrese opcion: ")
            while validar_numero(r)==False:
                clear()
                for i in range(len(u1)):
                    print(color[1], i+1, ".", u1[i][2], "."+color[0])
                r = input(color[1]+"Ingrese opcion: ")
            r=float(r)
        u[2] = int(r-1)
        ty = "->i: "+str(u[0])+" "+u1[u[2]][2]
    return ty
# funcion para mostrar tabla de conversiones


def tablaUnidades(u):
    if u[1] == 2:
        q = u[0]
        z = math.log10(float(u[0])/1)*10
    elif u[1] == 1:
        z = u[0]
        q = (10**(u[0]/10))
    q1 = []
    q2 = []
    z1 = []
    z2 = []
    for i in range(len(u1)):
        if i < u[2]:
            q2.append(-(3*(u[2]-i)))
        if i > u[2]:
            q2.append((3*-(u[2]-i)))
        if i == u[2]:
            q2.append(0)
    for i in range(len(u1)):
        if i < u[2]:
            z2.append(-(30*(u[2]-i)))
        if i > u[2]:
            z2.append((30*-(u[2]-i)))
        if i == u[2]:
            z2.append(0)
    for i in range(len(u1)):
        q1.append(format(q*(1*10**q2[i]), '.1E'))
        z1.append(str(round((z+z2[i]), 5)))
    m = -1
    n = -1
    for i in range(len(u1)):
        if len(z1[i]) >= m:
            m = len(str(z1[i]))
        if len(q1[i]) >= n:
            n = len(str(q1[i]))
    print(color[7],"   :-----:-------------:---------:-----------:       :-----:-----------:--------------:-----------:",color[0]) 
    print (color[7],"{:<2} {:<2} {:<2} {:<2} {:<10} {:<2} {:<6} {:<2} {:<8} {:<2} {:<1} {:<2} {:<2} {:<2} {:<3} {:<7} {:<4} {:<9} {:<2} {:<8} {:<2} {:<1}".format('','|','#','|','Valor','|','Unidad','|','Valor_U','|','','','|','#','|','Valor','|','Unidad','|','Valor_U','|',''),color[0])
    print(color[7],"   :-----:-------------:---------:-----------:       :-----:-----------:--------------:-----------:",color[0]) 
    for i in range(len(u1)):
        if i == u[2]:
            print (color[2],"{:<2} {:<2} {:<2} {:<2} {:<10} {:<2} {:<6} {:<2} {:<8} {:<2} {:<1} {:<2} {:<2} {:<2} {:<3} {:<7} {:<2} {:<11} {:<2} {:<8} {:<2} {:<1} ".format('->','|',i,'|',z1[i],'|',u1[i][0],'|',u1[i][1],'|','','->','|',i,'|',q1[i],'|',u1[i][2],'|', u1[i][1],'|',''),color[0])
        else:
            print (color[7],"{:<2} {:<2} {:<2} {:<2} {:<10} {:<2} {:<6} {:<2} {:<8} {:<2} {:<1} {:<2} {:<2} {:<2} {:<3} {:<7} {:<2} {:<11} {:<2} {:<8} {:<2} {:<1} ".format('','|',i,'|',z1[i],'|',u1[i][0],'|',u1[i][1],'|','','','|',i,'|',q1[i],'|',u1[i][2],'|', u1[i][1],'|',''),color[0])
    print(color[7],"   :-----:-------------:---------:-----------:       :-----:-----------:--------------:-----------:",color[0]) 
    input()
# funcion para dar ganancia a la señal


def ganancia(u, ty):
    g = ["w","", 0.0]
    r = -1
    g[1] = input(color[2]+"Ingrese valor: ")
    while validar_numero(g[1])==False:
        clear()
        g[1] = input(color[2]+"Ingrese valor: ")
    while r < 0 or r > 2:
        clear()
        print(color[2], "1.", float(g[1]), "dB.", color[0])
        print(color[2], "2.", float(g[1]), " veces.", color[0])
        print("0. Regresar")
        r = input(color[2]+"\nIngrese opcion: ")
        while validar_numero(r)==False:
            clear()
            print(color[2], "1.", float(g[1]), "dB.", color[0])
            print(color[2], "2.", float(g[1]), " veces.", color[0])
            print("0. Regresar")
            r = input(color[2]+"\nIngrese opcion: ")
        r=float(r)
    print("|:-------------------------------------------:|")
    if r == 1:
        if u[1] == 1:
            g[2] = u[0]+float(g[1])
            print(color[2], u[0], u1[u[2]][0], "+", g[1],
                  "dB: ", g[2], u1[u[2]][0], color[0])
            ty = ty+"|->G: "+str(g[1])+"dB: "+str(g[2])+u1[u[2]][0]
        else:
            g[2] = ((math.log10(float(u[0])/1)*10))+float(g[1])
            g[2] = (10**(float(g[2])/10))
            print(color[2], g[1], "dB a veces: ", round(
                (10**(float(g[1])/10)), 4), color[0])
            print(color[2], u[0], u1[u[2]][2], "*", round((10**(float(g[1])/10)), 4),
                  " veces: ", round(g[2], 4), u1[u[2]][2], color[0])
            ty = ty+"|->G: "+str(g[1])+"dB: " + \
                str(round(g[2], 2))+" "+u1[u[2]][2]
        u[0] = round(g[2], 4)
        input()
    elif r == 2:
        s = (math.log10(float(g[1])/1)*10)
        if u[1] == 1:
            g[2] = u[0]+s
            print(color[2], g[1], " veces a dB: ", round(s, 4), color[0])
            print(color[2], u[0], u1[u[2]][0], "+", round(s, 4),
                  " dB: ", round(g[2], 2), u1[u[2]][0], color[0])
            ty = ty+"|->G: "+str(g[1])+" veces: " + \
                str(round(g[2], 4))+u1[u[2]][0]
        else:
            g[2] = ((math.log10(float(u[0])/1)*10))+float(s)
            g[2] = (10**(float(g[2])/10))
            print(color[2], u[0], u1[u[2]][2], "*", g[1],
                  "veces: ", round(g[2], 2), u1[u[2]][2], color[0])
            ty = ty+"|->G: "+str(g[1])+" veces: " + \
                str(round(g[2], 4))+" "+u1[u[2]][2]
        u[0] = round(g[2], 4)
        input()
    return (u, ty)
# funcion para dar perdida a la señal


def perdida(u, ty):
    p = ["w","", 0.0]
    r = -1
    p[1] = input(color[3]+"Ingrese valor: ")
    while validar_numero(p[1])==False:
        clear()
        p[1] = input(color[3]+"Ingrese valor: ")
    while r < 0 or r > 2:
        clear()
        print(color[3]+"1.", float(p[1]), "dB."+color[0])
        print(color[3]+"2.", float(p[1]), " veces."+color[0])
        print("0. Regresar")
        r = input(color[3]+"\nIngrese opcion: ")
        while validar_numero(r)==False:
            clear()
            print(color[3]+"1.", float(p[1]), "dB."+color[0])
            print(color[3]+"2.", float(p[1]), " veces."+color[0])
            print("0. Regresar")
            r = input(color[3]+"\nIngrese opcion: ")
        r=float(r)
    print("|:-------------------------------------------:|")
    if r == 1:
        if u[1] == 1:
            p[2] = u[0]-float(p[1])
            print(color[3], u[0], u1[u[2]][0], "-", p[1],
                  "dB: ", round(p[2], 2), u1[u[2]][0], color[0])
            ty = ty+"|->P: "+str(p[1])+"dB: "+str(p[2])+u1[u[2]][0]
        else:
            p[2] = ((math.log10(float(u[0])/1)*10))-float(p[1])
            p[2] = (10**(float(p[2])/10))
            print(color[3], p[1], "dB a veces: ",
                  (10**(float(p[1])/10)), color[0])
            print(color[3], u[0], u1[u[2]][2], "/", round((10**(float(p[1])/10)), 4),
                  "veces: ", round(p[2], 2), u1[u[2]][2], color[0])
            ty = ty+"|->P: "+str(p[1])+"dB: " + \
                str(round(p[2], 4))+" "+u1[u[2]][2]
        u[0] = p[2]
        input()
    elif r == 2:
        s = (math.log10(float(p[1])/1)*10)
        if u[1] == 1:
            p[2] = u[0]-s
            print(color[3], p[1], "veces a dB: ", round(s, 5), " dB", color[0])
            print(color[3], u[0], u1[u[2]][0], "-", round(s, 5),
                  " dB: ", round(p[2], 2), u1[u[2]][0], color[0])
            ty = ty+"|->P: "+str(p[1])+" veces: " + \
                str(round(p[2], 4))+u1[u[2]][0]
        else:
            p[2] = ((math.log10(float(u[0])/1)*10))-float(s)
            p[2] = (10**(float(p[2])/10))
            print(color[3], u[0], u1[u[2]][2], "/ ", p[1],
                  " veces", round(p[2], 2), u1[u[2]][2], color[0])
            ty = ty+"|->P: "+str(p[1])+" veces: " + \
                str(round(p[2], 4))+" "+u1[u[2]][2]
        u[0] = round(p[2], 4)
        input()
    return (u, ty)
# funcion para ver la relacion señal a ruido


def senal_ruido(u, ty):
    if u[1] == 1:
        r = -1
        p = input(color[4]+"Ingrese Valor: ")
        while validar_numero(p)==False:
            clear()
            p = input(color[4]+"Ingrese Valor: ")
        while r < 0 or r > 2:
            clear()
            print(color[4]+"1.", float(p), u1[u[2]][0], color[0])
            print(color[4]+"2.", float(p), " ", u1[u[2]][2], color[0])
            print("0. regresar")
            r = input(color[4]+"\nIngrese opcion: ")
            while validar_numero(r)==False:
                clear()
                print(color[4]+"1.", float(p), u1[u[2]][0], color[0])
                print(color[4]+"2.", float(p), " ", u1[u[2]][2], color[0])
                print("0. regresar")
                r = input(color[4]+"\nIngrese opcion: ")
            r=float(r)
        print("|:-------------------------------------------:|")
        if r == 1:
            sr = u[0]-float(p)
            print(color[4], "Relacion señal a ruido: ps-pr: ",
                  u[0], u1[u[2]][0], " - ", float(p), u1[u[2]][0], ": ", sr, "dB", color[0])
            sr1 = round((1/(10**(sr/10))), 6)
            if sr1 > 1:
                print(color[4], u[0], u1[u[2]][0], " es N:", sr1,
                      "xS veces mayor que la señal ", color[0])
                ty = ty+"|->N: "+str(float(p))+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            elif sr1 <= 1:
                print(color[4], u[0], u1[u[2]][0], " es N:", sr1,
                      "xS veces menor que la señal", color[0])
                ty = ty+"|->N: "+str(float(p))+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces menor que Ps"
            input()
        elif r == 2:
            s1 = u[0]
            s2 = round(((math.log10(float(p)/1)*10)), 5)
            sr = s1-s2
            sr1 = round((1/(10**(sr/10))), 6)
            print(color[4], "Relacion señal a ruido: ps-pr: ", s1,
                  u1[u[2]][0], " - ", s2, u1[u[2]][0], ": ", round(sr, 6), "dB", color[0])
            if sr1 > 1:
                print(color[4], s1, u1[u[2]][0], " es N:", sr1,
                      "XS veces mayor que la señal", color[0])
                ty = ty+"|->N: " + \
                    str(s2)+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            elif sr1 <= 1:
                print(color[4], s1, u1[u[2]][0], " es ", sr1,
                      " veces menor que la señal", color[0])
                ty = ty+"|->N: " + \
                    str(s2)+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            input()
    else:
        r = -1
        p = input(color[4]+"Ingrese Valor: ")
        while validar_numero(p)==False:
            clear()
            p = input(color[4]+"Ingrese Valor: ")
        while r < 0 or r > 2:
            clear()
            print(color[4]+"1.", float(p), u1[u[2]][0], color[0])
            print(color[4]+"2.", float(p), " ", u1[u[2]][2], color[0])
            print("0. regresar")
            r = input(color[4]+",'\nIngrese opcion: ")
            while validar_numero(r)==False:
                clear()
                print(color[4]+"1.", float(p), u1[u[2]][0], color[0])
                print(color[4]+"2.", float(p), " ", u1[u[2]][2], color[0])
                print("0. regresar")
                r = input(color[4]+",'\nIngrese opcion: ")
            r=float(r)
        print("|:-------------------------------------------:|")
        if r == 1:
            s1 = round(((math.log10(float(u[0])/1)*10)), 5)
            s2 = round(float(p), 5)
            sr = s1-s2
            sr1 = round((1/(10**(sr/10))), 6)
            print(color[4], "Relacion señal a ruido: ps-pr: ", s1,
                  u1[u[2]][0], " - ", s2, u1[u[2]][0], ": ", round(sr, 6), "dB", color[0])
            if sr1 > 1:
                print(color[4], s1, u1[u[2]][0], " es N:", sr1,
                      " veces mayor que la señal", color[0])
                ty = ty+"|->N: " + \
                    str(s2)+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            elif sr1 <= 1:
                print(color[4], s1, u1[u[2]][0], " es N:", sr1,
                      " veces menor que la señal", color[0])
                ty = ty+"|->N: " + \
                    str(s2)+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            input()
        elif r == 2:
            s1 = round(((math.log10(float(u[0])/1)*10)), 5)
            s2 = round(((math.log10(float(p)/1)*10)), 5)
            sr = s1-s2
            sr1 = round((1/(10**(sr/10))), 6)
            print(color[4], "Relacion señal a ruido: ps-pr: ", s1,
                  u1[u[2]][0], " - ", s2, u1[u[2]][0], ": ", round(sr, 6), "dB", color[0])
            if sr1 > 1:
                print(color[4], s1, u1[u[2]][0], " es N:", sr1,
                      " veces mayor que la señal", color[0])
                ty = ty+"|->N: " + \
                    str(s2)+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            elif sr1 <= 1:
                print(color[4], s1, u1[u[2]][0], " es N:", sr1,
                      " veces menor que la señal", color[0])
                ty = ty+"|->N: " + \
                    str(s2)+"dB"+" :Ps-Pr: "+str(sr) + \
                    "dB y es: N:"+str(sr1)+" veces mayor que Ps"
            input()
    return ty


def resistencia(u, ty):
    p = 0
    z1 = []
    z2 = []
    z = 0
    r = 0
    if u[2] != 4:
        if u[1] == 1:
            z = u[0]
        else:
            z = math.log10(float(u[0])/1)*10
        for i in range(len(u1)):
            if i < u[2]:
                z2.append(-(30*(u[2]-i)))
            if i > u[2]:
                z2.append((30*-(u[2]-i)))
            if i == u[2]:
                z2.append(0)
        for i in range(len(u1)):
            z1.append(str(round((z+z2[i]), 5)))
        p = 10**(float(z1[4])/10)
    else:
        p = u[2]
    r = input(color[5]+"Ingrese valor de la resistencia: ")
    while validar_numero(r)==False:
        clear()
        r = input(color[5]+"Ingrese valor de la resistencia: ")
    print("|:-------------------------------------------:|")
    print(color[5], u[0], u1[u[2]][0], " en watt es: ",
          format(p, '.1E'), u1[u[2]][2], color[0])
    print(color[5], "V: ", round(math.sqrt(p*int(r)), 4), color[0])
    rp = format(p, '.1E')
    ty += "|->R: "+"sqrt("+rp + "*" + str(r) + ") V:" + \
        str(round(math.sqrt(p*int(r)), 4))
    input()
    return ty


def imprimirpy(t):
    x = t.split("|")
    te = ""
    # fin0,amarillo1,rojo2,verde3,morado4,cian5
    for i in range(len(x)):
        if x[i][2] == "i":
            te += color[1]+x[i]+color[0]
        elif x[i][2] == "G":
            te += " "+color[2]+x[i]+color[0]
        elif x[i][2] == "P":
            te += " "+color[3]+x[i]+color[0]
        elif x[i][2] == "N":
            te += " "+color[4]+x[i]+color[0]
        elif x[i][2] == "R":
            te += " "+color[5]+x[i]+color[0]
    print(te)


# menu principal
while m != "0":
   # fin0,amarillo1,verde2,rojo3,morado4,cian5,amarillo-blanco6,verde-blanco7,rojo-blanco8,morado-blanco9,cian-blanco10,
    if m != "e" and e != 0:
        print(color[0])
        print("|:------------------:|")
        print("| Bienvenido al menu |")
        print("|:------------------:|\n")
        imprimirpy(ty)
        if u[1] == 1:
            print("\n", "Valor Ingresado: ", u[0], u1[u[2]][0], " o ", round(
                (10**(float(u[0])/10)), 5), u1[u[2]][2])
        elif u[1] == 2:
            print("\n", "Valor ingresado: ", round(u[0], 5), u1[u[2]][2], " o ", round(
                ((math.log10(float(u[0])/1)*10)), 4), u1[u[2]][0])
        print("\n"+color[1]+"1. Ingresar valor. "+color[0])
        print("2. Tabla de conversiones. ")
        print(color[2]+"3. Ingresar Ganancia. "+color[0])
        print(color[3]+"4. Ingresar Perdida. "+color[0])
        print(color[4]+"5. Relacion Señal a Ruido. "+color[0])
        print(color[5]+"6. Resistencia. "+color[0])
        print("0. Salir. ")
        m = input(color[6]+"Ingrese opcion: ")
        clear()
        if m == "1":
            ty = ingresar()
            e = 1
        elif m == "2":
            tablaUnidades(u)
        elif m == "3":
            u, ty = ganancia(u, ty)
        elif m == "4":
            u, ty = perdida(u, ty)
        elif m == "5":
            ty = senal_ruido(u, ty)
        elif m == "6":
            ty = resistencia(u, ty)
    else:
        clear()
        print(color[0])
        print("|:------------------:|")
        print("| Bienvenido al menu |")
        print("|:------------------:|")
        print("\n"+color[1]+"1. Ingresar valor. "+color[0])
        print("0. Salir")
        m = input(color[6]+"\nIngrese opcion: ")
        clear()
        if m == "1":
            ty = ingresar()
            e = 1
    clear()
