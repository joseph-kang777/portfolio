# week_09_nlp

## 🖥 프로젝트명
**감성주점** (**감성**분석으로 **주**가를 **점**쳐보자!) 

## 📋 프로젝트 소개 및 기능
- 감성분석 기반으로 YG엔터테인먼트의 주가가 상승과 하락을 예측해보았습니다.

- 데이터는 YG 엔티테인먼트 주식의 종목토론방, 뉴스기사를 크롤링하였습니다.

- Transformers에 한국어가 사전학습된 snunlp/KR-FinBert-SC 모델을 사용하여, 긍정, 중립, 부정 여부를 산출하였습니다.

- 감성분석 결과를 Label로 사용하여, ML,DL 등으로 분석을 진행하였습니다.

## ⚙ 개발환경

- Machine Learning Language

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white"> <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"> <img src="https://img.shields.io/badge/transformers-570679?style=for-the-badge&logo=Transformers&logoColor=white">


## 📊 활용 데이터
- 네이버 페이 증권 YG 엔터테인먼트 종목토론방 데이터를 크롤링하였습니다.

- 네이버 YG엔터테인먼트 검색 후 관련 뉴스를 크롤링하였습니다.


## 📌 프로젝트 세부소개

- RandomForestClassifier, XGBoostClassifier,KNNClassifier 같은 ML 분류모델과, DL의 DNN모델를 써서 분류해보았습니다.


## 🔨 프로젝트 보완사항

- 이번 주가 예측은 감성분석을 기반으로 해서 진행하였는데, Precision이나 Recall 향상을 위해서 다른 인자를 추가하고자 합니다.
