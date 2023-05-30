from drivegame_info import ginfo
from drivegame_map import create_map_line
from drivegame_draw import *
import tkinter.messagebox as msgbox

def init_game():
    global win

    win = create_window(ginfo)
    win.bind("<Left>", key_event_left)
    win.bind("<Right>", key_event_right)

    game_loop()
    win.mainloop()

def key_event_left(e):
    if ginfo["car"] > 0:
        ginfo["car"] -= 1

def key_event_right(e):
    if ginfo["car"] <= ginfo["cols"] -1:
        ginfo["car"] += 1

def game_loop():
    draw_map(ginfo)
    win.title("ドライブスコア：" + str(ginfo["score"]))

    map_data = ginfo["map_data"]
    v = map_data[ginfo["rows"] -2][ginfo["car"]]

    if v != 0:
        msgbox.showinfo(
            title="ゲームオーバー",
            message="コースアウトしました \n" +
            "スコア：" + str(ginfo["score"]))

        quit()

    ginfo["score"] += 10
    del(map_data[ginfo["rows"] -1])
    line = create_map_line(ginfo)
    map_data.insert(0,line)
    win.after(100, game_loop)

if __name__ == "__main__": init_game()
    
