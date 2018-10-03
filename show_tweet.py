from handler_tweet import find_tweet_handler


tweet_list = find_tweet_handler()

print("\n******* ホーム *******")
for tweet in tweet_list:
    print("----------------------")
    print(tweet['create_date'])
    print(tweet['content'])

print("----------------------")
print("*******  End  *******")
