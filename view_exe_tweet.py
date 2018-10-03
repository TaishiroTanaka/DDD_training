import json

from handler_tweet import regist_tweet_handler


content = input("いまどうしてる？\n")

content_dict = {'content': content}
content_json = json.dumps(content_dict)
result = regist_tweet_handler(content_json)

print("\n------- " + result + "-------")
