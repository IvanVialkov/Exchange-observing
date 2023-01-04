lisff = input().lower().split()
d = {}
for i in lisff:
    if lisff.count(i) == 1:
        d[i] = lisff.count(i)
    elif lisff.count(i) > 1:
        d[i] = lisff.count(i)
        while i in lisff:
            position_i = lisff.index(i) 
            lisff.pop(position_i)
for i in lisff:
    if i not in d:
        d[i] = lisff.count(i)
for key, value in d.items():
    print(key, value)
