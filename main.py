#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 入力画像の読み込み
img = cv2.imread("pic.jpg")

# ガウスフィルタ
imgs = cv2.GaussianBlur(img, (9, 9), 5)

# グレースケール変換
gray = cv2.cvtColor(imgs, cv2.COLOR_RGB2GRAY)

#OTSUの2値化
ret,th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
bwimg = cv2.cvtColor(th,cv2.COLOR_GRAY2RGB)

black = [0, 0, 0]
blue = [99,32,0]

bwimg[np.where((bwimg == black).all(axis=2))] = blue

# 結果を出力
cv2.imwrite("output.png", bwimg)