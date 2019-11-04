# -*-coding:utf-8-*-
# auther : 'forrest'
# created at : 2018-08-05 => 22:14
import redis


def init_redis():
    redis_client = redis.Redis()
    return redis_client


if __name__ == '__main__':
    pring(123)
    rc = init_redis()

    while True:
        content = raw_input("input:")
        if content:
            rc.publish("bullet_test", content)
