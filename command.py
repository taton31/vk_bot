import vk_api.vk_api
import timetable
import json
import keyboards
import irregular_V
from whether import Weather


class Commander:   #1 - 3 forms , 2 - translate
    def __init__(self, Event = None):
        self.mode=-1
        event = Event
        self.ret={}

    def get_buttons(self, name):
        keyboard = json.dumps(keyboards.Keys[name], ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard


    def Set (self, Event):
        event=Event
        sms=event.object.message['text']
        self.mode=self.modes(sms)


    def modes(self, event):
        if event.object.message['text'] == '3 формы глагола':
            return 1
        elif event.object.message['text'] == 'Назад':
            return 0
        else:
            return event.object.message['text']

    
    def get(self, serv, Event):
        event=Event
        
        if self.modes(event) not in [1] and self.mode != 1:
            if event.object.message['text'] == "Начать":
                self.ret['message'] = 'Привет!'
                self.ret["random_id"] = 0
                self.ret["peer_id"] = event.object.message['peer_id']
                self.ret["keyboard"] = self.get_buttons('start')
                return self.ret
            
            if event.object.message['text'] == "Расписание":
                self.ret['message'] = timetable.Timetable()
                self.ret["random_id"] = 0
                self.ret["peer_id"] = event.object.message['peer_id']
                self.ret["keyboard"] = self.get_buttons('start')
                return self.ret
            
            elif event.object.message['text'] == 'Погода':
                user_id = event.object.message['peer_id']
                city = serv.get_user_city(user_id)
                self.ret['message'] = Weather.get_weather_today(city)
                self.ret["random_id"] = 0
                self.ret["peer_id"] = event.object.message['peer_id']
                self.ret["keyboard"] = self.get_buttons('start')
                return self.ret


            else:
                self.ret['message'] = "Команда не распознана"
                self.ret["random_id"] = 0
                self.ret["peer_id"] = event.object.message['peer_id']
                self.ret["keyboard"] = self.get_buttons('start')
                return self.ret

        elif self.mode != 1 and self.modes(event) == 1:    
            self.ret['message'] = "Введите неправильный глагол"
            self.ret["random_id"] = 0
            self.ret["peer_id"] = event.object.message['peer_id']
            self.ret["keyboard"] = self.get_buttons('go_back')
            self.mode=self.modes(event)
            return self.ret  

        elif self.mode==1:
            if self.modes(event) == 0:
                self.ret['message'] = "Возврат в главное меню"
                self.ret["random_id"] = 0
                self.ret["peer_id"] = event.object.message['peer_id']
                self.ret["keyboard"] = self.get_buttons('start')
                self.mode=self.modes(event)
                return self.ret  
            else:
                self.ret['message'] = irregular_V.get_verb(event.object.message['text'])
                self.ret["random_id"] = 0
                self.ret["peer_id"] = event.object.message['peer_id']
                self.ret["keyboard"] = self.get_buttons('go_back')
                return self.ret

        

