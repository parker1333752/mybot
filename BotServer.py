#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
#默认使用个税查询技能， 如果需要切换自己的技能  注意需要要更换成自己的Bot
# from dueros.samples.personal_income_tax.Bot import Bot
from speech_mail.Bot import Bot

def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
    print('request_body = %s\n' % request_body)
    if not request_body:
        return writeResponse(start_response, '未获取到请求数据')

    bot = Bot(request_body)
    #添加错误回调方法
    bot.set_callback(callback)
    #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
    bot.init_certificate(environ).enable_verify_request_sign()
    # bot.initCertificate(environ).disableVerifyRequestSign()
    #设置私钥
    bot.set_private_key(priKey)

    body_str = bot.run()

    return writeResponse(start_response, body_str)

def writeResponse(start_response, body_str):

    body = body_str.encode('utf-8')

    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(body)))]
    status = '200 OK'

    start_response(status, response_headers)

    return [body]

def callback(data):
    print('>'*30)
    print(data)
    print('<'*30)

priKey = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAw67B+5ldepUCyLu5jnXnDIzqfnXMV8IfG+QbkEoQFaweC4nc
SIzNe8TCKxzPhLdCfOAXfzKPNJbxQJ4NXl5KFVweasQHUW+C+Mt6AxwPybGuOKW3
qo0h34LLzcigbFpFZZdZtHkoz/X0d9zvG3S/8BjiLacIVRDoDsgDMdnuwVdOolYy
/cjHuQdkQgZI4evJyGCd8rwNIJv9QbyD4t+6NEMBsKKBeTupMZ9Kd5E74pExORuc
y1R2PFOqVCqb7QBibgzZhZK6WTwyFE2h1lsUGYoavSt3QVzLi9qzZtLvISltKnPv
hxbH//nUhNnXpsk/m5zXP2BBnvUqrDrO0QL+uwIDAQABAoIBAHx6vReqNhb2l7DO
Cnofcn0/XyRXF0h0SonZj9c35geDWBGK/0B/oW+seMAoMbKBSaBahVf697JCmvG6
GVMAtCvmT8snLGiXgT93YQR9Y2Wwy91pPe8WnIeskq0zhSmoOyEnKH9v25B/K6bc
OpbCrB62FZto+Bn1CUnt3mpl8kW2gS0BhdGrU7AQgZCO0i7nflYfbe9AaRZZsKrZ
nNAhyt4nFQWhyLbOnUdDz2+W0tzADX+RlhQD5Ip8PdhQmg7ihWAHpvPsk8LObis0
7NHdNCmgXzcZEmbu1p7DcyG77RHStq7rgj/pb53kTL69KSKwxL0FXAVVe/JMRnq0
oVRxOUECgYEA7OhaIU58xOfDtd9ceLAvoUbvXVCova4gL+Wogz8HlcwWxO50aFgb
GLaNQly0Obor3hsZld5dQKvICMqvemPZfSacLBX+vCHd4F4Dd0arB7ouwHoGl4P3
0VqP6PJ9rTQpTw2P7TgNKvlj3P5IrKRd5Ln0h8pFRcH8PK5lta3MaUsCgYEA03Pk
WWMMdcwLMLfqoOOavvbKOpYsQ3TGgINs1XxYMPuugh4vb0chDhrnDkLvXa3pGX8b
rBWqXOLvRytLV8W4CEbhlYbwjssfFwj77E2tL8lA8WjIrsM+syYRGEKmPyCR+jem
aXlGNhoNSU/Byix4cz+epqlT6Uh+A/G0QhzySlECgYEA09789DqQZTztD9OBjMHs
5uxcl/TR5Ek8qflXGoGdE//hASBM5SCeoxxn+siTuejg4JMV761dcr/udsZl5ywz
TrTgCKFnHvOezdDmgp6lyJReyW6YRJsWX5oBiBCOCv/STcvQQxPU2vEMuZCEiDm7
axpPMb3Y9AkHv3Esry2O2T8CgYEAu+canow0QGGn+A0XhQ19MAGix9k3UGJvGziu
+C9dN3oQIzSrtlkg+KXTeYrlpvuqTqvzbUJ7d7t6ImZIt6DN3x0NzZByKJI7+H5V
UDHemr5e5afV3edGynAjdMmVbjeFQTM+wC+ywtT3xZQIg55tEw0P8M478Owof1zE
cJPEg2ECgYBYMPW0VOVlyIIw866orT/xXOpL2kjaDyvzcxvqYXP2sWNffl/jNP22
TN5iNl7FITtRylGS7i6Kq2rqA5RVxfD6ax/J0BMyiVJsHSYvkmtKXPuqofsYcwpV
vq7YdwDRRfRf7mVJAp243gVUdHpBJO8ImOZLcTHeZZQsVpnECI706g==
-----END RSA PRIVATE KEY-----'''
