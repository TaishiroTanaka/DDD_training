from datetime import datetime
from datetime import timedelta
from datetime import timezone


def get_tweet_table_name() -> str:
    return 'Tweet'


def get_user_table_name() -> str:
    return 'user.json'


def get_timezone() -> timezone:
    return timezone(timedelta(hours=+9), 'JST')