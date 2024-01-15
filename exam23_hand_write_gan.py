import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

number_GAN_models = []
for i in range(10):
    number_GAN_models.append(load_model('./models/generator_{}.h5'.format(i)))
    # number_GAN_models.append(load_model('./models/generator_5_KDY.h5'))

four_digit_number = '51446865354'
imgs = []
for i in four_digit_number:
    print(i)
    i = int(i)  # i를 int형으로 바꿔주는것
    z = np.random.normal(0, 1, (1, 100))
    fake_img = number_GAN_models[i].predict(z)
    fake_img = fake_img * 0.5 + 0.5
    imgs.append(fake_img.reshape(28, 28))

_, axs = plt.subplots(1, len(four_digit_number), figsize=(10, 40), sharex=True, sharey=True)
for i in range(len(four_digit_number)):
    axs[i].imshow(imgs[i], cmap='Spectral')
    axs[i].axis('off')
plt.show()

img = imgs[0]
for i in range(1, len(four_digit_number)):
    img = np.append(img, imgs[i], axis=1)
plt.gray()
plt.imshow(img)
plt.axis('off')
plt.show()