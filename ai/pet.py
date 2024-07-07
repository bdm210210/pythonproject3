import requests
import base64
import cv2 as cv
import json

def pet_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image}
    access_token = '24.bf80ba093ebfdea13d9639164d50fa46.2592000.1722775112.282335-89935789'
    request_url = f"{request_url}?access_token={access_token}"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        data = response.json()
        names_scores = [f"动物名称: {item['name']}, 置信度: {item['score']}" for item in data.get('result', [])]
        return "\n".join(names_scores)  # 返回所有动物名称和置信度的字符串表示，每个名称换行
    return "未检测到动物信息"
