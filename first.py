# -*-coding:euc-kr

import time
import random
import os

# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 생성할 개인정보 파일 개수를 정의합니다.
NUM_SAMPLES = 100

# 정보를 저장할 폴더 이름을 정의합니다.
RESULT_FOLDER = "personal_info"

# 이메일 생성에 사용할 샘플 글자들을 정의합니다.
alphabet_sample = "abcdefghijklmnopqrstuvwxyzAMCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
alphabet_sample2 = "abcdefghijklmnopqrstuvwxyz1234567890"
num_sample = "123456890"


# 무작위로 선택된 영어 글자를 생성하는 함수입니다.
def random_string(length1, length2):
    result = ""
    for i in range(length1):
        result += random.choice(alphabet_sample)

    result += "@"

    for i in range(length2):
        result += random.choice(alphabet_sample)

    result += ".com"

    return result


# 이름 생성에 사용할 샘플 글자들을 정의합니다.
first_name_sample = "김이박최정강강강조윤장임"
middle_name_sample = "우상승서종현진진진현민다"
last_name_sample = "민혁빈준국진중주주주인표"


# 무작위로 사람 이름을 생성하는 함수입니다.
def random_name():
    result = ""

    result += random.choice(first_name_sample)

    result += random.choice(middle_name_sample)

    result += random.choice(last_name_sample)

    return result


def random_depart():
    result = ""
    for i in range(3):
        result += random.choice(alphabet_sample2)

    return result


def random_phone():
    result = "010-"
    for i in range(4):
        result += random.choice(num_sample)
    result += "-"
    for i in range(4):
        result += random.choice(num_sample)

    return result


# 결과물을 저장할 폴더를 생성합니다.
if not os.path.exists(RESULT_FOLDER):
    os.makedirs(os.path.join(RESULT_FOLDER))

# 개인정보 파일을 자동으로 생성하는 부분입니다.
# NUM_SAMPLES 회수만큼 반복합니다.
# 이를테면, NUM_SAMPLES가 100이면 무작위 개인정보 생성을 100회 반복합니다.
for i in range(NUM_SAMPLES):
    # 무작위로 사람 이름을 생성합니다.
    name = random_name()

    # 결과물 파일의 이름을 정의합니다.
    filename = str(i + 1) + "_" + name

    # 결과물 파일을 생성합니다. 텅 빈 파일이 생성됩니다.
    filepath = os.path.join("./{a}".format(a=RESULT_FOLDER), "{b}.txt".format(b=filename))
    f = open(filepath, 'w', encoding="UTF8")

    # 결과물 파일에 이름을 기재합니다.
    f.write("이름 : {a}".format(a=name) + "\n")

    # 결과물 파일에 무작위로 생성된 나이를 기재합니다.
    f.write("나이 : {a}".format(a=random.randint(18, 60)) + "\n")

    # 결과물 파일에 무작위로 생성된 이메일을 기재합니다.
    f.write("email : {a}".format(a=random_string(random.randint(4, 8), random.randint(3, 5))) + "\n")

    # 결과물 파일에 무작위로 생성된 부서명을 기재합니다.
    f.write("부서 : {a}".format(a=random_depart()) + "\n")

    # 결과물 파일에 무작위로 생성된 핸드폰 번호를 기재합니다.
    f.write("전화번호 : {a}".format(a=random_phone()) + "\n")

    # 결과물 파일에 무작위로 선정된 성별을 기재합니다.
    f.write("성별 : {a}".format(a=random.choice("남여")))

    # 결과물 파일 수정을 마무리합니다.
    f.close()

# 작업 종료 메세지를 출력합니다.# print("Process Done.")
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print(end_time - start_time)
