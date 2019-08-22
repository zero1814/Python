import redis
from dianping.settings import REDIS_HOST,REDIS_PORT,REDIS_PASSWORD
class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
    
    def add(self,value):
        self.db.zadd('dianping_hpg',value)