from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

argument15=[]
argument16=[]
argument17=[]
argument18=[]
argument19=[]
argument20=[]
argument21=[]
argument22=[]
argument23=[]
argument24=[]
argument25=[]
argument26=[]

for i in range(1,11):

    html = urlopen(f"https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=132000%2C025%2C024%2C023&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=10&keywordJobCont=&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=&actServExcYn=&maxPay=&keywordStaAreaNm=&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=1&region=&infaYn=&resultCntInfo=10&siteClcd=WORK&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=N&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=7bd1e995-f2e8-4b8e-8400-046e4729bbf0&keywordBusiNm=&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex={i}&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL")
    soup = BeautifulSoup(html,features="lxml")
    
    a_list = soup.select("div.cp-info-in > a")

    for i in a_list:
    
        sites = "https://www.work.go.kr" + i["href"]
        # print(sites)
        html2 = urlopen(sites)
        soup2 = BeautifulSoup(html2,features="lxml")
        # list1= soup2.select_one("#contents > section > div > div.careers-area > div.careers-new > div.border > div.left")
        # career=list1.select_one("div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(1) span").text.strip()
        # study =list1.select_one("div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(2) > span").text.strip()
        
        argument15.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(4) > table > tbody > tr > td").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument16.append(soup2.select_one("div.careers-area > div:nth-child(6) > table tr > td:nth-child(1)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument17.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(6) > table > tbody > tr > td:nth-child(3)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument18.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(14) > table > tbody > tr > td:nth-child(1)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument19.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(14) > table > tbody > tr > td:nth-child(2)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument20.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(14) > table > tbody > tr > td:nth-child(3)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument21.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(14) > table > tbody > tr > td:nth-child(4)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument22.append(soup2.select_one("#contents > section > div > div.careers-area > div:nth-child(14) > table > tbody > tr > td:nth-child(5)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument23.append(soup2.select_one("#contents > section > div > div.careers-area > div.careers-table.cnts.v1.mt20 > table > tbody > tr:nth-child(2) td:nth-child(1)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument24.append(soup2.select_one("#contents > section > div > div.careers-area > div.careers-table.cnts.v1.mt20 > table > tbody > tr:nth-child(2) td:nth-child(2)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument25.append(soup2.select_one("#contents > section > div > div.careers-area > div.careers-table.cnts.v1.mt20 > table > tbody > tr:nth-child(4) td:nth-child(1)").text.strip().replace("\n","").replace("\t","").replace(" ",""))
        argument26.append(soup2.select_one("#contents > section > div > div.careers-area > div.careers-table.cnts.v1.mt20 > table > tbody > tr:nth-child(4) td:nth-child(2)").text.strip().replace("\n","").replace("\t","").replace(" ",""))

total_list = [argument15,argument16,argument17,argument18,argument19,argument20,argument21,argument22,argument23,argument24,argument25,argument26]

df = pd.DataFrame(total_list,index=['직무내용',
        '모집직종','관련직종','전공','자격면허','외국어능력',
        '병역대체 복무자채용','고용허가제','우대조건','컴퓨터 활용능력','기타우대사항',
        '작업환경'])

df= df.T

df = df.assign(sqlp=df['자격면허'].apply(lambda x: 'SQLP(SQL전문가)' in x))
df = df.assign(a=df['자격면허'].apply(lambda x: '정보처리기사' in x))
df = df.assign(b=df['자격면허'].apply(lambda x: '정보통신기사' in x))
df = df.assign(c=df['자격면허'].apply(lambda x: '전기' in x))#
df = df.assign(d=df['자격면허'].apply(lambda x: '리눅스' in x))
df = df.assign(e=df['직무내용'].str.lower().apply(lambda x: 'c' in x))
df = df.assign(f=df['직무내용'].str.lower().apply(lambda x: 'java' in (' ' + x + ' ')))
df = df.assign(g=df['직무내용'].str.lower().apply(lambda x: 'javascript' in (' ' + x + ' ')))
df = df.assign(h=df['직무내용'].str.lower().apply(lambda x: 'html' in (' ' + x + ' ')))
df = df.assign(i=df['직무내용'].str.lower().apply(lambda x: 'python' in (' ' + x + ' ') or '파이썬' in (' ' + x + ' ')))

# 엑셀 파일 저장
df.to_csv("junior2.csv",sep=";")