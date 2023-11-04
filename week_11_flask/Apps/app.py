# 모듈 로딩
from flask import Flask,render_template,request,session
import os
# from pathlib import Path

# ORM Lib 모듈
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid3

# 채팅 모델
from keras.models import load_model
import tensorflow as tf
import re
import tensorflow_datasets as tfds
import pandas as pd
import numpy as np

# DB 전역변수
db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_pyfile("config.py")
    print(f'app.config[DEBUG] -> {app.config["DEBUG"]}')

    # ORM 연동
    from Apps.crud import model

    db.init_app(app)
    migrate.init_app(app,db)

    # 메인페이지
    @app.route("/")
    def index():
        return render_template("index.html")
    
    # 채팅화면
    @app.route("/chat")
    def chat():
        from Apps.crud.model import Chat
        from datetime import datetime

        #채팅기록가져옴
        chattings=db.session.query(Chat).filter_by(uuid=session["uuid"]).all()
        
        return render_template("chat.html",chattings=chattings)

    # 클라이언트에서 채팅 내용 보내면, 서버쪽에서 받아서 POST 방식으로 전송
    @app.route("/chat_react",methods=["POST"])
    def chat_react():
        import tensorflow as tf
        from transformers import AutoTokenizer
        from transformers import TFGPT2LMHeadModel

        # 사전학습된 모델 load
        model = TFGPT2LMHeadModel.from_pretrained("Apps/model/new_new_saved_model")
        
        # form 태그 내용 가져옴
        chatting=request.form["chat"]

        
        text = chatting
        sent = '' + text + ''
        
        # 토큰나이즈
        tokenizer = AutoTokenizer.from_pretrained('skt/kogpt2-base-v2')
        tokenizer.bos_token_id=1
        tokenizer.eos_token_id =1
        tokenizer.pad_token_id =3
        input_ids = [tokenizer.bos_token_id] + tokenizer.encode(sent)
        input_ids = tf.convert_to_tensor([input_ids])

        # 채팅 답장
        output =model.generate(input_ids, max_length=50, early_stopping=True, eos_token_id=tokenizer.eos_token_id,top_k=50,top_p=0.95,do_sample=True)
        decoded_sentence = tokenizer.decode(output[0].numpy().tolist())
        
        from Apps.crud.model import Chat
        from datetime import datetime

        # 본인이 채팅기록 DB추가
        chat1=Chat(uuid=session["uuid"],classification=1,chat=text,email=session["email"],created_at =datetime.now())
        db.session.add(chat1)
        db.session.commit()

        # 답변한 모델의 채팅기록 DB추가
        chat2=Chat(uuid=session["uuid"],classification=2,chat=decoded_sentence.split("<sys>")[1].replace("</s>",""),email=session["email"],created_at =datetime.now())
        db.session.add(chat2)
        db.session.commit()
        
        # 개인 채팅기록 모두 가져오기
        chattings=db.session.query(Chat).filter_by(uuid=session["uuid"]).all()
        
        # 채팅 데이터 모두 chat 페이지 전달
        return  render_template("chat.html",chattings= chattings)

    from Apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth)
    return app
