import smtplib
from email.message import EmailMessage  # MIME : ascii 코드를

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언3")
# --- 내용 부분 ---

message["Subject"] = "이것은 제목입니다"
message["From"] = "jmsmg3@gmail.com"
message["To"] = "jmsmg1@me.com"
# --- 헤더 부분 ---

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) # SSL보안방식을 사용하는 메일에는 SMTP_SSL을 사용한다
#  ---- 서버 연결 부분 --- 

smtp.login("jmsmg3@gmail.com","#####")
# ----- 로그인 부분 ----

smtp.send_message(message)

# --- 내용부분 ---

smtp.quit()
# --- 종료 부분