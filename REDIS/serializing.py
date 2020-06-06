import json

import redis
import yaml
from pprint import pprint
from collections.abc import MutableMapping

r = redis.Redis()
restaurant_484272 = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}

r.set(484272, json.dumps(restaurant_484272))

pprint(json.loads(r.get(484272)))
print(yaml.dump(restaurant_484272))


def setflat_skeys(
        r: redis.Redis,
        obj: dict,
        prefix: str,
        delim: str = ":",
        *,
        _autopfix=""
) -> None:
    """Выравнивает `obj` и стaвит полученную пару поле-значение в `r`.

    Вызывает `.set()` для записи в экземпляре Redis на месте и возвращает None.

    `prefix` - необязательный str, который ставит префикс перед всеми ключами.
    `delim` - разделитель, который разделяет соединенные, сплющенные ключи.
    `_autopfix` используется в рекурсивных вызовах созданных вложенных ключей.

    Глубоко вложенные ключи должны быть типов str, bytes, float или int.
    В противном случае возникает ошибка TypeError.
    """
    allowed_vtypes = (str, bytes, float, int)
    for key, value in obj.items():
        key = _autopfix + key
        if isinstance(value, allowed_vtypes):
            r.set(f"{prefix}{delim}{key}", value)
        elif isinstance(value, MutableMapping):
            setflat_skeys(
                r, value, prefix, delim, _autopfix=f"{key}{delim}"
            )
        else:
            raise TypeError(f"Unsupported value type: {type(value)}")


r.flushdb() # clean DB: clean all old records
setflat_skeys(r, restaurant_484272, 484272)

for key in sorted(r.keys("484272")): # filtering this pattern
    print(f"{repr(key):35}{repr(r.get(key)):15}")

print(r.get("484272:address:street:line1"))
