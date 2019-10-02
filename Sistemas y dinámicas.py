'EL SALTO DE LO CLÁSICO A LO CUÁNTICO'
'Sistemas y sus dinámicas'
#Nota:Es necesario importar la calculadora de números complejos.
import ComplejosCal
import math

'-------------------------Sistemas-----------------------------------------'

#Sistema y sus dinámicas.
def sistemas(dinamica,matriz,vector,click):
    
    #Permite determinar si los datos corresponden a una dinámica clásica determinista.
    if dinamica == 'determinista':
        validar=True
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j][1]!=0 and (matriz[i][j][0]!=1 or matriz[i][j][0]!=0):
                    validar=False
                    break
                break
        if validar:            
            determinista(matriz,vector,click)
        else:
            print('Los datos no corresponden a una dinámica determinista')
            
            
    #Permite determinar si los datos corresponden a una dinámica probabilística.  
    elif dinamica == 'probabilistica':
        validar=True
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j][1]!=0 and (matriz[i][j][0]==1 or matriz[i][j][0]==0):
                    validar=False
                    break
                break
        if validar:            
            probabilistica(matriz,vector,click)
        else:
            print('Los datos no corresponden a una dinámica probabilística')
            
            
    #Permite determinar si los datos corresponden a una dinámica cuántica. 
    elif dinamica == 'cuantica':
        validar=True
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if (matriz[i][j][0]!=0 and matriz[i][j][1]==0 or matriz[i][j][1]!=0 ):
                    validar=False
                    break
        if validar:            
            cuantica(matriz,vector,click)
        else:
            print('Los datos no corresponden a una dinámica cuantica')


        
'-----------------------Determinista---------------------------------------'

#Dinámicas desde el punto de vista clásico determinista
def determinista(m,v,t):
    
    # Ciclo para el cálculo de las acciones
    for t in range(t):
        v = ComplejosCal.productoMatriz(m, v)

         
    print('Estado final')
    print(v)
    print(" ")
    print('Evolución del sistema')
    #Permite mostrar la evolución del sistema
    for i in range(len(v)):
        grafico= '*' * (v[i][0][0]*10)
        print(i,grafico)

'-------------------Probabilístico---------------------------------'

#Dinámicas desde el punto de vista probabilistico
def probabilistica(m,v,t):
    
    # Ciclo para el cálculo de las acciones
    for t in range(t):
        v = ComplejosCal.productoMatriz(m, v)

         
    print('Estado final')
    print(v)
    print(" ")
    print('Evolución del sistema')    
    #Permite mostrar la evolución del sistema
    for i in range(len(v)):
        grafico= '*' * round((v[i][0][0]*10))
        print(i,grafico)

'---------------------Cuántico-------------------------------------'

#Dinámicas desde el punto de vista probabilistico
def cuantica(m,v,t):
    
    # Ciclo para el cálculo de las acciones de manera cuántica
    for t in range(t):
        v = ComplejosCal.productoMatriz(m, v)
    print('Sistema cuántico')

    #Permite mostrar la evolución del sistema
    for i in range(len(v)):
        grafico= '*' * round((v[i][0][0]*10))
        print(i,grafico)
    
    # Ciclo para el cálculo de las acciones de manera probabilística
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = ComplejosCal.producto(m[i][j],ComplejosCal.conjugado(m[i][j]))
    for i in range(len(v)):
        for j in range(len(v[0])):
            v[i][j] = ComplejosCal.producto(v[i][j],ComplejosCal.conjugado(v[i][j]))

    print(" ")
    # Ciclo para el cálculo de las acciones
    for t in range(t):
        v = ComplejosCal.productoMatriz(m, v)
    print('Sistema probabilístico')

    
    #Permite mostrar la evolución del sistema
    for i in range(len(v)):
        grafico= '*' * round((v[i][0][0]*10))
        print(i,grafico)
        

'-------------------Sistema ensamblado---------------------------------------'

#Permite ensamblar dos sistemas
def ensamblado(m1,v1,m2,v2,t):
    #Vector de estado inicial
    V = ComplejosCal.productoTensor(v1,v2)

    #Matriz estado inicial
    M = ComplejosCal.productoTensor(m1,m2)

    # Ciclo para el cálculo de las acciones
    for i in range(t):
        V = ComplejosCal.productoMatriz(M,V)
        
    print('Estado final')
    print(V)
    print(" ")
    print('Evolución del sistema')
    #Permite mostrar la evolución del sistema
    for i in range(len(V)):
        grafico= '*' * round((V[i][0][0]*10))
        print(i,grafico)

'-------------------Experimento doble rendija--------------------------------'
            
'--------------------------Rendija probabilística----------------------------'

#Experimento doble rendija probabilístico
def rendijaProba(numRendijas,numBlancos,vectorProba):
    #Datos necesarios
    paredes=numRendijas+1
    lonMatriz=(numBlancos*paredes)+(2*numRendijas)+1
    Matriz=[]

    #Vector estado inicial
    VI=[]
    for i in range(lonMatriz):
        if i==0:
            VI.append([(1,0)])
        else:
            VI.append([(0,0)])
            
    #Creación de la matriz de adyacencia(Llena de ceros)
    for i in range(lonMatriz):
        ele=[]
        for j in range(lonMatriz):
            ele.append((0,0))
        Matriz.append(ele)
        
    #Llenar la matriz creada con las probabilidades de las rendijas 
    for i in range(paredes):
        for j in range(paredes):
            if i==0:
                Matriz[i][j]=(0,0)
            else:
                Matriz[i][0]=(1/numRendijas,0)
                
    #Llenar las diagonales de la matriz creada de 1
    for i in range(paredes,lonMatriz):
        for j in range(paredes,lonMatriz):
            if i==j:
                Matriz[i][j]=(1,0)

    #Llenar la matriz creada con el vector probabilidad(blancos)
    num=1
    while num<numRendijas+1:
        pos=0
        for i in range(paredes,len(vectorProba)+paredes):
            Matriz[i][num]=vectorProba[pos]
            pos+=1
        num+=1
        paredes+=numBlancos+1
        
    #Multiplicación de las matriz dos veces
    Matriz2 = ComplejosCal.productoMatriz(Matriz,Matriz)
    
    #Multiplicación del vector inicial por la matriz de dos clicks de tiempo después
    VF = ComplejosCal.productoMatriz(Matriz2,VI)
            
    print("Matriz")
    print(Matriz)
    print(" ")
    print("Matriz déspues de dos clicks de tiempo")
    print(Matriz2)
    print(" ")
    print("Vector final")
    print(VF)

'--------------------------Rendija cuántica----------------------------'

#Experimento doble rendija cuántico
def rendijaCuanti(numRendijas,numBlancos,vectorProba):
    validar=False
    for i in range(len(vectorProba)):
        if vectorProba[i][1]!=0:
            validar=True
            break
    if validar==True:    
        for i in range(len(vectorProba)):  
            vectorProba[i]= ComplejosCal.producto(vectorProba[i],ComplejosCal.conjugado(vectorProba[i]))
    rendijaProba(numRendijas,numBlancos,vectorProba)
 
