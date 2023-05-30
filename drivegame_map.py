from random import randint

def create_map_line(ginfo):
    if randint(0,99) < 10:
        ginfo["dir"] = randint(-1,1)

    cx, sz, gdir = (ginfo["cx"], ginfo["size"], ginfo["dir"])
    if(gdir == -1 and cx <= 1):
    	ginfo["dir"] *= -1
    if(gdir == 1 and (cx + sz) >= (ginfo["cols"] -1)):
    	ginfo["dir"] *= -1

    ginfo["cx"] += ginfo["dir"]

    line = [1] * ginfo["cols"]

    for i in range(ginfo["size"]):
        line[i + ginfo["cx"]] = 0
    return line

def create_map(ginfo):
    map_data = []
    for i in range(ginfo["rows"]):
        line = create_map_line(ginfo)
        map_data.insert(0,line)
    return map_data

if __name__ == "__main__":
    ginfo = {
        "rows": 20,
        "cols": 30,
        "dir":0,
        "cx":10,
        "size":8
        }
    map_data = create_map(ginfo)
    for row in map_data: print(row)
