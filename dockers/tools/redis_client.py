import base64
import redis

class RedisClient():
    def __init__(self, host) :
        # connect to redis
        self.client = redis.Redis(host=host, port=6379)

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
            dico[key] = value.decode("utf-8")
        return dico

if __name__ == "__main__":
    client_redis = RedisClient(host="127.0.0.1")
    client_redis.create_key_value("api_key_tmdb", "678b941591dc9bdb6ec1352563253fdd")
    client_redis.create_key_value("api_key", "MyjgoENpH5NcIaNklNzKrbcBD")
    client_redis.create_key_value("api_key_secret", "OFcquJlUYOYaOlwcNbSS59cDzI7ovxLZn92hGmivypL4FahtNk")
    client_redis.create_key_value("access_token", "1377622154683019265-cbNJTqBWzPJ5CJDdUOVazLk518hOba")
    client_redis.create_key_value("access_token_secret", "Qjo3HWA2DPz7pF2RjVgobTGG6m8OKtZLmiYBYYIfCZHoY")
    print("insertion")