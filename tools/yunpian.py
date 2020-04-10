

import requests
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        # 需要传递的参数
        parmas = {
        "apikey": self.api_key,
        "mobile": mobile,
        "text": "【大家庭】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }
        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":

    yun_pian = YunPian("c60770e37f172c235b9b3c0380807108")
    yun_pian.send_sms("5201", "18388336183")