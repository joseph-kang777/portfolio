# 모듈 로드
from flask import Flask, render_template, request
import cv2
from rembg import remove
import numpy as np
import pandas as pd
import json
from PIL import Image
import tensorflow as tf
import keras
from keras.models import load_model
from rembg import remove

# 재필
test1_model = load_model("./models/Hogwarts_dorm_CNN_2.keras")

# 성진
test2_1_model = load_model("./models/man_tone_model.h5")
test2_2_model = load_model("./models/woman_tone_model.h5")

# 요셉
# 커스텀 레이어 정의
class CastToFloat32(keras.layers.Layer):
    def call(self, inputs):
        return tf.cast(inputs, tf.float32)

# 모델 로드 시 custom_objects 옵션 사용
# with keras.utils.custom_object_scope({'CastToFloat32': CastToFloat32}) :
test3_model = load_model("./models/auto_model2.h5",custom_objects=({ "Custom>CastToFloat32": CastToFloat32}))

# 찬수
test4_model = load_model("./models/Idol_Face.keras")

app = Flask(__name__, static_url_path='/static')

# 메인 페이지
@app.route('/')
def main():
    return render_template('inner.html')

@app.route('/inner.html')
def mains():
    return render_template('inner.html')

# 재필
@app.route('/test1.html')
def test1():
    return render_template('test1.html')

# 성진
@app.route('/test2.html')
def test2():
    return render_template('test2.html')

# 요셉
@app.route('/test3.html')
def test3():
    return render_template('test3.html')

# 찬수
@app.route('/test4.html')
def test4():
    return render_template('test4.html')

# 업로드 시 동작하는 route, Post 방식으로 받음
@app.route('/upload1', methods=['POST'])
def upload1_file():
 
    uploaded_file = request.files['file']
    uploaded_file.save('./static/image/uploaded_file.png')

    if uploaded_file:

        # 파일읽기
        image =cv2.imread('./static/image/uploaded_file.png',cv2.IMREAD_GRAYSCALE)

        # 배열로 바꾸고 28*28로 resize
        img = np.array(image)
        img = cv2.resize(img, (28, 28))

        # 4차원 / 스케일링
        image = img.reshape(-1, 28, 28, 1)
        image = image/255.

        # 확인하기
        result = list(test1_model.predict(image)[0]).index(test1_model.predict(image)[0].max())

        if result == 0:return render_template('test1.html', data='그리핀도르' )
        elif result ==1:return render_template('test1.html', data='후플푸프')
        elif result ==2:return render_template('test1.html', data='레번클로' )
        else :return render_template('test1.html', data='슬리데린' )

    # 파일이 선택되지 않았다면 알림 
    else:
        return "<script>alert('사진이 선택되지 않았습니다'); history.back();</script>"

# 업로드 시 동작하는 route, Post 방식으로 받음
@app.route('/upload2', methods=['POST'])
def upload2_file():

    gender=request.form.get("gender")
    
    uploaded_file = request.files['file']
    uploaded_file.save('./static/image/uploaded_file.png')

    if uploaded_file:

        # 1. 파일읽기
        org=cv2.imread('./static/image/uploaded_file.png')

        # 2. resize
        imgData=cv2.resize(org,dsize=(32,32))
        imgData=imgData.reshape((1,32,32,3))

        # 3. 정규화
        imgData_=imgData/255

        # 성별이 남자라면
        if gender == "man":
            predictions=test2_1_model.predict(imgData_)

            # 예측값을 해석하여 쿨톤 또는 웜톤으로 분류
            if predictions[0][0] > predictions[0][1]:
                return render_template('test2.html', data="쿨톤 이미지입니다." )
            else:
                return render_template('test2.html', data="웜톤 이미지입니다." )

        # 성별이 여자라면
        elif gender == "woman":
            predictions=test2_2_model.predict(imgData_)
             # 예측값을 해석하여 쿨톤 또는 웜톤으로 분류
            if predictions[0][0] > predictions[0][1]:
                return render_template('test2.html', data="쿨톤 이미지입니다." )
            else:
                return render_template('test2.html', data="웜톤 이미지입니다." )

    # 사진이 선택되지 않았을 경우 알림
    else:
        return "<script>alert('사진이 선택되지 않았습니다'); history.back();</script>"

# 업로드 시 동작하는 route, Post 방식으로 받음
@app.route('/upload3', methods=['POST'])
def upload3_file():
 
    uploaded_file = request.files['file']
    uploaded_file.save('./static/image/uploaded_file.png')
    
    if uploaded_file:

        dsize_ =(32,32)
        # 1. 파일읽기
        org=cv2.imread('./static/image/uploaded_file.png')
        # 2. resize
        imgData=cv2.resize(org,dsize=dsize_)
        # 3. 배경제거
        imgData=remove(imgData)
        # 4. 정규화
        imgData=imgData/255
        # 5. reshape
        imgData_=imgData.reshape((1,32,32,4))
        proba=test3_model.predict(imgData_)
        proba_list=proba.tolist()
        return render_template('test3.html', data=proba_list )
    
    # 사진이 선택되지 않았을 경우 알림
    else:
        return "<script>alert('사진이 선택되지 않았습니다'); history.back();</script>"

# 업로드 시 동작하는 route, Post 방식으로 받음
@app.route('/upload4', methods=['POST'])
def upload4_file():
 
    uploaded_file = request.files['file']
    uploaded_file.save('./static/image/uploaded_file.png')

    if uploaded_file:

        img = Image.open('./static/image/uploaded_file.png')
        img = img.convert('L').resize((200,200))
        img_array = np.array(img)
        img_array = img_array.reshape((1, -1))
        prediction = test4_model.predict(img_array)
        predicted_label = np.argmax(prediction)
        

        if predicted_label == 0:
            return render_template('test4.html', data='에스파' )
        elif predicted_label == 1:
            return render_template('test4.html', data='블랙핑크' )
       
        elif predicted_label == 2:
            return render_template('test4.html', data='아이들' )
        
        elif predicted_label == 3:
            return render_template('test4.html', data='잇지' )
          
        elif predicted_label == 4:
            return render_template('test4.html', data='아이브' )
          
        elif predicted_label == 5:
            return render_template('test4.html', data='르세라핌' )
        
        elif predicted_label == 6:
            return render_template('test4.html', data='뉴진스' )
   
    # 사진을 선택핮 않은 경우
    else:
        return "<script>alert('사진이 선택되지 않았습니다'); history.back();</script>"
    
if __name__ == '__main__':
    app.run()


