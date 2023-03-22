from tools.redis import RedisClient

client_redis = RedisClient()

client_redis.create_key_value("api_key_tmdb", "678b941591dc9bdb6ec1352563253fdd")
client_redis.create_key_value("api_key", "MyjgoENpH5NcIaNklNzKrbcBD")
client_redis.create_key_value("api_key_secret", "OFcquJlUYOYaOlwcNbSS59cDzI7ovxLZn92hGmivypL4FahtNk")
client_redis.create_key_value("access_token", "1377622154683019265-cbNJTqBWzPJ5CJDdUOVazLk518hOba")
client_redis.create_key_value("access_token_secret", "Qjo3HWA2DPz7pF2RjVgobTGG6m8OKtZLmiYBYYIfCZHoY")