# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:43:29 2022

@author: Serpil ÖZGÜVEN
"""

import cv2
import matplotlib.pyplot as plt

# resmi içe aktaralım
img = cv2.imread("sudoku.jpg",0)
plt.figure, plt.imshow(img, cmap="gray"),plt.axis("off"), plt.title("Orijinal Image")

# x eksenindeki gradyanlar
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5) 
plt.figure, plt.imshow(sobelx, cmap="gray"),plt.axis("off"), plt.title("Sobel X ")


# y eksenindeki gradyanlar
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5) 
plt.figure, plt.imshow(sobely, cmap="gray"),plt.axis("off"), plt.title("Sobel Y ")


# Laplacian Gradyan (Her ikisini de(x ve y )yi tespit etmek istersek)
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap="gray"), plt.axis("off"), plt.title("Laplacian")