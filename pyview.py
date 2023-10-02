from tkinter import *
from tkinter import ttk
import model
import maps

height, width = 150, 150
cell_size = 5
willUpdate = False
right_click_pos = [0, 0]

game = model.LifeGame(height, width)

def right_click_menu_handler(event):
    menu.tk_popup(event.x_root, event.y_root)
    right_click_pos[0] = event.x
    right_click_pos[1] = event.y

def start_handler(event):
    global willUpdate
    willUpdate = not willUpdate
    update()

def random_handler(event):
    global game,map_view
    game.randlife()
    map_view.delete(ALL)
    draw()

def clear_handler(event):
    global game,root,willUpdate
    game.clear_map()
    map_view.delete(ALL)
    draw()
    willUpdate = False

def load_map():
    global game,map_view,choice,right_click_pos
    x,y = right_click_pos[0]//cell_size,right_click_pos[1]//cell_size
    if choice.get() == 'Glider':
        game.load_map(maps.Glider,x,y)
    if choice.get() == 'Fan':
        game.load_map(maps.Fan)
    draw()

def update():
    global root, game, map_view,willUpdate
    map_view.delete(ALL)
    game.gen_next()
    draw()
    if willUpdate:
        root.after(100, update)


def draw():
    for y in range(0, game.height):
        for x in range(0, game.width):
            if game.map[y][x] == 1:
                map_view.create_rectangle(y*cell_size, x*cell_size,
                                          (y+1)*cell_size, (x+1)*cell_size,
                                          fill="black")


# init canvas
root = Tk()
root.title("Life Game")

map_view = Canvas(root, width=width*cell_size,
                  height=height*cell_size)
menu = Menu(root, tearoff=0)
menu.add_command(label="Load Model",command=load_map)
button_start = Button(root, text="Start Simulate", width=12)
button_clear = Button(root, text="Clear Map", width=12)
button_random = Button(root, text="Random Map", width=12)
label_map = Label(root, text="Map:")

choice = ttk.Combobox(root, width=30, state="readonly")
choice['values'] = ("Glider", "Fan")

button_start.bind("<Button-1>", start_handler)
button_random.bind("<Button-1>", random_handler)
button_clear.bind("<Button-1>", clear_handler)
map_view.bind("<Button-3>", right_click_menu_handler)

map_view.grid(row=0, columnspan=3)
button_clear.grid(row=1, column=2, pady=10)
button_random.grid(row=1, column=1, pady=10)
button_start.grid(row=1, column=0, pady=10)
choice.grid(row=2, column=1, pady=10)
label_map.grid(row=2, column=0, pady=10)

root.mainloop()
