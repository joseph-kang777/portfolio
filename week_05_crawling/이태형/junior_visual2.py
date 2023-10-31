import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from matplotlib import font_manager
import numpy as np
import PIL
from	wordcloud import	WordCloud
from	konlpy.tag import	Okt
from	collections	import	Counter
import	platform

fe = font_manager.FontEntry(
    fname=r'KBO Dia Gothic_TTF\KBO Dia Gothic_bold.ttf', # ttf 파일이 저장되어 있는 경로
    name='KBO Dia Gothic_bold')                        # 이 폰트의 원하는 이름 설정
font_manager.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 12, 'font.family': 'KBO Dia Gothic_bold'}) # 폰트 설정

# junior1.csv df으로 바꾸기
df1 = pd.read_csv("크롤링_CSV/junior1.csv",sep=";")
df1= df1.drop('Unnamed: 0',axis=1)

# junior2.csv df으로 바꾸기
df2 = pd.read_csv("크롤링_CSV/junior2.csv",sep=";")
df2= df2.drop('Unnamed: 0',axis=1)

# df 열로 합침
df = pd.concat([df1,df2],axis=1)

#시각화
fig= plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
pallete_colors = sns.color_palette("RdPu", 3)

sns.barplot(x=df["학력"],y=df["임금"],data=df,ax=ax1,edgecolor="black",ci=None,palette=pallete_colors)
ax1.set_title("학력별 연봉",size=20)
ax1.set_xlabel("학력",size=12)
ax1.set_ylabel("연봉(만원/년)",size=12)
for i in ax1.containers:
    ax1.bar_label(i,size=12)
fig.savefig("junior학력별연봉.png")

#시각화
fig2= plt.figure(figsize=(14,7))
ax1 = fig2.add_subplot(1,1,1)
pallete_colors2 = sns.color_palette("RdBu", 14)
sns.barplot(x=df["지역"],y=df["임금"],data=df,ax=ax1,edgecolor="black",ci=None,palette=pallete_colors2)
ax1.set_title("지역별 연봉",size=20)
ax1.set_xlabel("지역",size=12)
ax1.set_ylabel("연봉(만원/년)",size=12)
plt.xticks(rotation=45)
for i in ax1.containers:
    ax1.bar_label(i,size=12)
fig2.savefig("junior지역별연봉.png")

# wordcloud시각화
list_work2=" ".join(df["모집직종"].str.replace("\xa0","").str.replace("\r","").to_list())
icon = PIL.Image.open(r'using_img\electronic.png')
img2 = PIL.Image.new('RGB', icon.size, (255,255,255))
img2.paste(icon, icon)
img = np.array(img2)

okt =	Okt()	#	Open	Korean	Text	객체 생성
#	okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag =	[]
sentences_tag =	okt.pos(list_work2)

noun_adj_list =	[]
#	tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for	word,	tag	in	sentences_tag:
    if	tag	in	['Noun'	,	'Adjective']:
        noun_adj_list.append(word)

#	가장 많이 나온 단어부터 40개를 저장한다.
counts	=	Counter(noun_adj_list)
tags	=	counts.most_common(40)
tags.pop(1)

if	platform.system()	==	'Windows':
    path	=	r'KBO Dia Gothic_TTF\KBO Dia Gothic_bold.ttf'
wc =	WordCloud(font_path=path,	background_color="white",	max_font_size=200,mask=img, colormap='inferno')
cloud	=	wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,	10))
plt.axis('off')
plt.imshow(cloud)
plt.savefig("junior_wordcloud2")
