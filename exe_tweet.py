import json

from handler_tweet import regist_tweet_handler


content = input("いまどうしてる？\n")

content_dict = {'content': content}
content_json = json.dumps(content_dict)
# print(type(content_json))

# print(content_json)

result = regist_tweet_handler(content_json)
print("\n------- " + result + "-------")
