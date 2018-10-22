import json

from handler_user import user_authentication_handler

print("******* ログイン *******")
user_id = input("ユーザーIDを入力してください↓\n")
password = input("パスワードを入力してください\n")

params_dict = {
    'user_id': user_id,
    'password': password
}
params_json = json.dumps(params_dict)
result = user_authentication_handler(params_json)

if result:
    file_write = open('front_status.json', 'w')
    json.dump(params_dict, file_write, indent=4)
    print("\n------- ログイン完了 -------")
else:
    print("\n------- ログインできませんでした -------")
