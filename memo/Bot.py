#!/usr/bin/env python3
# -*- encoding=utf-8 -*-
# description:
# author: Sijun Li
# create_time: 2018/8/19

"""
    desc: The memo Bot.
"""

from dueros.Bot import Bot


class Bot(Bot):
    def __init__(self, data):
        super(Bot, self).__init__(data)
        self.add_launch_handler(self.launchRequest)

    def launchRequest(self):
        return {
            'outputSpeech': r'欢迎进入思君的备忘录'
        }
