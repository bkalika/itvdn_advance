from datetime import timedelta
import redis

# setex: "SET" with action durability

r = redis.Redis()
r.setex(
    "runner",
    timedelta(minutes=1),
    value="now you see me, now you don't"
)
