# -*- coding: utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot


@qqbotslot
def onQQMessage(bot, contact, member, content):
    # print(bot)
    # print(contact)
    # print(member)
    # print(content)
    # if contact == '群\"botTest\"':
    if content == '机器人在不在':
        bot.SendTo(contact, '在的 在的')
    elif content == '机器人阔步阔耐':
        bot.SendTo(contact, '非常阔耐')
    elif content == '你走 我不要你了':
        bot.SendTo(contact, '机器人走了,并关上了门')
        bot.Stop()
    # elif contact == '好友\"、Joker\"':
    #     bot.SendTo('群\"botTest\"','来自、Joker的消息:'+contact)
    #     pass


if __name__ == '__main__':
    RunBot()
