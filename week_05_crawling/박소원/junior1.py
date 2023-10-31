from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

argument1=[]#경력
argument2=[]
argument3=[]
argument4=[]
argument5=[]
argument6=[]
argument7=[]
argument8=[]
argument9=[]
argument10=[]
argument11=[]
argument12=[]
argument13=[]
argument14=[]

for i in range(1,11):

    html = urlopen(f"https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=132000%2C025%2C024%2C023&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=10&keywordJobCont=&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=1&region=&infaYn=&resultCntInfo=10&siteClcd=WORK&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=N&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=7bd1e995-f2e8-4b8e-8400-046e4729bbf0&keywordBusiNm=&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex={i}&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL")
    soup = BeautifulSoup(html,features="lxml")
    
    a_list = soup.select("div.cp-info-in > a")

    for i in a_list:
    
        sites = "https://www.work.go.kr" + i["href"]
        html2 = urlopen(sites)
        soup2 = BeautifulSoup(html2,features="lxml")

        list1 = soup2.select("#contents > section > div > div.careers-area > div.careers-new > div.border > div.left")
        for i in list1:
            argument1.append(i.select_one("div:nth-child(3) > div  div > ul > li span").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument2.append(i.select_one("div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(2) > span").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument3.append(i.select_one("div:nth-child(2) > div:nth-child(2) > div > ul > li:nth-child(1) > span").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument4.append(i.select_one("div:nth-child(2) > div:nth-child(2) > div > ul > li:nth-child(2) > span").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument5.append(i.select_one("div:nth-child(3) > div:nth-child(1) > div > ul > li:nth-child(1) > span").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument6.append(i.select_one("div:nth-child(3) > div:nth-child(1) > div > ul > li:nth-child(2) > span").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument7.append(i.select_one("div:nth-child(3) > div:nth-child(2) > div > ul > li").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        list2= soup2.select("#contents > section > div > div.careers-area > div.careers-new > div.border > div.right")
        for i in list2:
            argument8.append(i.select_one("div.info > ul > li:nth-child(1) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument9.append(i.select_one("div.info > ul > li:nth-child(2) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument10.append(i.select_one("div.info > ul > li:nth-child(3) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument11.append(i.select_one("div.info > ul > li:nth-child(4) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument12.append(i.select_one("div.info > ul > li:nth-child(5) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument13.append(i.select_one("div.info > ul > li:nth-child(6) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))
            argument14.append(i.select_one("div.info > ul > li:nth-child(7) > div").text.strip().replace("\n","").replace("\t","").replace(" ",""))

total_list = [argument1,argument2,argument3,argument4,argument5,argument6,argument7,argument8,argument9,argument10,argument11,argument12,argument13,argument14]

df = pd.DataFrame(total_list,index=['경력','학력','지역','임금','고용형태',
        '근무형태','복리후생','기업명','업종','기업규모',
        '설립년도','연매출액','홈페이지','근로자수'])

# 행렬 전환
df= df.T

# 학력무관이면 그냥 출력, 다른 경우는 학력 최저기준을 기준으로 출력

def edu_slice(str1):
    if str1!="학력무관":
        return str1[:2]+"이상"
    else:
        return str1
    
# 학력 재분류
df["학력"]=df["학력"].apply(edu_slice)

# 지역 광역시 및 도 기준으로 분류
df["지역"]=df["지역"].str.replace("도","도 ").str.replace("시","시 ").str.split(" ").str[0]

# 임금 부분을 숫자로 변경 및 평균으로 변경하는 함수
def wage_avg(list1):
    
    if int(list1[0])>9000:
        if len(list1)==1:
            return int(list1[0])*40*52/10000
        else:
            wage =int((int(list1[0])+int(list1[1]))/2)*40*52/10000
            return wage
    
    elif int(list1[0])>1000:
        if len(list1)==1:
            return int(list1[0])
        else:
            wage =int((int(list1[0])+int(list1[1]))/2)
            return wage
    elif int(list1[0])<1000:
        if len(list1)==1:
            return int(list1[0])*12
        else:
            wage =int((int(list1[0])+int(list1[1]))/2)*12
            return wage

# 임금 수치 변환
df["임금"]=df["임금"].str.replace("연봉","").str.replace("월급","").str.replace("시급","").str.replace("만원","").str.replace("원","").str.replace("이상","").str.replace(",","").str.split("~").apply(wage_avg).apply(lambda x: int(x))

# 고용형태는 기간 유무로만 구분 필요
df["고용형태"]=df["고용형태"].str.replace("\(시간\(선택\)제\)","")

# 기업명에 있던 "(주)" 및 "주식회사" 제거
df["기업명"]=df["기업명"].str.replace("주식회사","").str.replace("\(주\)","")

# 설립년도 없는 곳 그냥 0으로 처리함
# 0으로 처리해야 나중에 불린 인덱스 조건 줘서 하기 좋을거 같아서
# ~년도 없앰
# int 형으로 바꿈
df["설립년도"]=df["설립년도"].str[:4].replace("",0).apply(lambda x :int(x))

# 근로자수 수치형으로 변경
df["근로자수"]=df["근로자수"].str.replace("명","").apply(lambda x: int(x))

# 엑셀 파일 저장
df.to_csv("junior1.csv",sep=";")