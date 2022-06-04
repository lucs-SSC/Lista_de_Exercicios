# -*- coding: utf-8 -*-
"""Lista de Exercícios de Implementação

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LWzK6yH6C7rl3wgODA1N1KRPFTNWD-yX
"""

# Passo 1: Instalar o Pytesseract e o tesseract-OCR no Colab:
! sudo apt install tesseract-ocr 
! pip install pytesseract
! sudo apt-get install tesseract-ocr-por

# Importar bibliotecas:
import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import imagem

import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt
import scipy

"""1) Desenvolva um código que lhe permita abrir uma imagem RGB ou BGR de sua preferência, utilizando a interface python do OpenCV. Logo depois, converta a imagem para escala de cinza e exiba as duas imagens lado a lado na tela. Documente as funções utilizadas no código."""

urls = ["cristiano.png"]

for url in urls:
  image = cv.imread(url) #Função para carregar a imagem
  gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)#Função para converter para cinza
  graySpace = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)#Função para converter para o espaço de cor BGR

  final_frame = np.hstack((image, graySpace))#Função para agrupar e juntar na horizontal
  
  cv2_imshow(final_frame)

"""2)Utilizando o código fonte das nossas aulas como base, carregue uma imagem contendo pelo menos uma face (pode ser a imagem carregada no item 1), depois carregue o modelo de detecção de faces utilizado nas nossas aulas anteriores. Construa um código de detecção de faces, encontre a caixa envolvente da face na imagem. Pinte o retângulo ao redor da(s) face(s) encontrada(s) e exiba a imagem pintada na tela. Documente as funções utilizadas no código"""

face = cv.imread('cristiano.png') #Função para carregar a imagem

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')#Função para classificar o rosto


faces = face_cascade.detectMultiScale(face,scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv.CASCADE_SCALE_IMAGE)


for (x,y,w,h) in faces:
     cv.rectangle(face,(x,y),(x+w,y+h),(0,0,255),2)

cv2_imshow(face)

"""3)Carregue uma imagem que contenha uma página de texto de um documento digitalizado de sua preferência. Uma vez carregada a imagem, utilize o OCR com o qual trabalhamos na nossa última aula (Tesseract), reconheça o texto, e imprima o texto reconhecido na tela. Documente as funções utilizadas no código."""

# ! sudo apt-get install tesseract-ocr-por

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import imagem

urls2 = ["motivacional.jpg"]

for url in urls2:
  image = cv.imread(url) 
  cv2_imshow(image)

Informações = pytesseract.image_to_string(image, lang='por')#Função para converter a imagem para texto
print(Informações)#Função para escrever o texto