import requests
import logging as logger


class BaseApi:
    def send_api(self,req):
        req.update({'headers':{"X-Authorization":'Bearer '+self.get_token(),
                               "Content-Type":'application/json'}})
        # print(req)
        # logger.info(f"请求数据为======> {req}")
        r=requests.request(**req)
        # logger.info(f"响应数据为------>{r.text}")
        return r



    def get_token(self):
        url = 'https://thingsboard.stu.hogwarts.ceshiren.com/api/auth/login'
        param = {
            "username": 'mayunlong@ceshiren.com',
            "password": 'hogwarts'
        }
        r = requests.post(url, json=param,params=proxys)
        return r.json().get('token')

proxys = {

    'htttp': '127.0.0.1:8888',
    'https': '127.0.0.1:8888'

}