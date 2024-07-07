import requests
import base64
import cv2 as cv
import json

def land_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image}
    access_token = '24.bf80ba093ebfdea13d9639164d50fa46.2592000.1722775112.282335-89935789'
    request_url = f"{request_url}?access_token={access_token}"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        data = response.json()
        print(data)
        # 处理返回结果
        result = data.get('result', {}).get('landmark', '未检测到地标信息')
        print(result)
        return result  # 返回地标信息
    return "未检测到地标信息"
