#from vk_api.keyboard import VkKeyboard, VkKeyboardColor

remove = {"buttons":[],"one_time":True}

default = {
  "one_time": False,
  "buttons": [
      [{
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"1\"}",
                  "label": "Negative"
              },
              "color": "negative"
          },
          {
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"2\"}",
                  "label": "Positive"
              },
              "color": "positive"
          },
          {
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"2\"}",
                  "label": "Primary"
              },
              "color": "primary"
          },
          {
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"2\"}",
                  "label": "Secondary"
              },
              "color": "secondary"
          }
      ]
  ]
}

go_back = {
  "one_time": False,
  "buttons": [
      [
          {
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"1\"}",
                  "label": "Назад"
              },
              "color": "negative"
          }
      ]
  ]
}

Exit = {
  "one_time": False,
  "buttons": [
      [
          {
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"1\"}",
                  "label": "Exit"
              },
              "color": "negative"
          }
      ]
  ]
}

start = {
  "one_time": False,
  "buttons": [
      [{
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"1\"}",
                  "label": "Погода"
              },
              "color": "default"
          }],
          [{
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"2\"}",
                  "label": "Расписание"
              },
              "color": "default"
          }],
          [{
              "action": {
                  "type": "text",
                  "payload": "{\"button\": \"2\"}",
                  "label": "3 формы глагола"
              },
              "color": "default"
          }]
          
  ]
}

test = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Negative"
                },
                "color": "negative"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Positive"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Primary"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Secondary"
                },
                "color": "secondary"
            }
        ]
    ]
}

Keys={'remove': remove, 'default': default, 'exit': Exit, 'start': start, "go_back": go_back, "test": test}