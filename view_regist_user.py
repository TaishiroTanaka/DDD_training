import json

from handler_user import register_user_handler

print("******* ユーザー登録 *******")
user_id = input("ユーザーIDを半角英数で入力してください↓\n")
name = input("ユーザー名を入力してください↓\n")

params_dict = {
    'user_id': user_id,
    'name': name
}
params_json = json.dumps(params_dict)
result = register_user_handler(params_json)

print("\n------- " + result + "-------")
