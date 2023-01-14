import redis
from config.startupconfig import init_config
config=init_config
redisConn = redis.StrictRedis(host=config.redis.ip, port=config.redis.port, decode_responses=True)