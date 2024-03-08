import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"C:\Users\dell\Desktop\OpenCv\Photos\ajedrez.jpg"
img = cv2.imread(ruta_img, 0)

# aumento de brillo  ---------------------------------------------------------------------------------------------------------------

alto, ancho = img.shape# Obtener dimensiones de la imagen

factorBrillo = 100 # Factor de aumento de brillo

#img_aumento_brillo = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen con aumento de brillo

img_aumento_brillo = np.empty((alto, ancho))

for i in range(alto):
    for j in range(ancho):
        nuevo_valor = img[i, j] - factorBrillo
        
        img_aumento_brillo[i, j] = nuevo_valor
        
minValor = abs(np.min(img_aumento_brillo))
maxValor = np.min(img_aumento_brillo)

for i in range(alto): # Aumentar el brillo pixel por pixel
        print("el valor inicial es : ", img[i, j])
        nuevo_valor = img[i, j] + factorBrillo
        print("el nuevo valor es ", nuevo_valor)
        
        if nuevo_valor < 0: # Validar que los valores estén en el rango válido (0 a 255)
            print("se cambio")
            img_aumento_brillo[i, j] = nuevo_valor + minValor
            
        elif nuevo_valor > 255:
            img_aumento_brillo[i, j] = ((nuevo_valor/maxValor) * 255)
            
        else:
            img_aumento_brillo[i, j] = nuevo_valor
            print("se paso el valor :", img_aumento_brillo[i, j])

#IMPORTANTE: funcion para convertir los datos de la matriz a un formato valido para imprimirlo como imagen
img_modificada = cv2.convertScaleAbs(img_aumento_brillo)

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen modificada", img_modificada)

cv2.waitKey(0)
cv2.destroyAllWindows()