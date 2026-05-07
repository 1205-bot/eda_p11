#Diseña un algoritmo recursivo que imprima una cadena al reves 

#A) Escribe el caso base: cuando i == 0
#B) Escribe el caso recursivo: i - 1
#C) Encuentra la ecuación de recurrencia 
#D) Encuentra la complejidad del algoritmo usando la ecuación de recurrencia 

i = 4
def imp_arr(arr, i):
    if i == 0:
        return
    
    print(arr[i])

    imp_arr(arr, i - 1)

arr = [10, 20, 30, 40, 50]

imp_arr(arr, i)

#A) i == 0
#B) i - 1
#C) T(n) = T(n - 1) + 1
#D) T(n) + T(n - 1) = 1
#   si T(n) = x^1
#   (x - 1)(x - 1) = 0
#   O(T(n)) = n