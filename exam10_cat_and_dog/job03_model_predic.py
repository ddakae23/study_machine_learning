from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

img_path = ('../datasets/cat_dog/test/cat_test_02.jpg')
model_path = './cat_and_dog_0.814.h5'
model = load_model(model_path)
img = Image.open(img_path)
img = img.convert('RGB')
img = img.resize((64,64))
data = np.asarray(img)
data = data / 255
data = data.reshape(1, 64, 64, 3)

pred = model.predict(data)
print(pred)