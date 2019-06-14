import configparser
import requests
import wxpy
import platform

#Initial Configuration
Bot = wxpy.Bot

# #Read Configuration Document
# cfg = configparser.ConfigParser()
# cfg.read("./config.ini",encoding="UTF-8")
#
# #Configure Target Wechat Username
# target_user_name = cfg.get("configuration","target_wechat_name")
#
# #Configure Target Chatting Time
# morning_chat = cfg.get("configuration","good_morning_chat")
# night_chat = cfg.get("configuration","good_night_chat")

#Configure Target Birthday
# birthday_month = cfg.get("configuration","birth_month")
# birthday_day = cfg.get("configuration","birth_day")

#Start Wechat Bot
if 'Windows' in platform.system():
    bot = Bot()
elif 'Darwin' in platform.system():
    bot = Bot()
elif 'Linux' in platform.system():
    bot = Bot(console_qr=2,cache_path=True)
else:
    print('Unable to detect the operating system')

#Get Inspiring Sentences
def get_words():
    r = requests.get('http://open.iciba.com/dsapi')
    note = r.json('note')
    content = r.json('content')
    return note,content

message_monitor = bot.friends().search(target_user_name)

@bot.register(chats=message_monitor,except_self=False)
def print_others(msg):
    print(msg.text)

    #Emotion Analysis
    post_data = {
        'data':msg.text
    }
    response = requests.post('https://bosonnlp.com/analysis/sentiment?analysisType=',data = post_data)
    data = response.text

    #Emotion Regulation
    now_mod_rank = data.split(','[0]).replace('[[','')
    print(now_mod_rank)

    mod_message = u"Target's emotion analysis report: score is {0}".format(now_mod_rank)

