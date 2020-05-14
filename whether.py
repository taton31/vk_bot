import pyowm
import config


class Weather:
    @staticmethod
    def get_weather_today(city: str = "moscow") -> list:
                
        owm = pyowm.OWM(config.API_wether)  
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
  

        # Weather details
        w.get_wind()                  # {'speed': 4.6, 'deg': 330}          # 87
        w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}


        result = 'В городе ' + city + '\n'
        result = result + ('Температура от ' + str(w.get_temperature('celsius')['temp_min']) + ' до ' + str(w.get_temperature('celsius')['temp_max'])) + ' ' +  u'\xb0' + 'C' + '\n'
        result = result + 'Ветер: ' + str(w.get_wind()['speed']) + ' метров в секунду ' + '\n'
        return result