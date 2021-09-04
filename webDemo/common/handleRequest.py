import json
import urllib.parse
from urllib3 import encode_multipart_formdata

import requests

class handle_request():
    def __init__(self):
        self.session=requests.Session()
    def request_data(self,method,url,params=None,data=None,files=None,headers=None,cookies=None,session=None):
        method=method.lower()
        if isinstance(headers,str):
            headers=eval(headers)
        if isinstance(params,str):
            params=eval(params)
        if method=="post":
            if headers["Content-Type"]=="application/json":
                return self.session.request(method,url,data=json.dumps(json.loads(str(data).replace("'",'\"'),strict=False),ensure_ascii=False,separators=(',',':')).encode("utf-8"),headers=headers,cookies=cookies)
            elif headers["Content-Type"]=="application/x-www-form-urlencoded":
                return self.session.request(method,url,data=urllib.parse.urlencode(json.loads(str(data).replace("'",'\"'),strict=False).encode("utf-8")),headers=headers,cookies=cookies)
            elif headers["Content-Type"]=="multipart/form-data":
                encode_data=encode_multipart_formdata(data)
                headers["Content-Type"]=encode_data[1]
                return self.session.request(method,url,data=encode_data[0],headers=headers,cookies=cookies)
            else:
                print("请添加请求头类型")
        elif method=="get":
            return self.session.request(method,url,params=params,headers=headers,allow_redirects=False)
        else:
            print("请添加请求方式")


