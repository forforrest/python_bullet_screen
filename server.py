# -*-coding:utf-8-*-
# auther : 'forrest'
# created at : 2018-08-05 => 22:14

import redis


def init_redis():
    redis_client = redis.Redis()
    ps = redis_client.pubsub()
    ps.subscribe("bullet_test")
    return ps


if __name__ == '__main__':
    rc = init_redis()
    while True:
        try:
            message = rc.get_message()
        except:
            message = None
            pass
        if message:
            print message
