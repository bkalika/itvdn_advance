import redis

r = redis.Redis(db=5)
print(r.lpush("ips", "51.218.112.236"))
print(r.lpush("ips", "90.213.45.98"))
print(r.lpush("ips", "115.215.230.176"))
print(r.lpush("ips", "51.218.112.236"))
for _ in range(20):
    r.lpush("ips", "104.174.118.18")
