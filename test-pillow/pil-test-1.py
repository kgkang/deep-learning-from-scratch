# coding: utf-8

import sys, os
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from PIL import Image
import numpy as np

(xtrain,ytrain),(xtest,ytest) = load_mnist(normalize=False, flatten=True, one_hot_label=False);
# train,test = (xtrain,ytrain), (xtest,ytest)
# print(type(train),type(test))
# print(type(xtrain),type(ytrain))
# print(type(xtest),type(ytest))

# xtrain은 numpy.ndarray 타입

print("xtrain type: ", type(xtrain), "xtrain shape: ", xtrain.shape)
print("xtrain[0] type: ", type(xtrain[0]), "xtrain[0] shape: ", xtrain[0].shape)

img = xtrain[0]
print("Before reshape: ", img.shape)
# print("img data : ", img)
img = img.reshape(28,28)
print("After reshape : ", img.shape)
# print("img data : ", img)

# pil_img = Image.fromarray(img)
pil_img = Image.fromarray(np.uint8(img))
pil_img.show()
# img.show()
