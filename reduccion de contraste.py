import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"C:\Users\dell\Desktop\OpenCv\Photos\ajedrez.jpg"
img = cv2.imread(ruta_img, 0)


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

