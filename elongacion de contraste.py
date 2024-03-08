import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"C:\Users\dell\Desktop\OpenCv\Photos\ajedrez.jpg"
img = cv2.imread(ruta_img, 0)


# Elongación/Reducción de contraste

# elongación

alto, ancho = img.shape # Obtener dimensiones de la imagen

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