import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import font_manager, rc

fe = font_manager.FontEntry(
    fname=r'KBO Dia Gothic_TTF\KBO Dia Gothic_bold.ttf', # ttf 파일이 저장되어 있는 경로
    name='KBO Dia Gothic_bold')                        # 이 폰트의 원하는 이름 설정
font_manager.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 12, 'font.family': 'KBO Dia Gothic_bold'}) # 폰트 설정

file = '오승준/데이터산업_데이터직무_인력_현황.csv'   # 데이터산업_내_빅데이터_관련_데이터직무_인력_현황_20230804090602.csv
datajobDF = pd.read_csv(file, header=None,encoding='ms949')

datajobDF_total = datajobDF.set_index(0)


datajobDF_total.drop([2,3,5,6,8,9,11,12], axis=1, inplace=True)

datajobDF_total.drop(['데이터 아키텍트','데이터 개발자','데이터 엔지니어','데이터 분석가','데이터베이스 관리자','데이터 과학자','데이터 컨설턴트','데이터 기획자'], axis=0, inplace=True)
datajobDF_total = datajobDF_total.T
datajobDF_total = datajobDF_total.set_index('데이터직무별(1)')
datajobDF_total
x = [2017, 2018, 2019, 2020]
y = [77105, 82623, 89058, 101967]


plt.plot(x, y, color = '#B22222', marker='o')
plt.xlabel('연도')
plt.ylabel('인력 수')
plt.title('연도별 데이터직무 인력 수')
plt.savefig("data_work")