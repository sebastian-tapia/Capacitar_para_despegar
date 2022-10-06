#Ejercio 1 
#Definí una función pozo_vacio, que nos indique si el pozo está en 0:
#pozo=0
def pozo_vacio():
    global pozo
    return pozo==0

#Ejercicio 2
#Sabemos que para llegar al Chaltén necesitamos por persona 3000 pesos
#Hacé una función cuanta_gente_viaja_al_chalten que retorne, según el monto del pozo, la cantidad de personas que pueden viajar. ¡Tené en cuenta que media persona no puede viajar! 😛

#pozo=9000
def cuanta_gente_viaja_al_chalten():
    global pozo
    return int(pozo/3000)
#uso la funcion int para obtener el entero del resultado (borrar los decimales)



#Ejercicio 3
#¡A quién no le gusta tener opciones! Sabemos cuánto nos sale por persona el viaje al Chaltén y nos pasaron en la agencia de viaje los valores por persona a Tilcara ($3500 por persona) y Mendoza ($2500 por persona).


#Definí una función hasta_donde_llegamos que según la cantidad de personas que van a viajar, nos devuelva un string con el nombre de la ciudad a la que podemos llegar. Y si no nos alcanza, que nos recomiende seguir ahorrando:

#pozo=2600
boletoTilcara=3500
boletochalten= 3000
boletoMendoza=2500

def hasta_donde_llegamos(personas):
    global pozo
    global boletoTilcara
    global boletochalten
    global boletoMendoza
    if  pozo>=(personas*boletoTilcara):
        return "Tilcara"
    elif pozo>=(personas*boletochalten):
        return "CHAlten"
    elif pozo>=(personas*boletoMendoza):
        return "Mendoza"
    else:
        return "siguan  ahorrando "

#ejercicio 4
#Definí un procedimiento llamada aportar_al_pozo, que tome como parámetro un aporte (monto de plata) y actualice el monto del pozo:

#pozo=0
def aportar_al_pozo(monto):
    global pozo
    pozo+=monto

#Ejercicio 5
##¿Pero qué pasa si alguien se quiere bajar? La agencia nos devuelve solo 500, sin importar el monto inicial (asumimos que las personas deben aportar inicialmente más de 500)

#Definí el procedimiento darse_de_baja, que descuenta del pozo 500

def darse_de_baja():
    global pozo
    pozo-=500


#EJercicio 6 
#Por una nueva reglamentación, todos pozos de dinero que tengan más de $15000, deberán tributar un impuesto (llamado I.V.G.: Impuesto a las Variables Globales) del 1% si el pozo. Por la misma reglamentación, el valor máximo del impuesto será de $500.

"""Definí:

    1.una función calcular_monto_ivg, que indique el valor del impuesto I.V.G. que el pozo debe pagar;

    2.un procedimiento aplicar_ivg, que descuente del pozo el valor del impuesto que corresponda."""


pozo=18000


def calcular_monto_ivg(): 
    global pozo
    unPorcientoPozo=int(pozo/100)

    if pozo>15000 and unPorcientoPozo>=500:
        #comparo si el pozo es mayor a 15000 Y Si el 1% del pozo es mayor o igual a 500
        #si el 1% del pozo es mayor a 500 devuelve el el impuestomaximo
        return 500 
    elif pozo>15000 and unPorcientoPozo<500:
        #comparo si el pozo es mayor a 15k Y si el 1% del pozo es menor a 500
        #si es menor a 500 descuento del pozo el valor del impuesto que corresponda
        return unPorcientoPozo
ivg=0
def aplicar_ivg():
    global pozo
    global ivg
    
    if ivg<3:
        pozo-=calcular_monto_ivg()
    ivg+=1

#17820
#17642
#17466
#ejercicio 7
#Otra nueva reglamentación! Después de algunas quejas contra el I.V.G. 😡, se determinó que ningún pozo deberá pagar el impuesto más de tres veces. En otras palabras, al aplicar el impuesto, sólo deberemos descontar del pozo su monto si se aplicó hasta 3 veces. Ejemplo:

"""

    Modificá el procedimiento aplicar_ivg para que refleje estos cambios de reglamentación.

    💡 Sugerencia: para poder hacer estos cambios en la aplicación del impuesto I.V.G., quizás te convenga agregar nuevas variables globales (qué ironía 😜).
"""



#Ejercicio 8
#Parece que la recaudación no anduvo tan bien y la gente se quiere retirar del pozo 😥️. Así que definimos una nueva regla: si no llegamos a un objetivo mínimo de $1000, el pozo vuelve a cero (porque se devolverá la plata a sus participantes 💸️)
#Definí un procedimiento volver_a_empezar, tal que si tenemos menos de $1000 en el pozo, lo vuelva a cero.

def volver_a_empezar():
    global pozo
    if pozo<1000:
        pozo=0


#Ejercicio 9 
#En la clase están votando al delegado que representará al curso. Pero como esta es una clase de pensamiento computacional, vamos a crear un procedimiento declarar_delegado que asigne en la variable global delegado el nombre de la persona que tenga más votos:
delegado=""
def declarar_delegado(alumno1,pntsAlumno1,alumno2,pntsAlumno2):
    global delegado
    if pntsAlumno1 > pntsAlumno2:
        delegado=alumno1
    else:
        delegado=alumno2
#EJercicio 10
#En la comisión E están creando el registro histórico de delegados/as del curso. Para ellos quieren ahora un procedimiento que les permita registrar los/las delegados/as del curso en cada año en la variable global delegados_por_anio


delegados_por_anio=[]
anioA=2022
anioB=2024
def registrar_delegado_del_anio(alumno, anio):
    global delegados_por_anio
    global anioA
    global anioB
    if anio>anioA and anio<anioB:
        delegados_por_anio+=[alumno +" "+str(anio)]
        anioA+=1
        anioB+=1

