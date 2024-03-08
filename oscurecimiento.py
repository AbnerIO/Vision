import cv2
import numpy as np

np.set_printoptions(threshold=np.inf) # Configuro numpy para que me imprima toda la lista de numeros sin cortes

ruta_img = r"C:\Users\dell\Desktop\OpenCv\Photos\ajedrez.jpg"
img = cv2.imread(ruta_img, 0)

# oscurecimiento  ---------------------------------------------------------------------------------------------------------------

factor_oscurecimiento = 0.5 # Factor de oscurecimiento (menor que 1 para oscurecer)

alto, ancho = img.shape# Obtener dimensiones de la imagen
img_oscura = np.empty((alto, ancho))

for i in range(alto):
    for j in range(ancho):
        pixel = int(img[i, j] * factor_oscurecimiento)
        
        img_oscura[i, j] = pixel
        
minValor = abs(np.min(img_oscura))
maxValor = np.min(img_oscura)

for i in range(alto):# Aplicar la fórmula de aclarado de forma manual
    for j in range(ancho):
        pixel = int(img[i, j] * factor_oscurecimiento)

        if pixel < 0:# Utilizar if y else para asegurar que los valores estén en el rango válido (0 a 255)
            img_oscura[i, j] = pixel + minValor
        elif pixel > 255:
            img_oscura[i, j] = ((pixel/maxValor) * 255)
        else:
            img_oscura[i, j] = pixel


#IMPORTANTE: funcion para convertir los datos de la matriz a un formato valido para imprimirlo como imagen
img_modificada = cv2.convertScaleAbs(img_oscura)

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen modificada", img_modificada)

cv2.waitKey(0)
cv2.destroyAllWindows()