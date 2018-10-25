import json

from handler_tweet import find_tweet_handler


file_read = open('front_status.json')
front_status = json.load(file_read)
params_dict = {
    'user_id': front_status['user_id'],
}
params_json = json.dumps(params_dict)

tweet_list = find_tweet_handler(params_json)

print("\nユーザー：" + params_dict['user_id'])
print("******* ホーム *******")
for tweet in tweet_list:
    print("----------------------")
    print(tweet['create_date'])
    print(tweet['content'])

print("----------------------")
print("*******  End  *******")
