# 모듈 로딩
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from konlpy.tag import Kkma,Okt
import mariadb
import pandas as pd
import json

# 데이터를 가져올 db params
conn_params = {'host':'아이피주소','port':3306,'user':'project_user','password':'project_user','database':"project",'autocommit':True}
conn = mariadb.connect(**conn_params)
cur = conn.cursor()

# cosine 유사도 함수
def make_cosine(a,b):
    return np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))

#db에서 recipe 가져오기
cur.execute("SELECT * FROM tb_recipe")
total_recipe=cur.fetchall()
df=pd.DataFrame(total_recipe,columns=["요리","레시피"])


okt = Okt()

# 레시피에서 명사만 추출
noun_list = []
for i in df["레시피"]:
    noun_list.append(" ".join(okt.nouns(i)))

df["레시피_명사"] = noun_list

#db에서 ingredient 가져오기
cur.execute("SELECT * FROM tb_ingredient")
total_ingredient=cur.fetchall()
df2=pd.DataFrame(total_ingredient,columns=["요리","재료"])


#db에서 picture 가져오기
cur.execute("SELECT * FROM tb_picture")
total_picture=cur.fetchall()
df3=pd.DataFrame(total_picture,columns=["요리","사진"])

ndf=df.merge(df3,how="inner",on="요리")

# countvectorizer로 단어 인코딩
cv = CountVectorizer()
texts = ndf["레시피_명사"].to_list()
dtm = cv.fit_transform(texts)
dtm_df = pd.DataFrame(dtm.toarray(),columns=cv.get_feature_names_out())

app = Flask(__name__, static_url_path='/static')

# index 홈페이지
@app.route('/')
def main():
    return render_template('index.html')

# 키 이벤트로 request 받은 데이터 처리
@app.route('/request_data',methods=['POST'])
def mains():

    data = request.form.get("key")
    test = okt.nouns(data)
    test = [" ".join(test)]
    dtm1 = cv.transform(test)
    dtm1.toarray()[0]
    target =dtm1.toarray()[0]
    box = []
    for i in range(len(dtm_df)):
        sample = dtm_df.iloc[i].to_numpy()
        cosine = make_cosine(target,sample)
        box.append(cosine)

    ndf["유사도분석"] = box

    best_name=ndf.sort_values("유사도분석",ascending=False)["요리"].to_list()[0]
    best_recipe="\n".join(ndf.sort_values("유사도분석",ascending=False)["레시피"].to_list()[0].split("|"))
    best_pic = ndf.sort_values("유사도분석",ascending=False)["사진"].to_list()[0]

    best_name2=ndf.sort_values("유사도분석",ascending=False)["요리"].to_list()[1]
    best_recipe2="\n".join(ndf.sort_values("유사도분석",ascending=False)["레시피"].to_list()[1].split("|"))
    best_pic2 = ndf.sort_values("유사도분석",ascending=False)["사진"].to_list()[1]

    best_name3=ndf.sort_values("유사도분석",ascending=False)["요리"].to_list()[2]
    best_recipe3="\n".join(ndf.sort_values("유사도분석",ascending=False)["레시피"].to_list()[2].split("|"))
    best_pic3 = ndf.sort_values("유사도분석",ascending=False)["사진"].to_list()[2]

    
    return json.dumps({"cook_name":best_name,"recipe_name":best_recipe,"picture_name":best_pic,"cook_name2":best_name2,"recipe_name2":best_recipe2,"picture_name2":best_pic2,"cook_name3":best_name3,"recipe_name3":best_recipe3,"picture_name3":best_pic3 },ensure_ascii=False)

if __name__ == '__main__':
    app.run()
