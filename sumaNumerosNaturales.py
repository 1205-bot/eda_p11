#Diseña un algoritmo recursivo que calculo la suma de los primeros números n naturales

#A) Escribe el caso base: cuando n == 1
#B) Escribe el caso recursivo: n - 1
#C) Encuentra la ecuación de recurrencia 
#D) Encuentra la complejidad del algoritmo usando la ecuación de recurrencia 

def Suma_natural(n):
    if n == 1:
        return 1 
    
    return n + Suma_natural(n - 1)


n = int(input("Ingresa el numero natural: "))

resultado = Suma_natural(n)

print("El resultado es: ", resultado)

# A) T(1) = 1
# B) return n + Suma_natural(n - 1)
# C) T(n) = T(n -1) + 1
# D) O(T(n)) = n