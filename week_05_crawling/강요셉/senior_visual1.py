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

# senior1.csv df으로 바꾸기
df1 = pd.read_csv("크롤링_CSV/senior1.csv",sep=";")
df1= df1.drop('Unnamed: 0',axis=1)

# senior2.csv df으로 바꾸기
df2 = pd.read_csv("크롤링_CSV/senior2.csv",sep=";")
df2= df2.drop('Unnamed: 0',axis=1)

# df 열로 합침
df = pd.concat([df1,df2],axis=1)

#시각화
fig= plt.figure(figsize=(20,7))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
contrast_colors = sns.color_palette("Dark2")
sns.barplot(x=["정보처리기사 자격증 O","정보처리기사 자격증 X"], y= [df.loc[df["a"],"임금"].mean(),df.loc[~df["a"],"임금"].mean()],palette=contrast_colors,ax=ax1,edgecolor="black")
ax1.set_title("정보처리기사 자격증에 따른 연봉",size=20)
ax1.set_xlabel("정보처리기사 자격증 유무",size=12)
ax1.set_ylabel("연봉(만원/년)",size=12)
for i in ax1.containers:
    ax1.bar_label(i,size=12)
ax1.bar_label

sns.barplot(x=["정보통신기사 자격증 O","정보통신기사 자격증 X"], y= [df.loc[df["b"],"임금"].mean(),df.loc[~df["b"],"임금"].mean()],palette=contrast_colors,ax=ax2,edgecolor="black")
ax2.set_title("정보통신기사 자격증에 따른 연봉",size=20)
ax2.set_xlabel("정보통신기사 자격증 유무",size=12)
ax2.set_ylabel("연봉(만원/년)",size=12)
for i in ax2.containers:
    ax2.bar_label(i,size=12)
ax2.bar_label

sns.barplot(x=["전기기사 자격증 O","전기기사 자격증 X"], y= [df.loc[df["c"],"임금"].mean(),df.loc[~df["c"],"임금"].mean()],palette=contrast_colors,ax=ax3,edgecolor="black")
ax3.set_title("전기기사 자격증에 따른 연봉",size=20)
ax3.set_xlabel("전기기사 자격증 유무",size=12)
ax3.set_ylabel("연봉(만원/년)",size=12)
for i in ax3.containers:
    ax3.bar_label(i,size=12)
ax3.bar_label
fig.savefig("senior자격증연봉.png")


#시각화
fig2= plt.figure(figsize=(20,7))
ax1 = fig2.add_subplot(1,3,1)
ax2 = fig2.add_subplot(1,3,2)
ax3 = fig2.add_subplot(1,3,3)
contrast_colors = sns.color_palette("Dark2")
sns.barplot(x=["리눅스 언어 O","리눅스 언어 X"], y= [df.loc[df["d"],"임금"].mean(),df.loc[~df["d"],"임금"].mean()],palette=contrast_colors,ax=ax1,edgecolor="black")
ax1.set_title("리눅스 언어에 따른 연봉",size=20)
ax1.set_xlabel("리눅스 언어 사용 여부",size=12)
ax1.set_ylabel("연봉(만원/년)",size=12)
for i in ax1.containers:
    ax1.bar_label(i,size=12)
ax1.bar_label

sns.barplot(x=["C 언어 O","C 언어 X"], y= [df.loc[df["e"],"임금"].mean(),df.loc[~df["e"],"임금"].mean()],palette=contrast_colors,ax=ax2,edgecolor="black")
ax2.set_title("C 언어에 따른 연봉",size=20)
ax2.set_xlabel("C 언어 사용 여부",size=12)
ax2.set_ylabel("연봉(만원/년)",size=12)
for i in ax2.containers:
    ax2.bar_label(i,size=12)
ax2.bar_label

sns.barplot(x=["JAVA 언어 O","JAVA 언어 X"], y= [df.loc[df["f"],"임금"].mean(),df.loc[~df["f"],"임금"].mean()],palette=contrast_colors,ax=ax3,edgecolor="black")
ax3.set_title("JAVA 언어에 따른 연봉",size=20)
ax3.set_xlabel("JAVA 언어 사용 여부",size=12)
ax3.set_ylabel("연봉(만원/년)",size=12)
for i in ax3.containers:
    ax3.bar_label(i,size=12)
ax3.bar_label
fig2.savefig("senior언어연봉1.png")

#시각화
fig3= plt.figure(figsize=(20,7))
ax1 = fig3.add_subplot(1,3,1)
ax2 = fig3.add_subplot(1,3,2)
ax3 = fig3.add_subplot(1,3,3)
contrast_colors = sns.color_palette("Dark2")
sns.barplot(x=["JAVASCRIPT 언어 O","JAVASCRIPT 언어 X"], y= [df.loc[df["g"],"임금"].mean(),df.loc[~df["g"],"임금"].mean()],palette=contrast_colors,ax=ax1,edgecolor="black")
ax1.set_title("JAVASCRIPT 언어에 따른 연봉",size=20)
ax1.set_xlabel("JAVASCRIPT 언어 사용 여부",size=12)
ax1.set_ylabel("연봉(만원/년)",size=12)
for i in ax1.containers:
    ax1.bar_label(i,size=12)
ax1.bar_label

sns.barplot(x=["HTML 언어 O","HTML 언어 X"], y= [df.loc[df["h"],"임금"].mean(),df.loc[~df["h"],"임금"].mean()],palette=contrast_colors,ax=ax2,edgecolor="black")
ax2.set_title("HTML 언어에 따른 연봉",size=20)
ax2.set_xlabel("HTML 언어 사용 여부",size=12)
ax2.set_ylabel("연봉(만원/년)",size=12)
for i in ax2.containers:
    ax2.bar_label(i,size=12)
ax2.bar_label

sns.barplot(x=["PYTHON 언어 O","PYTHON 언어 X"], y= [df.loc[df["i"],"임금"].mean(),df.loc[~df["i"],"임금"].mean()],palette=contrast_colors,ax=ax3,edgecolor="black")
ax3.set_title("PYTHON 언어에 따른 연봉",size=20)
ax3.set_xlabel("PYTHON 언어 사용 여부",size=12)
ax3.set_ylabel("연봉(만원/년)",size=12)
for i in ax3.containers:
    ax3.bar_label(i,size=12)
ax3.bar_label
fig3.savefig("senior언어연봉2.png")

# wordcloud시각화
list_work=" ".join(df["직무내용"].str.replace("\xa0","").str.replace("\r","").to_list())
icon = PIL.Image.open(r'using_img\electronic.png')
img = PIL.Image.new('RGB', icon.size, (255,255,255))
img.paste(icon, icon)
img = np.array(img)

okt =	Okt()	#	Open	Korean	Text	객체 생성
#	okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag =	[]
sentences_tag =	okt.pos(list_work)

noun_adj_list =	[]
#	tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for	word,	tag	in	sentences_tag:
    if	tag	in	['Noun','Adjective']:
        noun_adj_list.append(word)

#	가장 많이 나온 단어부터 40개를 저장한다.
counts	=	Counter(noun_adj_list)
tags	=	counts.most_common(40)
tags.pop(1)

if	platform.system()	==	'Windows':
    path	=	r'KBO Dia Gothic_TTF\KBO Dia Gothic_bold.ttf'
wc =	WordCloud(font_path=path,	background_color="white",	max_font_size=150,mask=img, colormap='inferno')
cloud	=	wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,	10))
plt.axis('off')
plt.imshow(cloud)
plt.savefig("senior_wordcloud1")