import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"C:\Users\dell\Desktop\OpenCv\Photos\ajedrez.jpg"
img = cv2.imread(ruta_img, 0)

# disminución de brillo ---------------------------------------------------------------------------------------------------------------

alto, ancho = img.shape# Obtener dimensiones de la imagen

factor_disminucion_brillo = 0# Factor de disminución de brillo

#img_disminucion_brillo = np.zeros_like(img, dtype=np.uint8)# Crear una nueva matriz para la imagen con disminución de brillo

img_disminucion_brillo = np.empty((alto, ancho))

for i in range(alto):
    for j in range(ancho):
        nuevo_valor = img[i, j] - factor_disminucion_brillo
        
        img_disminucion_brillo[i, j] = nuevo_valor
        
minValor = abs(np.min(img_disminucion_brillo))
maxValor = np.min(img_disminucion_brillo)

for i in range(alto):# Disminuir el brillo pixel por pixel
    
        nuevo_valor = img[i, j] - factor_disminucion_brillo
        
        if nuevo_valor < 0: # Utilizar if y else para asegurar que los valores estén en el rango válido (0 a 255)
            print("se cambio")
            img_disminucion_brillo[i, j] = nuevo_valor + minValor
            
        elif nuevo_valor > 255:
            img_disminucion_brillo[i, j] = ((nuevo_valor/maxValor) * 255)
            
        else:
            img_disminucion_brillo[i, j] = nuevo_valor
            print("se paso el valor :", img_disminucion_brillo[i, j])
            

#IMPORTANTE: funcion para convertir los datos de la matriz a un formato valido para imprimirlo como imagen
img_modificada = cv2.convertScaleAbs(img_disminucion_brillo)

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen modificada", img_modificada)

cv2.waitKey(0)
cv2.destroyAllWindows()