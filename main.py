from board import *

def create_board():
    for x in range(BOARD_SIZE + Game.chapter - 1):
        for y in range(BOARD_SIZE):
            c = Cell(x, y)
            c.create_label(board_frame)
            c.label_obj.grid(row=y, column=x, padx=2, pady=2)
    Cell.enemy_count = (BOARD_SIZE + Game.chapter - 1)*(BOARD_SIZE)//(6 - DIFFICULTIES.index(Game.difficulty))
    Cell.randomize_enemies()
    Cell.cell_count = BOARD_SIZE*(BOARD_SIZE + Game.chapter - 1) - Cell.enemy_count
    remaining_tiles.label_obj.configure(text=f"REMAINING TILES\n{Cell.cell_count}")
    enemies.label_obj.configure(text=f"ENEMIES LEFT\n{Cell.enemy_count}")
    chapter.label_obj.configure(text=f"CHAPTER {Game.chapter}")

def start_game(*event):
    Audio.select()
    Cell.all = []
    Game.lost_or_won = False
    Game.difficulty = difficulty.label_obj.cget("text")
    Game.style = style.label_obj.cget("text")

    difficulty.label_obj.grid_remove()
    style.label_obj.grid_remove()
    start.label_obj.grid_remove()

    Cell.define_tiles(Game.style, Game.chapter)
    create_board()

    new_game_btn.label_obj.grid(row=0, column=1, padx=10)
    side_screen.frame_obj.grid(row=1, column=0)
    main_screen.frame_obj.grid(row=1, column=1)

def new_game(*event):
    Audio.select()
    #mixer.music.stop()
    Game.chapter = 1
    side_screen.frame_obj.grid_remove()
    main_screen.frame_obj.grid_remove()
    new_game_btn.label_obj.grid_remove()

    next_chapter.label_obj.place_forget()
    game_over.label_obj.place_forget()
    game_end.label_obj.place_forget()

    for widget in board_frame.winfo_children():
        widget.destroy()

    for cell in Cell.all:
        del cell.label_obj
        del cell

    difficulty.label_obj.grid(row=0, column=1, padx=10)
    style.label_obj.grid(row=0, column=2, padx=10)
    start.label_obj.grid(row=0, column=3, padx=10)

def begin_next_chapter(*event):
    Game.chapter += 1
    next_chapter.label_obj.place_forget()
    start_game()

root = Tk()

# window settings
root.configure(bg='black')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Fog of War')
root.resizable(False, False)
root.grid_propagate(False)

# default style for all widgets
root.option_add("*Font", FONT)
root.option_add("*background", "black")
root.option_add("*foreground", "white")

# Frames
top_screen = Screen("top", root, (WIDTH-20), 70)
top_screen.frame_obj.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

side_screen = Screen("side", root, (0.25*WIDTH - 20), (HEIGHT-100))
main_screen = Screen("main", root, (0.75*WIDTH - 20), (HEIGHT-100))

board_frame = Frame(main_screen.frame_obj)
board_frame.place(relx=0.5, rely=0.4, anchor="center")

# top_screen
top_screen.frame_obj.columnconfigure(0, weight=1)

title = Text("Fog of War", top_screen)
title.label_obj.grid(row=0, column=0, padx=10, pady=10, sticky='w')

difficulty = Text(DIFFICULTIES, top_screen, True, 10)
difficulty.label_obj.grid(row=0, column=1, padx=10)
difficulty.label_obj.bind("<Button-1>", difficulty.change_option)

style = Text(STYLES, top_screen, True, 10)
style.label_obj.grid(row=0, column=2, padx=10)
style.label_obj.bind("<Button-1>", style.change_option)

start = Text("START", top_screen, True, 10)
start.label_obj.grid(row=0, column=3, padx=10)
start.label_obj.bind("<Button-1>", start_game)

new_game_btn = Text("NEW GAME", top_screen, True, 10)
new_game_btn.label_obj.bind("<Button-1>", new_game)

# side_screen
side_screen.frame_obj.columnconfigure(0, weight=1)
side_screen.frame_obj.rowconfigure((0,1,2,3), weight=1)

chapter = Text("CHAPTER 1", side_screen)
chapter.label_obj.grid(row=0, column=0)

remaining_tiles = Text("REMAINING TILES\n", side_screen)
remaining_tiles.label_obj.grid(row=1, column=0)
Text.tiles_text = remaining_tiles

enemies = Text("ENEMIES LEFT\n5", side_screen)
enemies.label_obj.grid(row=2, column=0)
Text.enemies_text = enemies

next_chapter = Text("NEXT CHAPTER", main_screen, True)
next_chapter.label_obj.bind("<Button-1>", begin_next_chapter)
Text.next_chapter = next_chapter

game_over = Text("GAME OVER", main_screen)
Text.game_over = game_over

game_end = Text("YOU WON!", main_screen)
Text.game_end = game_end

# Change the following variable to True if you
# want to know easily where the enemies are
Game.DEBUGGING = False

# mainloop
root.mainloop()