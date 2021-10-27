# -*-coding:euc-kr

import time
import random
import os

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �������� ���� ������ �����մϴ�.
NUM_SAMPLES = 100

# ������ ������ ���� �̸��� �����մϴ�.
RESULT_FOLDER = "personal_info"

# �̸��� ������ ����� ���� ���ڵ��� �����մϴ�.
alphabet_sample = "abcdefghijklmnopqrstuvwxyzAMCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
alphabet_sample2 = "abcdefghijklmnopqrstuvwxyz1234567890"
num_sample = "123456890"


# �������� ���õ� ���� ���ڸ� �����ϴ� �Լ��Դϴ�.
def random_string(length1, length2):
    result = ""
    for i in range(length1):
        result += random.choice(alphabet_sample)

    result += "@"

    for i in range(length2):
        result += random.choice(alphabet_sample)

    result += ".com"

    return result


# �̸� ������ ����� ���� ���ڵ��� �����մϴ�.
first_name_sample = "���̹�������������������"
middle_name_sample = "���¼��������������δ�"
last_name_sample = "�������ر�������������ǥ"


# �������� ��� �̸��� �����ϴ� �Լ��Դϴ�.
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


# ������� ������ ������ �����մϴ�.
if not os.path.exists(RESULT_FOLDER):
    os.makedirs(os.path.join(RESULT_FOLDER))

# �������� ������ �ڵ����� �����ϴ� �κ��Դϴ�.
# NUM_SAMPLES ȸ����ŭ �ݺ��մϴ�.
# �̸��׸�, NUM_SAMPLES�� 100�̸� ������ �������� ������ 100ȸ �ݺ��մϴ�.
for i in range(NUM_SAMPLES):
    # �������� ��� �̸��� �����մϴ�.
    name = random_name()

    # ����� ������ �̸��� �����մϴ�.
    filename = str(i + 1) + "_" + name

    # ����� ������ �����մϴ�. �� �� ������ �����˴ϴ�.
    filepath = os.path.join("./{a}".format(a=RESULT_FOLDER), "{b}.txt".format(b=filename))
    f = open(filepath, 'w', encoding="UTF8")

    # ����� ���Ͽ� �̸��� �����մϴ�.
    f.write("�̸� : {a}".format(a=name) + "\n")

    # ����� ���Ͽ� �������� ������ ���̸� �����մϴ�.
    f.write("���� : {a}".format(a=random.randint(18, 60)) + "\n")

    # ����� ���Ͽ� �������� ������ �̸����� �����մϴ�.
    f.write("email : {a}".format(a=random_string(random.randint(4, 8), random.randint(3, 5))) + "\n")

    # ����� ���Ͽ� �������� ������ �μ����� �����մϴ�.
    f.write("�μ� : {a}".format(a=random_depart()) + "\n")

    # ����� ���Ͽ� �������� ������ �ڵ��� ��ȣ�� �����մϴ�.
    f.write("��ȭ��ȣ : {a}".format(a=random_phone()) + "\n")

    # ����� ���Ͽ� �������� ������ ������ �����մϴ�.
    f.write("���� : {a}".format(a=random.choice("����")))

    # ����� ���� ������ �������մϴ�.
    f.close()

# �۾� ���� �޼����� ����մϴ�.# print("Process Done.")
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print(end_time - start_time)
