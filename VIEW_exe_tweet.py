import json

import requests
import pprint


url_items = 'https://msiehe3350.execute-api.ap-northeast-1.amazonaws.com/dev/tweet'


content = input('いまどうしてる？\n')

file_read = open('front_status.json')
front_status = json.load(file_read)
item_data = {
    'content': content,
    'user_id': front_status['user_id'],
}

r_post = requests.post(url_items, json=item_data)

# pprint.pprint(r_post.json())
r_post_dict = r_post.json()
print('\n--- ' + r_post_dict['message'] + ' ---')
