import json

from handler_user import regist_user_handler

print("******* ユーザー登録 *******")
name = input("ユーザー名を入力してください↓\n")

params_dict = {'name': name}
params_json = json.dumps(params_dict)
result = regist_user_handler(params_json)

print("\n------- " + result + "-------")