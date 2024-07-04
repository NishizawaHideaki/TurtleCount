"""
フォルダ内のファイルの枚数に応じてフィルタをかける
"""
#削除するファイルの枚数の閾値。jpgの枚数を計数する。

import argparse
import os
import shutil
from glob import glob
import cv2


base_path = "./test/"

img = cv2.imread('test/6.jpg', 0)

_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255), 3)
cv2.imwrite('test.png', img)


cnt = contours[0]

moment = cv2.moments(cnt)
print(moment)

print(moment['m00'])
print(cv2.contourArea(cnt))

