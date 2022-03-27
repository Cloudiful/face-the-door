# coding=utf8
import base64
import requests
import os.path
import numpy as np
import cv2 as cv
from aip import AipFace
from time import sleep
import data


# 开始检测人脸，每10帧检测一次，检测到5张人脸后返回主程序，并保存人脸图像至image文件夹下.
def capture():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)  # set Width
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)  # set Height
    cap.set(cv.CAP_PROP_FPS, 25)

    print("开始检测人脸")
    frame = 0
    detected = 0
    faceCascade = cv.CascadeClassifier('/usr/local/lib/python3.9/dist-packages/cv2/data'
                                       '/haarcascade_frontalface_default.xml')

    while True:
        frame += 1
        ret, img = cap.read()
        img = cv.flip(img, 0)

        if frame % 10 == 0:  # every 10 frames
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(20, 20)
            )
            # print(faces)
            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                detected += 1
                print("已捕获" + str(detected) + "张人脸图像")

        # cv.imshow('video', img)
        data.cameraFeed = img  # send img into cameraFeed for pygame

        if detected != 0:  # 捕获到人脸后将其保存至images文件夹中
            cv.imwrite(os.path.join('./images/', 'detected face ' + str(detected) + '.jpg'), img)

        if detected >= 5:  # 捕获到五张人脸图片或按ESC键时退出
            break

    cap.release()
    print("人脸检测完毕，已保存5张图片待处理。")


# 调用百度云API，对之前保存的人脸图像进行比对，并输出结果
def baidu_api():
    APP_ID = '25749430'
    API_KEY = 'gn1iBNz9gjz510x0bzykaGqp'
    SECRET_KEY = 'cQTtGIA2GoykQZZ52f5NPgUdH5GivRSN'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    name = []  # 保存五张图片的人名
    score = np.arange(0, 5, dtype=np.float)  # 保存五张图片的分数
    liveness = np.arange(0, 5, dtype=np.float)  # 保存五张图片的liveness

    for n in range(5):  # 分别读取之前捕获的五张图片
        file = open('./images/detected face ' + str(n + 1) + '.jpg', 'rb')
        image = base64.b64encode(file.read())

        # 获取人脸比对结果
        result_who = client.search(str(image, 'utf-8'), 'BASE64', 'Resident')
        if result_who['error_msg'] == 'SUCCESS':  # 如果成功
            name.append(result_who['result']['user_list'][0]['user_id'])  # 获取名字
            score[n] = result_who['result']['user_list'][0]['score']  # 获取相似度
        else:
            print("验证失败: " + result_who['error_msg'])

        # 获取活体验证结果
        result_liveness = client.faceverify([
            {
                'image': str(image, 'utf-8'),
                'image_type': 'BASE64',
            }
        ])
        if result_liveness['error_msg'] == 'SUCCESS':
            liveness[n] = result_liveness['result']['face_liveness']  # 获取活体值
        else:
            print("活体验证失败: " + result_liveness['error_msg'])

        sleep(0.2)  # 防止QPS超过免费限制造成Timeout的情况

    name_result = name[0]
    for i in range(0, 5):
        if name[i] != name_result or score[i] <= 70:
            return "error"

    print("认证成功，欢迎：" + name_result)
    return name_result


# test if device is online
def test_network():
    try:
        html = requests.get("https://www.baidu.com", timeout=1)
        print(html.text)
    except:
        return False
    return True


def recognition():
    fail = 0

    # 如果设备已联网，则使用百度API进行人脸比对
    if test_network():
        print("已联网，将使用百度API。")
        while fail < 3:
            # 调用Opencv进行人脸检测
            if capture() == "pwd":
                return "pwd"
            result = baidu_api()  # 调用百度API进行人脸比对与活体检测
            if result != "error":
                return "success"
            else:
                print("认证失败，请重新尝试。")

                fail += 1
        if fail >= 3:
            print("尝试次数过多，系统暂时锁定......")
            return "error"

    # 设备脱机
    else:
        print("当前未连接互联网......")
        return "error"
