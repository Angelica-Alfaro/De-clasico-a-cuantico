'LIBRERÍA COMPUTACIÓN CUÁNTICA'
'Calculadora números complejos'
#Nota:Las funciones se realizaron sin ningún tipo de redondeo para no descartar ninguna cifra decimal.
import math

'-----------------------------------Operaciones básicas-----------------------------------'

#Suma.(Permite sumar números complejos de la forma a+bi)
#La suma se realiza sumando parte real y parte imaginaría
def sumar(num1,num2):
    a=num1[0]+num2[0]
    b=num1[1]+num2[1]
    return(a,b)

#Resta.(Permite restar números complejos de la forma a+bi)
#La resta se realiza restando parte real y parte imaginaría
def restar(num1,num2):
    a=num1[0]-num2[0]
    b=num1[1]-num2[1]
    return(a,b)

#Multiplicación.(Permite multiplicar números complejos de la forma a+bi)
#La multiplicación se realiza haciendo distrubutividad entre los operandos
def producto(num1,num2):
    a=(num1[0]*num2[0])-(num1[1]*num2[1])
    b=(num1[0]*num2[1])+(num1[1]*num2[0])
    return(a,b)

#Conjugado.(Permite hallar el conjugado de un número complejo de la forma a+bi)
#El conjugado se halla multiplicando por -1 la parte imaginaría
def conjugado(num):
    return(num[0],-1*num[1])

#Modulo.(Permite hallar el módulo de un número complejo de la forma a+bi)
#El módulo se halla sacando la raiz cuadrada de elevar al cuadrado la parte real y el coeficiente imaginario
def modulo(num):
    m=math.sqrt(num[0]**2+num[1]**2)
    return(m)

#División.(Permite hallar la divisón entre números complejos de la forma a+bi)
#la división se realiza elevando al cuadrado el complejo divisor(denominador) y haciendo distributividad entre los operandos(numerador)
def division(num1,num2):
    if num2[0]==0 and num2[1]==0:
        raise ValueError('No es posible dividir por cero!')
    else:
        deno=num2[0]**2+num2[1]**2
        a=(num1[0]*num2[0])+(num1[1]*num2[1])
        b=(num1[1]*num2[0])-(num1[0]*num2[1])
        return(a/deno,b/deno)

#Conversión de representación polar a cartesiana.(Permite la conversión polar a cartesiana de un número complejo de la forma a+bi)
#La conversión se realiza a=pcos(θ) y b=psen(θ)
#El ángulo ingresado es en radianes
def pol_a_car(cord):
    a= cord[0]*math.cos(cord[1])
    b= cord[0]*math.sin(cord[1])
    return(a,b)

#Conversión de representación cartesiana a polar.(Permite la conversión cartesiana a polar de un número complejo de la forma a+bi)
#La conversión se realiza p=módulo y θ=atan(b/a)
#El ángulo retornado es en grados
def car_a_pol(num):
    p=math.sqrt(num[0]**2+num[1]**2)
    θ=fase(num)
    return (p,θ)

#Fase.(Permite hallar la fase de un número complejo de la forma a+bi)
#La fase se halla teniendo en cuenta el cuadrante en donde se encuentran las coordenadas
#El ángulo retornado es en grados
def fase(num):
    f1=math.atan(num[1]/num[0])
    if num[0]<0 and num[1]<0:
        return(180+math.degrees(f1))
    elif num[0]<0:
        return (180+math.degrees(f1))
    elif num[1]<0:
        return(360+ math.degrees(f1))
    else:
        return(math.degrees(f1))

'-----------------------------------Vectores-----------------------------------'

#Adición de vectores.(Permite sumar vectores complejos)
#La adición se realiza sumando componente a componenente los vectores
def sumaVector(v1,v2):
    lista=[]
    if len(v1) != len(v2):
        raise ValueError('Los vectores deben tener el mismo tamaño')
    else:
        for i in range(len(v1)):
            lista.append((sumar(v1[i],v2[i])))
    return(lista)

#Inversa de un vector complejo.(Permite hallar el inverso aditivo de un vector complejo)
#El inverso aditivo se halla multiplicando por -1 el vector
def inversaVector(v1):
    lista=[]
    for i in range(len(v1)):
        a=-1*(v1[i][0])
        b=-1*(v1[i][1])
        lista.append((a,b))
    return lista

#Multiplicación escalar de vectores.(Permite multiplicar un escalar por un vector complejo)
#La multiplicación escalar se halla multiplicando el escalar por cada componente del vector
def escalarVector(escalar,v3):
    lista=[]
    for i in range(len(v3)):
        a,b=producto(escalar,v3[i])
        lista.append((a,b))
    return(lista)

#Distancia entre vectores.(Permite hallar la distancia entre vectores complejso)
#La distancia entre vectores se halla |v2-v1|
v1=[(2,7),(4,-1),(2,-4)]
v2=[(7,8),(2,-8),(1,4)]
def distanciaVector(v1,v2):
    a=0
    b=0
    if len(v1)!= len(v2):
        raise ValueError('los vectores deben tener el mismo tamaño')
    else:
        for i in range(len(v1)):
            a+=(v1[i][0]-v2[i][0])**2
            b+=(v1[i][1]-v2[i][1])**2
        dis=math.sqrt(a+b)
    return (dis)

#Producto interno.(Permite hallar el producto interno entre vectores complejos)
#El producto interno <v1,v2> se hallando la adjunta de  v1 y multiplicando componente a componente v2
def productoInterno(v1,v2):
    if len(v1) != len(v2):
        raise ValueError('Los vectores deben tener el mismo tamaño')
    else:
        newV1=[]
        for x in range(len(v1)):
            newV1.append(conjugado(v1[x]))

        suma=(0,0)
        for i in range(len(newV1)):
            a=producto(newV1[i],v2[i])
            suma=sumar(suma,a)
        return (suma)

#Norma de vector.(Permite hallar la norma de un vector complejo)
#La norma de un vector se halla sacando la raiz de la suma de cada elemento elevado al cuadrado
def normaVector(v1):
    suma=0
    for i in range(len(v1)):
        suma+=(v1[i][0]**2)+(v1[i][1]**2)
    norma=math.sqrt(suma)
    return (norma)

'----------------------------------Matrices---------------------------------'

#Adición de matrices.(Permite sumar matrices complejas)
#La adición se halla sumando las matrices componente a componente
def sumaMatriz(m1,m2):
    lista=[]
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError('Las matrices deben tener la misma dimensión')
    else:
        for i in range(len(m1)):
            lista2=[]
            for j in range(len(m1[0])):
                a=sumar(m1[i][j],m2[i][j])
                lista2.append((a))
            lista.append(lista2)
    return(lista)

#Inversa de matrices.(Permite hallar el inverso aditivo de una matriz compleja)
#El inverso aditivo se halla multiplicando por -1 la matriz
def inversaMatriz(m1):
    lista=[]
    for i in range(len(m1)):
        lista2=[]
        for j in range(len(m1[0])):
            a=-1*(m1[i][j][0])
            b=-1*(m1[i][j][1])
            lista2.append((a,b))
        lista.append(lista2)
    return(lista)

#Multiplicación escalar de matrices.(Permite multiplicar un escalar por una matriz compleja)
#La multiplicación escalar se halla multiplicando el escalar por cada componente de la matriz
def escalarMatriz(escalar,m1):
    lista=[]
    for i in range(len(m1)):
        lista2=[]
        for j in range(len(m1[0])):
            num=producto(escalar,m1[i][j])
            lista2.append((num))
        lista.append((lista2))
    return(lista)

#Matriz transpuesta.(Permite hallar la transpuesta de una matriz compleja)
#La matriz transpuesta se halla cambiando filas por columnas(o viceversa)
def matrizTranspuesta(m1):
    lista=[]
    for j in range(len(m1[0])):
        lista.append([])
        for i in range(len(m1)):
            num=m1[i][j]
            lista[j].append(num)
    return(lista)

#Matriz conjugada.(Permite hallar la conjugada de una matriz compleja)
#La matriz conjugada se halla multiplicando por -1 la parte imaginaría de cada componente de la matriz
def matrizConjugada(m1):
    lista=[]
    for i in range(len(m1)):
        lista2=[]
        for j in range(len(m1[0])):
            num=conjugado(m1[i][j])
            lista2.append((num))
        lista.append((lista2))
    return (lista)

#Matriz adjunta.(Permite hallar la adjunta o daga de una matriz compleja)
#La matriz adjunta se halla obteniendo la transpuesta y la conjugada de la matriz
def matrizAdjunta(m1):
    transpuesta=matrizTranspuesta(m1)
    adjunta=matrizConjugada(transpuesta)
    return (adjunta)

#Producto de matrices.(Permite multiplicar dos matrices complejas)
#La mulptiplicación matricial se halla sumando la multiplicación de las filas de la matriz A con las columnas de la matriz B
def productoMatriz(m1,m2):
    lista=[]
    if len(m1[0]) != len(m2):
        raise ValueError('Las matrices no tienen dimensiones compatibles')
    else:
        for i in range(len(m1)):
            lista2=[]
            for j in range(len(m2[0])):
                suma=(0,0)
                for k in range(len(m2)):
                    a=producto(m1[i][k],m2[k][j])
                    suma=sumar(suma,a)
                lista2.append(suma)
            lista.append(lista2)
        return (lista)

#Acción de matriz sobre vector.(Permite multiplicar una matriz compleja por un vector complejo)
#La acción de una matriz sobre un vector se halla multiplicando de las fila de la matriz con la columna del vector
def accionMatriz(m1,v1):
    lista = []
    if len(m1[0]) != len(v1):
        raise ValueError('La matriz y el vector no tienen dimensiones compatibles')
    else:
        for i in range(len(m1)):
            for j in range(len(v1)):
                suma=(0,0)
                for k in range(len(v1)):
                    a=producto(m1[i][k],v1[k])
                    suma=sumar(suma, a)
            lista.append(suma)
        return (lista)

#¿Es la matriz una matriz unitaria?.(Permite revisar si la matriz compleja ingresada es unitaria)
#Para verificar que sea unitaría se multiplica A por A adjunta lo que debería ser igual a I
def matrizUnitaria(m1):
        m2=matrizConjugada(matrizTranspuesta(m1))
        m3=[]
        m1=productoMatriz(m1,m2)
        n=m1[0][0]
        for i in range(len(m1)):
            lista=[]
            for j in range(len(m1)):
                if i == j:
                    lista.append((1,0))
                    m1[i][j] = division(m1[i][j],n)
                else:
                    lista.append((0,0))
            m3.append(lista)
        return (m3 == m1)

#¿Es un matriz una matriz hermitiana?.(Permite revisar si la matriz conpleja ingresada es hermitiana)
#Para verificar que sea hermitiana A debe ser igual a A adjunta
def matrizHermitiana(m1):
    m2=matrizConjugada(matrizTranspuesta(m1))
    return (m1 == m2)

#Producto tensorial.(Permite realizar el producto tensorial de matrices complejas)
#El producto tenorial se halla multiplicando un componente de A por todos los componentes de B

def productoTensor(m1,m2):
    lista=[]
    filas=len(m1)*len(m2)
    columnas=len(m1[0])*len(m2[0])
    for x in range(filas):
        lista2=[]
        lista.append(lista2)
        for y in range(columnas):
            lista2.append([])
    for i in range(filas):
        for j in range(columnas):
            a=i//len(m2)
            b=j//len(m2[0])
            res=escalarMatriz(m1[a][b],m2)
            a2=i%len(m2)
            b2=j%len(m2[0])
            lista[i][j]=res[a2][b2]
    return(lista)
    










