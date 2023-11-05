# week_06_ml

## 🖥 프로젝트명
돈벼락 : 머신러닝으로 이더리움 가격 등락 예측하기

## 📋 프로젝트 소개 및 기능
- Kaggle에서 수집한 이더리움 가격 데이터셋으로 이더리움 가격을 예측하고자 하였습니다.

- RandomForest, XGboost 등을 활용하였습니다.

- 참고문헌을 통해 금 시세 같은 외부 데이터를 병합하여 사용하였습니다.


## ⚙ 개발환경

- Machine Learning Language

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 
 <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"> <img src="https://img.shields.io/badge/XGBOOST-570679?style=for-the-badge&logo=XGBOOST&logoColor=white">


## 📊 활용 데이터
- Kaggle에서 2017-2022년까지의 분당 이더리움 가격 데이터셋을 활용하였습니다.

- investing.com 홈페이지에서 금 선물 시세 csv 파일을 받아 활용하였습니다.

- 구글 트렌드에 이더리움 검색해 csv 파일을 받아 활용하였습니다.


## 📌 프로젝트 세부소개

- RandomForestRegressor, XGBoostClassifier,XGBoostRegressor 등을 활용하여 예측해보았습니다.

- 구글트렌드를 독립변수를 사용하는 경우는 가격의 등락을 예측하는데 효과적이지 않았습니다. 


- 상승과 하락을 자체를 더미변수를 만들어  XGBoostClassifier 모델로 학습시킨 결과 0.86 수준의 높은 성능을 보였으나, XGBoostRegressor 가격의 등락 자체는 0.67 수준의 낮은 성능을 보였습니다.

- RandomForestRegressor 같은 트리 기반 모델들은 가격 등락 예측에 효과적이지 않았으며, 비교적 Boosting 방식이 효과적이었습니다.


## 🔨 프로젝트 보완사항

- 프로젝트 진행 당시 시계열 데이터에 대한 이해가 부족해 train, test 데이터를 randomstate를 줘서 진행했는데, 시계열 데이터 성능 확인을 위해 기간에 기준으로 train 과 test를 분리해서 다시 분석할 예정입니다.