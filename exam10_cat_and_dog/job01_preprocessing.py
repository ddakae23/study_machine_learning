from PIL import Image   ##설치 안되어있으면 'pip install pillow' 로 설치 진행필요
import glob #파이썬 기본패키지  / 파일 찾아서 리스트로 만들어주는 함수
import numpy as np
from sklearn.model_selection import train_test_split

img_dir = '../datasets/cat_dog/train/'  ##파일 이미지 경로
categories = ['cat','dog']
image_w = 64
image_h = 64    ##이미지 사이즈 맞춤 전처리필요함

pixel = image_h * image_w * 3
X = []
Y = []
files = None

for idx, category in enumerate(categories):
    files = glob.glob(img_dir + category + '*.jpg')

    for i, f in enumerate(files):
        try:    ##try, except 예외처리문법
            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((image_w, image_h))
            data = np.asarray(img)  #데이터타입 array로 바꿈
            X.append(data)
            Y.append(idx)
            if i % 300 == 0:
                print(category,':',f)
        except:
            print('error :',category,i)
X = np.array(X)
Y = np.array(Y)
X = X/255
print(X[0])
print(Y[0])
exit()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1)
xy = (X_train, X_test, Y_train, Y_test)
np.save('../datasets/binary_image_data_npy',xy)
