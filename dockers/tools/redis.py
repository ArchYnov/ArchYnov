import base64
import redis

class RedisClient():
    def __init__(self) :
        # connect to redis
        self.client = redis.Redis(host="redis", port=6379)

    def create_key_value(self, key, value):
        """insert in base redis
        args :
            key [str] : key associated value
            value [str] : value of credential
        """

        self.client.set(key, base64.b64encode(value.encode()))


    def get_value_by_key(self, keys):
        """  get value by key in base redis
        args :
            keys [list] : list of different key
        return [dict] : dict of credential
        """
        dico = {}
        for key in keys:
            value = self.client.get(key)
            dico[key] = base64.b64decode(value).decode("utf-8")
        return dico


    