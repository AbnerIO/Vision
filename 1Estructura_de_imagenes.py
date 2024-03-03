import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Confugiro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"assets/ranita.png"
img = cv2.imread(ruta_img, 0)
img_color = cv2.imread(ruta_img)

# print("imagen a color")
# print(img_color) #
print("imagen a escala de grises")
print(img)


# Muestra la imagen en una ventana
cv2.imshow('Imagen', img)
cv2.waitKey(0)  # Espera hasta que se presione una tecla
cv2.destroyAllWindows()  # Cierra la ventana al presionar una tecla