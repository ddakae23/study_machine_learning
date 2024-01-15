import dlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
import numpy as np

detector = dlib.get_frontal_face_detector()
shape = dlib.shape_predictor('./models/shape_predictor_68_face_landmarks.dat')
#
# img = dlib.load_rgb_image('./image/01.jpg')
# plt.figure(figsize=(16, 10))
# plt.imshow(img)
# plt.show()
#
# img_result = img.copy()
# dets = detector(img, 1)
#
# if (len(dets)) == 0:
#     print('Not find faces')
#
# else:
#     fig, ax = plt.subplots(1, figsize=(10,16))
#     for det in dets:
#         x, y, w, h = det.left(), det.top(), det.width(), det.height()
#         rect = patches.Rectangle((x, y), w, h,      #얼굴부분에 사각형 그리는 코드 / Rectangle(사각형그리는 함수)
#                                  linewidth=2, edgecolor='b', facecolor='None') # 선두께=2, 선색=b,  사각형 안의 색 안칠하기
#         ax.add_patch(rect)
# ax.imshow(img_result)
# plt.show()
#
# fig, ax = plt.subplots(1, figsize=(16, 10))
# obj = dlib.full_object_detections()
#
# for detection in dets:
#     s = shape(img, detection)
#     obj.append(s)
#
#     for point in s.parts():
#         circle = patches.Circle((point.x, point.y),     ## 얼굴부분에 점으로 라인그려주는 코드
#                                 radius=3, edgecolor='b', facecolor='b')
#         ax.add_patch(circle)
#     ax.imshow(img_result)
# plt.show()

def align_faces(img):
    dets = detector(img)
    objs = dlib.full_object_detections()
    for detection in dets:
        s = shape(img, detection)
        objs.append(s)
    faces = dlib.get_face_chips(img, objs, size=256, padding=0.5)
    return faces
#
# test_img = dlib.load_rgb_image('./image/02.jpg')
# test_faces = align_faces(test_img)
# fig, axes = plt.subplots(1, len(test_faces)+1, figsize=(10, 8))
# axes[0].imshow(test_img)
# for i, face in enumerate(test_faces):
#     axes[i + 1].imshow(face)
# plt.show()
#
sess = tf.Session()
init_op = tf.group(tf.global_variables_initializer(),
                   tf.local_variables_initializer())

## tensorflow모델 읽어서 제너레이터 하는 부분
sess.run(init_op)

saver = tf.train.import_meta_graph('./models/model.meta')
saver.restore(sess, tf.train.latest_checkpoint('./models'))
graph = tf.get_default_graph()
X = graph.get_tensor_by_name('X:0')
Y = graph.get_tensor_by_name('Y:0')
Xs = graph.get_tensor_by_name('generator/xs:0')

## 이미지 전처리 부분
def preprocess(img):
    return img / 127.5 - 1
def deprecess(img):
    return (img + 1) / 2

img1 = dlib.load_rgb_image('./image/no_makeup/vSYYZ429.png')
img1_faces = align_faces(img1)

img2 = dlib.load_rgb_image('./image/makeup/XMY-014.png')
img2_faces = align_faces(img2)

fig, axes = plt.subplots(1, 2, figsize=(8, 5))
axes[0].imshow(img1_faces[0])
axes[1].imshow(img2_faces[0])
plt.show()

##이미지 전처리 부분
src_img = img1_faces[0]
ref_img = img2_faces[0]

X_img = preprocess(src_img)
X_img = np.expand_dims(X_img, axis=0)

Y_img = preprocess(ref_img)
Y_img = np.expand_dims(Y_img, axis=0)

output = sess.run(Xs, feed_dict={X:X_img, Y:Y_img})
output_img = deprecess(output[0])

fig, axes = plt.subplots(1, 3, figsize=(8, 5))
axes[0].imshow(img1_faces[0])
axes[1].imshow(img2_faces[0])
axes[2].imshow(output_img)
plt.show()
