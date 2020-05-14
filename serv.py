import vk_api.vk_api
import config 
import random
import json
import keyboards
import command

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class Server:

    def __init__(self, api_token, group_id, server_name="apta_j"):

        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)
        
        # Для использования Long Poll API
        self.longpoll = VkBotLongPoll(self.vk, group_id)   

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, rand_id, message, Keyboard=None):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        random_id: если сообщение с таким random_id уже было отправлено, то новое сообщение не отправится
        :return: None
        """
        return self.vk_api.messages.send(peer_id=send_id,
                                  message=message,
                                  random_id=rand_id,
                                  Keyboard=Keyboard
                                  )

    def test(self, ID,f):
        # Посылаем сообщение пользователю с указанным ID
        return self.send_msg(ID,f, "Привет-привет!", Keyboard=open(config.path_to_keyboard + "/default.json", "r", encoding="UTF-8").read())


    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return [self.vk_api.users.get(user_id=user_id)[0]['first_name'],self.vk_api.users.get(user_id=user_id)[0]['last_name']]

    
    def get_user_city(self, user_id):
        """ Получаем город пользователя"""
        return self.vk_api.users.get(user_id=user_id, fields="city")[0]["city"]['title']

    def get_buttons(self, name):
        keyboard = json.dumps(keyboards.Keys[name], ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard
    


    def start(self):
        commander = command.Commander()
        for event in self.longpoll.listen():   # Слушаем сервер
            
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.vk.method("messages.send", commander.get(self, event))


    


