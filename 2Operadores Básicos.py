import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"assets/ranita.png"
img = cv2.imread(ruta_img, 0)


# Aclarado/Oscurecimiento


factor_aclarado = 1.5 # Factor de aclarado (mayor que 1 para aclarar)

alto, ancho = img.shape # Obtener dimensiones de la imagen

img_aclarada = np.zeros_like(img, dtype=np.uint8) # Crear una nueva matriz para la imagen aclarada

for i in range(alto):# Aplicar la fórmula de aclarado de forma manual
    for j in range(ancho):
        pixel = int(img[i, j] * factor_aclarado)

        if pixel < 0:# Utilizar if y else para asegurar que los valores estén en el rango válido (0 a 255)
            img_aclarada[i, j] = 0
        elif pixel > 255:
            img_aclarada[i, j] = 2551
        else:
            img_aclarada[i, j] = pixel

print("Imagen original:")
print(img)
print("Imagen aclarada: ")
print(img_aclarada)


# oscurecimiento

factor_oscurecimiento = 0.5 # Factor de oscurecimiento (menor que 1 para oscurecer)

alto, ancho = img.shape# Obtener dimensiones de la imagen

img_oscurecida = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen oscurecida

for i in range(alto):# Aplicar la fórmula de oscurecimiento de forma manual
    for j in range(ancho):
        pixel = int(img[i, j] * factor_oscurecimiento)

        if pixel < 0:# Utilizar if y else para asegurar que los valores estén en el rango válido (0 a 255)
            img_oscurecida[i, j] = 0
        elif pixel > 255:
            img_oscurecida[i, j] = 255
        else:
            img_oscurecida[i, j] = pixel

print("Imagen original:")
print(img)
print("Imagen oscurecida: ")
print(img_oscurecida)

# Copiado

alto, ancho = img.shape # Obtener dimensiones de la imagen

img_copiada = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen copiada

for i in range(alto):# Copiar la imagen pixel por pixel
    for j in range(ancho):
        img_copiada[i, j] = img[i, j]

print("Imagen original:")
print(img)
print("Imagen copiada: ")
print(img_copiada)

# Negativo

alto, ancho = img.shape # Obtener dimensiones de la imagen

img_negativa = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen negativa

for i in range(alto): # Crear el negativo pixel por pixel
    for j in range(ancho):
        img_negativa[i, j] = 255 - img[i, j]
print("Imagen original:")
print(img)
print("Imagen negativo: ")
print(img_negativa)

# Aumento/Disminución de brillo

# aumento de brillo

alto, ancho = img.shape# Obtener dimensiones de la imagen

factor_brillo = 50# Factor de aumento de brillo

img_aumento_brillo = np.zeros_like(img, dtype=np.uint8) # Crear una nueva matriz para la imagen con aumento de brillo

for i in range(alto):# Aumentar el brillo pixel por pixel
    for j in range(ancho):
        nuevo_valor = img[i, j] + factor_brillo
        if nuevo_valor < 0:# Utilizar if y else para asegurar que los valores estén en el rango válido (0 a 255)
            img_aumento_brillo[i, j] = 0
        elif nuevo_valor > 255:
            img_aumento_brillo[i, j] = 255
        else:
            img_aumento_brillo[i, j] = nuevo_valor

print("Imagen original:")
print(img)
print("Imagen aumento de brillo: ")
print(img_aumento_brillo)

# disminución de brillo

alto, ancho = img.shape# Obtener dimensiones de la imagen

factor_disminucion_brillo = 50# Factor de disminución de brillo

img_disminucion_brillo = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen con disminución de brillo

for i in range(alto):# Disminuir el brillo pixel por pixel
    for j in range(ancho):
        nuevo_valor = img[i, j] - factor_disminucion_brillo
        if nuevo_valor < 0:# Utilizar if y else para asegurar que los valores estén en el rango válido (0 a 255)
            img_disminucion_brillo[i, j] = 0
        elif nuevo_valor > 255:
            img_disminucion_brillo[i, j] = 255
        else:
            img_disminucion_brillo[i, j] = nuevo_valor
print("Imagen original:")
print(img)
print("Imagen disminución de brillo: ")
print(img_disminucion_brillo)

# Elongación/Reducción de contraste

# elongación

alto, ancho = img.shape# Obtener dimensiones de la imagen

punto_control_min = 50 # Puntos de control para la elongación de contraste
punto_control_max = 200

img_elongacion_contraste = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen con elongación de contraste

for i in range(alto): # Aplicar la elongación de contraste pixel por pixel
    for j in range(ancho):
        if img[i, j] < punto_control_min:# Aplicar la transformación lineal
            img_elongacion_contraste[i, j] = 0
        elif img[i, j] > punto_control_max:
            img_elongacion_contraste[i, j] = 255
        else:
            img_elongacion_contraste[i, j] = int(
                ((img[i, j] - punto_control_min) / (punto_control_max - punto_control_min)) * 255
            )
print("Imagen original:")
print(img)
print("Imagen dcontraste elongado: ")
print(img_elongacion_contraste)

# reducción de contraste

alto, ancho = img.shape# Obtener dimensiones de la imagen

punto_control_min = 50# Puntos de control para la reducción de contraste
punto_control_max = 200

img_reduccion_contraste = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen con reducción de contraste

for i in range(alto):# Aplicar la reducción de contraste pixel por pixel
    for j in range(ancho):
        if img[i, j] < punto_control_min:# Aplicar la transformación lineal
            img_reduccion_contraste[i, j] = 0
        elif img[i, j] > punto_control_max:
            img_reduccion_contraste[i, j] = 255
        else:
            img_reduccion_contraste[i, j] = int(
                ((img[i, j] - punto_control_min) / (punto_control_max - punto_control_min)) * 127
            )
print("Imagen original:")
print(img)
print("Imagen contraste reducido: ")
print(img_reduccion_contraste)


# Shifting H/V/D
 



