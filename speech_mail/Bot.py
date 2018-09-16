#!/usr/bin/env python3
# -*- encoding=utf-8 -*-
# description: send mail.
# author: Sijun Li
# create_time: 2018/9/02

"""
    desc: Send mail.
"""

from dueros.Bot import Bot
# import User_DB as db


class Bot(Bot):
    def __init__(self, data):
        super(Bot, self).__init__(data)
        self.add_launch_handler(self.launchRequest)
        self.add_intent_handler('profile', self.bind_profile)
        self.add_intent_handler('send', self.send_mail)

    def launchRequest(self):
        return {
            'outputSpeech': r'欢迎使用邮件发送功能'
        }

    def bind_profile(self):
        '''
        绑定用户信息
        '''
        device_id = self.request.get_device_id()
        user_id = self.request.get_user_id()
        user_name = self.get_slots('name')
        user_code = self.get_slots('code')

        # TODO: check if device_uuid in DB, if not, add it.
        print('device_id', device_id)
        print('user_id', user_id)
        print('user_name', user_name)
        print('user_code', user_code)

        return {
            'outputSpeech': '好的我记住你了%s' % user_name
        }
