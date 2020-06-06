import bz2

import redis

blob = "i have a lot to talk about" * 10000
print(len(blob.encode("utf-8")))

r = redis.Redis()
# set up zip row as value
r.set("msg:500", bz2.compress(blob.encode("utf-8")))
r.get("msg:500")
print(len(r.get("msg:500")))

print(260_000 / 122)

# Getting and decompressing values and confirmation comparison to the original
rblob = bz2.decompress(r.get("msg:500")).decode("utf-8")
print(rblob == blob)
