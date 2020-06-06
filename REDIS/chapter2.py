# new tab or window

import datetime
import ipaddress

import redis

# here we set up out harmful IP-addresses
blacklist = set()
MAXVISITS = 15

ipwatcher = redis.Redis(db=5)

while True:
    _, addr = ipwatcher.blpop("ips")
    addr = ipaddress.ip_address(addr.decode("utf-8"))
    now = datetime.datetime.utcnow()
    addrts = f"{addr}:{now.minute}"
    n = ipwatcher.incrby(addrts, 1)
    if n >= MAXVISITS:
        print(f"Hat bot detected!: {addr}")
        blacklist.add(addr)
    else:
        print(f"{now}: saw {addr}")
    _ = ipwatcher.expire(addrts, 60)
