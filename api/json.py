# -*- coding:utf-8 _*-
import json
json_string = '{"user_man": [{"name": "Peter"}, {"name": "xiaoming"}],' \
              '"user_woman": [{"name": "Ann"}, {"name": "zhangsan"}]}'

json_data = json.loads(json_string)
print(json_data.get("user_man"))
print(json_data.get("user_woman"))
print(json_data.get("user_man")[0].get("name"))
print(json_data.get("user_woman")[1].get("name"))