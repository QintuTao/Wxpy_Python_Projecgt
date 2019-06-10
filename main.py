import configparser

#Read Configuration Document
cfg = configparser.ConfigParser()
cfg.read("./config.ini",encoding="UTF-8")

#Configure Target Wechat Username
target_user_name = cfg.get("configuration","target_wechat_name")

#Configure Target Chatting Time
morning_chat = cfg.get("configuration","good_morning_chat")
night_chat = cfg.get("configuration","good_night_chat")

#Configure Target Birthday
birthday_month = cfg.get("configuration","brith_month")
birthday_day = cfg.get("configuration","birth_day")
