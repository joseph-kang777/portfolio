# 목표 : 학생 성적 관리 프로그램

# 클래스명: Student
# 속성필드: 학생이름(__name), 학번(__student_Id), 과목(__subject), 
# 중간고사 성적(__score1),기말고사 성적(__score2), + 클래스 속성: 학교(__school)
# 메서드: 인스턴스 속성 get,set 메서드, 중간고사 & 기말고사 평균에 따른 학점 메서드, 
# 비공개 클래스 속성 학교 메서드 get 메서드

# 클래스명: Student_dict
# 속성필드: 학생정보(__students) 딕셔너리
# 메서드: 딕셔너리 추가 및 수정, 학생정보 딕셔너리 get 메서드

# input 받는 전처리를 위한 모듈
from input_condition import *

# Student Class
class Student:
    
    __school = "한국대학교" #비공개 클래스 속성

    def __init__(self,_name,_student_Id, _subject, _score1,_score2):
        
        # 비공개 인스턴스 속성
        self.__name = _name
        self.__student_Id = _student_Id
        self.__subject = _subject
        self.__score1 = _score1
        self.__score2 = _score2

    # 클래스 속성값 리턴하는 클래스 메서드
    @classmethod
    def school(cls): return cls.__school

    # @property를 활용한 getter,setter
    @property
    def name(self): return self.__name

    @property
    def subject(self) : return self.__subject

    @property
    def score1(self) : return self.__score1

    @score1.setter
    def score1(self,newScore1) : self.__score1 = newScore1

    @property
    def score2(self) : return self.__score2

    @score2.setter
    def score2(self,newScore2) : self.__score2 = newScore2

    @property
    def student_Id(self) : return self.__student_Id 

    # 종합 성적 확인
    def grade(self):
        total_score =(self.__score1 + self.__score2)/2

        if total_score >= 90:
            grade = "A"
        elif total_score >= 80:
            grade = "B"
        elif total_score >= 70:
            grade = "C"
        elif total_score >= 80:
            grade = "D"
        else:
            grade = "F"

        return grade

# 학생정보를 저장할 Student_dict class
class Student_dict:
    
    def __init__(self):
        # 학생 정보 저장할 딕셔너리 생성
        self.__students ={}

    # 학생정보 갱신
    def update_student(self,student):
        self.__students[(student.name, student.student_Id)] = [student.subject,student.score1,student.score2,student.school(),student.grade()]
    
    # 학생 정보 출력
    def print_student(self):
        for k,v in self.__students.items(): 
            print(f"이름 : {k[0]:>4}, 학번 : {k[1]:>8}, 과목 : {v[0]:>7}, 중간고사 성적 : {v[1]:0>3}점, 기말고사 성적 : {v[2]:0>3}점, 대학교 : {v[3]}, 학점 : {v[4]}\n")

    # 학생정보 저장된 딕셔너리 getter
    def get_dict(self):
        return self.__students
    

students = Student_dict()
students.update_student(Student("김민수",20157722,"파이썬의 이해",91,90))
students.update_student(Student("이수진",20147733,"파이썬의 이해",81,90))
students.update_student(Student("소인수",20187722,"파이썬의 이해",71,88))
students.update_student(Student("대인수",20147733,"파이썬의 이해",81,100))
students.update_student(Student("대인수",20158823,"파이썬의 이해",81,86))
students.update_student(Student("정대만",20188823,"농구의 이해",88,98))
students.update_student(Student("채치수",20118823,"농구의 이해",100,86))
students.update_student(Student("김대환",20162323,"마술의 이해",100,100))
students.update_student(Student("배진호",20212925,"파이썬의 이해",10,100))
students.update_student(Student("장진석",20219915,"운동의 이해",100,100))
students.update_student(Student("김근태",20182289,"파이썬의 이해",100,100))
students.update_student(Student("강백호",20208823,"농구의 이해",88,95))
students.update_student(Student("배보람",20212282,"창업의 이해",100,100))
students.update_student(Student("김찬수",20212282,"파이썬의 이해",100,100))
students.update_student(Student("박선경",20201833,"파이썬의 이해",100,100))
students.update_student(Student("이태영",20193823,"파이썬의 이해",100,100))
students.update_student(Student("최성진",20187295,"파이썬의 이해",100,100))
students.update_student(Student("나서영",20208123,"파이썬의 이해",100,100))

# 실행부
def process():

    while True:
        students_list_keys =list(students.get_dict().keys())

        num =numCheck_withoutError(input("1. 학생정보 입력 2.학생정보 조회 3. 학생성적 변경 4. 수강인원 출력 5. 종료 " ))
        
        # 학생 정보 입력받아 딕셔너리에 저장할 수 있음.
        if num == 1: 
            
            try: 
                name = strCheck_withError(input("이름 : "))
                student_Id = numCheck_withError2(input("학번 : "))
                subject = strCheck_withError(input("과목 : "))
                score1 = numCheck_withError((input("중간 : ")))
                score2 = numCheck_withError((input("기말 : ")))
                students.update_student(Student(name,student_Id,subject,score1,score2))
                
            except: 
                print("에러발생!, 초기화면으로 돌아갑니다.")

        # 딕셔너리에 저장된 학생 정보 조회 가능
        elif num ==2: 
            try: 
                cnt = 0
                key_idx = 0
                name = strCheck_withError(input("이름 : "))

                for i in range(0,len(students_list_keys)):
                    if students_list_keys[i][0] ==name:
                        key_idx = i 
                        cnt+=1

                if cnt >= 2: # 동명이인 존재 확인
                    print("동명이인이 있습니다.")
                    
                    #추가적인 정보로 학번을 받음
                    student_Id = numCheck_withError2(input("학생의 학번을 입력하세요 :")) 

                    print(f"이름 : {name}, \
                            학번 : {student_Id}, \
                            수강과목 : {students.get_dict()[name,student_Id][0]}, \
                            중간고사 성적 : {students.get_dict()[name,student_Id][1]}, \
                            기말고사 성적 : {students.get_dict()[name,student_Id][2]}, \
                            대학교 : {students.get_dict()[name,student_Id][3]}, \
                            학점 : {students.get_dict()[name,student_Id][4]}")

                elif cnt == 1: #검색된 결과가 한명이라서 바로 출력
                    student_Id =students_list_keys[key_idx][1] 
                    print(f"이름 : {name}, \
                            학번 : {student_Id}, \
                            수강과목 : {students.get_dict()[name,student_Id][0]}, \
                            중간고사 성적 : {students.get_dict()[name,student_Id][1]}, \
                            기말고사 성적 : {students.get_dict()[name,student_Id][2]}, \
                            대학교 : {students.get_dict()[name,student_Id][3]}, \
                            학점 : {students.get_dict()[name,student_Id][4]}")

                else: # 리스트에 없는 이름을 입력할 경우 에러 발생
                    raise Exception
            
            except:
                print("에러발생!, 초기화면으로 돌아갑니다.")

        # 학생 성적 변경 기능
        elif num ==3:
            try:
                cnt = 0
                key_idx = 0
                name = strCheck_withError(input("이름 : "))

                for i in range(0,len(students_list_keys)):
                    if students_list_keys[i][0] ==name:
                        key_idx = i 
                        cnt+=1

                if cnt >= 2: # 동명이인이 있을 경우
                    print("동명이인이 있습니다.")
                    student_Id = numCheck_withError2(input("학생의 학번을 입력하세요 :")) 
                    score1 = numCheck_withError((input("중간 : ")))
                    score2 = numCheck_withError((input("기말 : ")))
                    students.update_student(Student(name,student_Id,students.get_dict()[name,student_Id][0],score1,score2))

                elif cnt ==1: #검색된 결과가 한명이라서 바로 출력
                    student_Id =students_list_keys[key_idx][1]
                    score1 = numCheck_withError((input("중간 : ")))
                    score2 = numCheck_withError((input("기말 : ")))
                    students.update_student(Student(name,student_Id,students.get_dict()[name,student_Id][0],score1,score2))

                else: # 리스트에 없는 이름을 입력할 경우 에러 발생
                    raise Exception
            except:
                 print("에러발생!, 초기화면으로 돌아갑니다.")

        # 수강인원 출력 및 성적 저장
        elif num==4:
            cnt2= 0
            try:
                subject_dict ={}
                subject = strCheck_withError(input("과목명을 입력해주세요 : "))


                for k,v in students.get_dict().items():
                    if v[0] == subject:
                        subject_dict[k] = v
                        cnt2 +=1

                if cnt2 >0:

                    subject_list = sorted(subject_dict.items(), key= lambda x: x[1][4])
                    subject_dict = dict(subject_list)
                    subject_dict_keys_list = list(subject_dict)
                    
                    # 수강 학생 성적 저장
                    filename = "'"+subject +"'"+ " 수강인원" + ".txt"
                    fp = open(filename,mode="w",encoding= "utf-8")
                    fp.write("'"+subject +"'"+ " 수강인원\n")
                    
                    for i in range(0, len(subject_dict)):
                        k = subject_dict_keys_list[i] 
                        fp.write(f"이름 : {k[0]:>4}, \
                                학번 : {k[1]:>8},  \
                                중간고사 성적 : {subject_dict[k][1]:0>3}점, \
                                기말고사 성적 : {subject_dict[k][2]:0>3}점, \
                                대학교 : {subject_dict[k][3]}, \                                        학점 : {subject_dict[k][4]}\n")
                    fp.close()

                else:
                    raise Exception

            except:
                print("에러발생!, 초기화면으로 돌아갑니다.")

        # 프로그램 종료
        elif num ==5:
            print("프로그램을 종료합니다.")
            break

        else:
            print("숫자 범위를 벗어났거나 잘못된 입력입니다.")

process()