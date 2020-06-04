# 1
capitals = {}
capitals["Bahamas"] = "Nassau"
capitals["Croatia"] = "Zagreb"

print(capitals.get("Croatia"))
print(capitals.get("Japan"))

# 2
capitals.update({
    "Lebanon": "Beirut",
    "Norway": "Oslo",
    "France": "Paris",
})

mset = [capitals.get(k) for k in ("Lebanon", "Norway", "Bahamas")]
print(mset)

# 3
print("Norway" in capitals)
print("Sweden" in capitals)

# 4 Type hesh

data = {
    "pythonscripts": {
        "url": "https://python-scripts.com/",
        "github": "pythonscripts",
        "fullname": "Python Scripts",
    }
}