import smtplib 
from email.message import EmailMessage  # MIME : ascii 코드를
import imghdr # 이미지 유형을 판단해주는 모듈
import re # 유효성 검사를 위한 정규표현식 ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 E-mail이 발송 되었습니다.")
    else:
        print("유효한 E-mail이 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언3")
# --- 내용 부분 ---

message["Subject"] = "이것은 제목입니다"
message["From"] = "jmsmg3@gmail.com"
message["To"] = "jmsmg1@me.com"
# --- 헤더 부분 ---

image = open("capture.PNG","rb") #rb ab wb (append binary)
# --- 이미지를 읽는 부분 ---
with open ("capture.PNG","rb") as image:  # open한 내용을 image로서 놓는 것
    image_file = image.read() # 이미지를 사용하고 자동으로 닫아줌

image_type = imghdr.what("capture",image_file)
# ---  확장자 판별 부분 ---
message.add_attachment(image_file, maintype="image", subtype=image_type)
# --- 이미지파일을 붙이는 부분 사진

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) # SSL보안방식을 사용하는 메일에는 SMTP_SSL을 사용한다
#  ---- 서버 연결 부분 --- 
smtp.login("jmsmg3@gmail.com","#####")
# ----- 로그인 부분 ----

# reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
# re.match(reg, "jmsmg1@me.com") # 적합성 검사 boolean

# smtp.send_message(message)
# --- 내용부분 ---
smtp.quit()
# --- 종료 부분