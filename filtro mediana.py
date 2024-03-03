import cv2
import numpy as np

def obtener_submatriz(img, x, y):
    # Definir los límites para la submatriz
    fila_inicio = max(0, x)
    fila_fin = min(len(img), x + 10)
    col_inicio = max(0, y)
    col_fin = min(len(img[0]), y + 10)
    
    # Extraer la submatriz
    submatriz = img[fila_inicio:fila_fin, col_inicio:col_fin]
    
    # Si la submatriz no tiene 10x10, ajustarla con ceros
    if submatriz.shape != (10, 10):
        submatriz_ajustada = np.zeros((10, 10))
        submatriz_ajustada[0:submatriz.shape[0], 0:submatriz.shape[1]] = submatriz
        return submatriz_ajustada
    else:
        return submatriz

def calcular_mediana(arreglo):
    arreglo_ordenado = sorted(arreglo)
    #print(arreglo_ordenado)
    n = len(arreglo_ordenado)
    
    if n % 2 == 0:
        indice_medio_1 = n // 2 - 1
        indice_medio_2 = n // 2
        n1 = arreglo_ordenado[indice_medio_1]
        n2 = arreglo_ordenado[indice_medio_2]
        nuevo = int(n1)
        nuevo2 = int(n2)
        rs = nuevo + nuevo2
        
        mediana = (rs) // 2
    else:
        # Si hay un número impar de elementos, la mediana es el número en el medio
        indice_medio = n // 2
        mediana = arreglo_ordenado[indice_medio]
    
    return mediana

def dispersion_valores(arreglo, promedio):
    arreglo_nuevo = arreglo.copy()  # Para evitar modificar el arreglo original
    #print(arreglo_nuevo)
    
    for i in range(len(arreglo_nuevo)):  # Iteramos sobre los índices del arreglo
        valorA = int(arreglo_nuevo[i])
        #print(valorA)
        arreglo_nuevo[i] = abs(((valorA - promedio) * 100) / promedio)
        #print(arreglo_nuevo[i])
    
    arreglo_dispersiones = arreglo_nuevo
    
    return arreglo_dispersiones

def cambiar_valores(arreglo_dispersiones, arreglo, mediana):
    for i in range(len(arreglo_dispersiones)):
        if arreglo_dispersiones[i] > 10:
            arreglo[i] = mediana
            print("se cambioooooooooo")
    
    arreglo_final = arreglo
    
    return arreglo_final

img = cv2.imread(r"C:\Users\dell\Desktop\OpenCv\Photos\pruebavc.jpeg", 0)

np.set_printoptions(threshold=np.inf)

# Pedir al usuario las coordenadas
x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

# Se obtiene el pedazo de la matriz
submatriz = obtener_submatriz(img, x, y)

#print("Submatriz iniciando en las coordenadas ({},{}):".format(x, y))
#print(submatriz)

#submatriz = [[209, 224, 210, 204],[219, 211, 223, 232], [228, 207, 140, 233], [215, 223, 219, 225]]

#Se convierte a arreglo
arreglo = np.ravel(submatriz)

# Sacar el promedio
suma_valores = sum(arreglo)
cantidad_elementos = len(arreglo)
promedio = suma_valores / cantidad_elementos
print("El promedio es", promedio)

# Sacar la mediana
mediana = calcular_mediana(arreglo)
print("La mediana del arreglo es:", mediana)


# Sacar la dispersion de cada valor
arreglo_dispersiones = dispersion_valores(arreglo, promedio)
print("El arreglo de dispersiones es:", arreglo_dispersiones)

# Arreglo ya corregido
arreglo_final = cambiar_valores(arreglo_dispersiones, arreglo, mediana)
print(arreglo_final)
