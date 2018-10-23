import json

from handler_tweet import register_tweet_handler


content = input("いまどうしてる？\n")

file_read = open('front_status.json')
front_status = json.load(file_read)
params_dict = {
    'content': content,
    'user_id': front_status['user_id'],
}
params_json = json.dumps(params_dict)

result = register_tweet_handler(params_json)
print("\n------- " + result + "-------")
