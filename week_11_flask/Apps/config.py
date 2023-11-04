import os

# Application 구동에 필요한 설정들
# 예) DB URL, Table..
# 적용 -> Flask.config 인스턴스에 저장됨

# 디버그 모드 여부 설정값
DEBUG = True

BASE_DIR = os.path.dirname(__file__)
DB_NAME = "app.db"
DB_SQLITE_URI = f"sqlite:///{os.path.join(BASE_DIR,DB_NAME)}"
DB_MYSQL_URI = "mysql+pymysql://root:root@localhost:5005/proejct_1020"
DB_MARIA_URI ="mariadb+mariadbconnector://root:root@127.0.0.1:3306/project"

SQLALCHEMY_DATABASE_URI = DB_MARIA_URI
SQLALCHEMY_TRACK_MODIFICATIONS =False
