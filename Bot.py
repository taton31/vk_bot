# Импортируем созданный нами класс Server
from serv import Server
import random
import sys
import config 


random.seed()

server = Server(config.vk_api_token, config.group_id, config.server_name)

#server.test(config.my_ID, random.randint(0,sys.maxsize))

server.start()