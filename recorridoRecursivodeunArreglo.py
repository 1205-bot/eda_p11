#Diseña un algoritmo recursivo que imprima todos los elementos de un arreglo

#A) Escribe el caso base: cuando i == 0
#B) Escribe el caso recursivo: i - 1
#C) Encuentra la ecuación de recurrencia 
#D) Encuentra la complejidad del algoritmo usando la ecuación de recurrencia 

def imp_arr(arr, i):
    if i == len(arr):
        return
    
    print(arr[i])

    imp_arr(arr, i + 1)

arr = [10, 20, 30, 40, 50]

imp_arr(arr, 0)

#A) i == 0
#B) i + 1
#C) T(n) = T(n - 1) + 1
#D) T(n) + T(n - 1) = 1
#   si T(n) = x^1
#   (x - 1)(x - 1) = 0
#   O(T(n)) = n