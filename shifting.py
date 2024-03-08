import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"C:\Users\dell\Desktop\OpenCv\Photos\ajedrez.jpg"
img = cv2.imread(ruta_img, 0)

# Cantidad de desplazamiento (50 píxeles hacia abajo y 30 píxeles hacia la derecha)
# En caso de querer moverlos para arriba o para la izquierda, solo se ponen los valores en negativo y ya
shift_horizontal = 30
shift_vertical = 50

# Funciones de numpy para hacer el shifting
shifted_image = np.roll(img, shift_horizontal, axis=1)
shifted_image = np.roll(shifted_image, shift_vertical, axis=0)

cv2.imshow('Original', img)
cv2.imshow('Shifted', shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()