
def cargar_lista():
    lista=[]
    veces=input("ingrese cuantos numeros va a ingresar")
    for i in range(int(veces)):
        valor=float(input("ingrese numero a comparar"))
        lista.append(valor)
    return lista

def maximo(lista):
    long=len(lista)
    max=lista[0]
    for i in range(long):
        if lista[i]>max:
            max=lista[i]
    print(f"el mayo es {max}")

def suma(listaA):
    acum1=0
    for num in listaA:
        acum1+=num
    print(f"la suma de la lista es {acum1}")


def suma_vectores(listaA, listaB):
    if len(listaA)==len(listaB):
        nueva_lista=[]
        for n,m in zip(listaA, listaB):
            nueva_lista.append(n+m)
        print(f"las listas eran de la misma longitud, asi que las sumamos. su nueva lista es{nueva_lista}")
    else:
        print("las listas eran de distinta longitud")

def contar_vocales(oraciones):
    oraciones=oraciones.split()
    vocales="aeiouáéíóúü"
    cont=0
    for palabra in oraciones:
        for letra in palabra:
            if letra in vocales:
                cont+=1
    print(f"lo que ingresaste tiene {cont} vocales")
        
def contar_consonantes(oraciones):
    oraciones=oraciones.split()
    vocales="aeiouáéíóúü"
    cont=0
    for palabra in oraciones:
        for letra in palabra:
            if letra.isalpha()  and letra not in vocales:
                cont+=1
    print(f"lo que ingresaste tiene {cont} consonantes")

def calcular_potencia(k,x):
    rdo = 1
    while x > 0:
        rdo *= k
        x -= 1
    print(f"el resultado es {rdo}")

def calcular_digitos(a):
    cont=0
    while a!=0:
        a%10
        cont+=1
        a=a//10
    print(f"el numero tiene {cont} digitos")

def capicua(numero):
    l_numero=list(numero)
    rl_numero=l_numero[::-1]
    if l_numero==rl_numero:
        print(f"el numero {numero} es capicua")
    else:
        print(f"el numero {numero} no es capicua")

def crear_matriz():
    filas=int(input("ingrese la cantidad de filas que quiere en la matriz"))
    columnas=int(input("ingrese la cantidad de columnas que debe tener la matiz"))
    matriz=[]
    for f in range (filas):
        fila=[]
        for c in range (columnas):
            numero=float(input(f"valor para fila {f+1}, columna {c+1}"))
            fila.append(numero)
        matriz.append(fila)
    print("matriz creada")
    print(matriz)
    return matriz, filas, columnas

def sumar_matriz(matrizA, matrizB, filas, columnas):
    rdo_matriz=[]
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            suma = matrizA[i][j] + matrizB[i][j]
            fila_suma.append(suma)
        rdo_matriz.append(fila_suma)
    for fila in rdo_matriz:
        print(fila)
    return rdo_matriz

def producto_matriz(matrizA,matrizB,filas,columnas):
    rdo_matriz=[]
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            suma = matrizA[i][j] * matrizB[i][j]
            fila_suma.append(suma)
        rdo_matriz.append(fila_suma)
    for fila in rdo_matriz:
        print(fila)
    return rdo_matriz








    
    

        







        
