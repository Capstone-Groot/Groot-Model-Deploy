# 필수 패키지를 import합니다.
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import tensorflow as tf
from flask import Flask, flash, request, redirect, url_for, jsonify
import io
import tensorflow.keras as keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Flask 애플리케이션과 Keras 모델을 초기화합니다.
app = Flask(__name__)
model = None


def load_model():
    # 미리 학습된 Keras 모델을 불러옵니다
    global model
    model = keras.models.load_model('./flower.h5')


@app.route("/predict", methods=["POST"])
def predict():
    # view로부터 반환될 데이터 딕셔너리를 초기화합니다.
    data = {"success": False}

    # 이미지가 엔트포인트에 올바르게 업로드 되었는디 확인하세요
    if request.method == "POST":

        if request.files.get("file"):
            # PIL 형식으로 이미지를 읽어옵니다.
            image = request.files["file"].read()

            # 분류를 위해 이미지를 전처리합니다.
            test_img = Image.open(io.BytesIO(image))
            test_img = test_img.resize((224, 224), Image.ANTIALIAS)
            test_img = img_to_array(test_img)
            test_img = test_img.reshape((1,) + test_img.shape)
            # 입력 이미지를 분류하고 클라이언트로부터 반환되는 예측치들의 리스트를 초기화 합니다.

            result = model.predict_classes(test_img)
            name = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
            result = int(result[0])

            # 결과를 반복하여 반환된 예측 목록에 추가합니다.
            data["image"] = name[result]

            # 요청이 성공했음을 나타냅니다.
            data["success"] = True

    # JSON 형식으로 데이터 딕셔너리를 반환합니다.
    return jsonify(data)


@app.route('/predict', methods=['GET'])
def hi():
    test_img = Image.open('./image.jpg')
    test_img = test_img.resize((224, 224), Image.ANTIALIAS)
    test_img = img_to_array(test_img)
    test_img = test_img.reshape((1,) + test_img.shape)
    print(test_img)
    print(test_img.shape)

    result = model.predict_classes(test_img)
    name = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
    result = int(result[0])
    return str(name[result])


# 실행에서 메인 쓰레드인 경우, 먼저 모델을 불러온 뒤 서버를 시작합니다.
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    load_model()
    app.run()