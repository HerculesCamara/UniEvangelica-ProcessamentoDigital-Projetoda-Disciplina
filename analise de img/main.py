from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure
import numpy as np
import cv2

# Abrir a imagem
imagem = Image.open('mamografia.jpg')

# Converter a imagem para tons de cinza
imagem_cinza = imagem.convert('L')

# Converter a imagem em matriz NumPy
matriz_imagem = np.array(imagem_cinza)

# Encontrar contornos na matriz da imagem
contornos = measure.find_contours(matriz_imagem, 0.8)

# Desenhar os contornos na imagem original
desenhar = ImageDraw.Draw(imagem)
for contorno in contornos:
    for i in range(len(contorno) - 1):
        desenhar.line([contorno[i][1], contorno[i][0], contorno[i+1][1], contorno[i+1][0]],
                      fill='red', width=2)

# Realçar o contraste da imagem
realcar = ImageEnhance.Contrast(imagem)
imagem = realcar.enhance(1.5)

# Salvar a nova imagem com os contornos
imagem.save('imagem_contornos.jpg')

#------------------------------------------------
import cv2
import numpy as np

# Corrigir a leitura da imagem
img = cv2.imread('imagem_contornos.jpg', cv2.IMREAD_GRAYSCALE)

# Contar o número de pixels brancos (valor 255) e pretos (valor 0)
numero_pixels_branco = np.sum(img == 255)
numero_pixels_preto = np.sum(img == 0)

# Exibir os números de pixels brancos e pretos
print('Número de pixels brancos:', numero_pixels_branco)
print('Número de pixels pretos:', numero_pixels_preto)

# Calcular o percentual de pixels brancos
percentual_pixels_brancos = numero_pixels_branco / (numero_pixels_branco + numero_pixels_preto) * 100

# Verificar o percentual de pixels brancos
if percentual_pixels_brancos >= 30:
    print('Imagem com câncer')
else:
    print('Imagem sem câncer')