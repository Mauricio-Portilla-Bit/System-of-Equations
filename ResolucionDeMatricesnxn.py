# Para resolver una ecuacion de N variables, se Necesitan N funciones para relacionarlas
# Este programa observa la sumatoria de produccion de cada maquina y resuleve para los valores 

#Matriz de a Resolver
A = []
AC = []
ren = []

print('ESCRIBE CON CUANTOS PRODUCTOS EXISTEN EN PRODUCCION')
var = int(input())
print('DEBE DE COMPLETAR ' + str(var) + ' REGISTROS')

for a in range(var):
    ren = []
    for i in range(var+1):
        if (i + 1 < var + 1):
            print('ESCRIBE LA PRODUCCION DEL PRODUCTO #' + str(i + 1))
        else:
            print('ESCRIBE EL CONSUMO')
        ren.append(float(input()))
    A.append(ren)
    AC.append(ren)

#Matriz de Ceros Aqui se realizan las operaciones 
B = []
ren = []
for i in range(2):
    ren = []
    for a in range(len(A[0])):
        ren.append([0])
    B.append(ren)

#Valor de los parametros 
val = []
for i in range (len(A[0])-1):
    val.append(0) 

#De acuerdo a los elementos que tiene realiza las operaciones 
# Recorrer las filas 

for a in range(len(A[0])-2):
    longCol = (len(A[0]))-2-a

    # Recorrer las columnas 
    for i in range (longCol):

        for z in range(2):
            for m in range(len(A[0])):
                B[z][m] = 0

            #Se multiplica las filas despues de la primera por el valor de arriba
        for p in range(len(A[0])):  
            B[0][p] = A[a][a]*A[len(A[0])-i-2][p]
                
            #Se multiplica la fila superior por el valor de arriba 
        for e in range(len(A[0])):
            B[1][e] = A[a][e]*A[len(A[0])-i-2][a]

            #Se suman las filas ya multiplicadas para obtener el valor esperado 
        for o in range(len(A[0])):
            A[len(A[0])-i-2][o] = B[0][o] - B[1][o]

#Despeje de Ecuaciones
for i in range(len(val)): #Divisiones 
    val[i] = A[len(val)-i-1][len(A[0])-1]

    for k in range (i): # Restas 
        val[i] = val[i]- (A[len(A[0])-i-2][len(A[0])-2-k])*val[k]# Respuesta = Respuesta - (valores anteriores)*variable en k

    val[i] = val[i]/(A[len(A[0])-2-i][len(A[0])-2-i]) # Division entre la diagonal inversa

print('MATRIZ A RESOLVER')
for i in range (len(AC[0])-1):
    print(AC[i])  

print('RESPUESTA DE CADA VARIABLE')
print(val)

