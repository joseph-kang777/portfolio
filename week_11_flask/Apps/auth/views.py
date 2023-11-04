#모듈
from flask import Blueprint,render_template,request,redirect,session,url_for,flash
import re

#DB 모듈
from Apps.crud.model import User
from Apps.app import db
from datetime import datetime
from uuid import uuid4


# 객체 생성
auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/auth"
)

# 로그인 페이지
@auth.route("/login")
def login():
    return render_template("auth/login.html")

# 사용자가 로그인 시
@auth.route("/login_done",methods=["POST"])
def login_done():

    # POST로 정보 받음
    email = request.form["email"]
    pw = request.form["pw"]

    try:
        # 로그인 성공시
        login_check=User.query.filter(User.email==email)
        if login_check[0].password ==pw:
            # 세션에 name 추가됨
            session["name"]=login_check[0].username
            session["uuid"]=login_check[0].uuid
            session["email"]=login_check[0].email
            return redirect(url_for("index"))
        # 로그인 실패 시
        else:
            flash("일치하지 않는 정보입니다",category="error")
            return redirect("login")
    # 로그인 실패 시
    except:
        flash("일치하지 않는 정보입니다",category="error")
        return redirect("login")

# 로그아웃 시 session name 제거됨
@auth.route("/logout")
def logout():
    session.pop('name', None)
    return redirect("/")

# 회원가입 페이지
@auth.route("/signup")
def signup():
    return render_template("auth/signup.html")

# 회원가입 정보를 전달할 때
@auth.route("/signup_done",methods=["POST"])
def signup_done():
    #post로 정보를 받음
    name=request.form["name"]
    email = request.form["email"]
    pw = request.form["pw"]
    check=re.compile('@.*[.]')

    if not re.search(check,email):
        flash("이메일 주소 양식이 맞지 않아요",category="error")
        return redirect("signup")
    else:
        try:
            #email 기준으로 중복 검사
            user= User(uuid =str(uuid4()),username = name, email=email,password = pw,created_at =datetime.now())
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        
        except:
            # 회원가입 실패 시
            flash("이미 존재하는 이메일입니다",category="error")
            return redirect("signup")