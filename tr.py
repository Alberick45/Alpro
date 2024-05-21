dict = {}
string = " place : pn + pnum , clas : cn + cnum"
pairs = string.split(",")

for pair in pairs:
    keys, values = pair.split(":")
    keys = keys.strip()
    values = values.split('+')
    dict[keys] = values
items = list(dict.keys())
print(items[1])
