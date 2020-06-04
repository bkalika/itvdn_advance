import redis
import datetime

r = redis.Redis()
one = r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
print(one)
print(r.get("Bahamas"))
print(r.get("Bahamas").decode("utf-8"))

# will be error, due to key is date
today = datetime.date.today()
visitors = {"dan", "jon", "alex"}
# r.sadd(today, *visitors)

stoday = today.isoformat()
print(stoday)
print(r.sadd(stoday, *visitors))
print(r.smembers(stoday))
print(r.scard(today.isoformat()))

