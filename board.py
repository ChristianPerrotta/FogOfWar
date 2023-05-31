from __future__ import annotations
import random
from settings import *
from pygame import mixer
from tkinter import Tk, Label, Frame
from PIL import Image, ImageTk

mixer.init()

class Audio:

    death_sound = mixer.Sound(SOUND_PATH + "death.mp3")
    change_sound = mixer.Sound(SOUND_PATH + "change.wav")
    select_sound = mixer.Sound(SOUND_PATH + "select.wav")

    def death():
        pass
        mixer.Sound.play(Audio.death_sound)

    def change():
        pass
        mixer.Sound.play(Audio.change_sound)

    def select():
        pass
        mixer.Sound.play(Audio.select_sound)


class Game:
    style: str = 'FE1'
    difficulty: str = 'Normal'
    chapter: int = 1
    enemy_count: int = 7
    lost_or_won = False
    
    DEBUGGING = False

    @staticmethod
    def win_chapter():
        Game.lost_or_won = True
        if Game.chapter == 5:
            Game.game_end()
        else:
            Text.next_chapter.label_obj.place(relx=0.5, rely=0.9, anchor="center")

    @staticmethod
    def game_end():
        Text.game_end.label_obj.place(relx=0.5, rely=0.9, anchor="center")

class Screen:
    def __init__(self, name: str, master: Tk, width, height) -> None:
        self.name = name
        self.frame_obj = Frame(
            master,
            width=width,
            height=height,
            highlightbackground="white",
            highlightthickness=2
            )
        self.frame_obj.grid_propagate(False)

class Text:

    enemies_text: Text = None
    tiles_text: Text = None
    next_chapter: Text = None
    game_over: Text = None
    game_end: Text = None

    def __init__(self, name, master: Screen,
                 hoverable: bool = False, width = False) -> None:
        if type(name) == str:
            self.name = name
        else:
            self.name = name[0]
            self.options = name
        self.label_obj = Label(master.frame_obj, text=self.name)
        if width:
            self.label_obj.configure(width=width)
        if hoverable:
            self.label_obj.bind("<Enter>", self.hover)
            self.label_obj.bind("<Leave>", self.leave)
    
    def hover(self, *event):
        self.label_obj.configure(font=FONT_UNDER)

    def leave(self, *event):
        self.label_obj.configure(font=FONT)

    def change_option(self, *event):
        Audio.change()
        option = self.label_obj.cget("text")
        index = self.options.index(option) + 1
        if index > len(self.options) - 1:
            index = 0
        self.label_obj.configure(text=self.options[index])

class Cell:

    all: list[Cell] = []
    enemy_count: int = 0
    cell_count = 0

    default_tile: ImageTk = None
    flag_tile: ImageTk = None
    enemy_tile: ImageTk = None
    tiles: list = []
    numbered_tiles: list = []

    def __init__(self, x, y, is_enemy = False):
        self.is_enemy = is_enemy
        self.is_flagged = False
        self.is_opened = False
        self.label_obj: Label = None

        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_label(self, master: Screen):
        lbl = Label(master)
        lbl.bind("<Button-1>", self.left_click)
        lbl.bind("<Button-3>", self.right_click)
        lbl.bind("<Enter>", self.hover)
        lbl.bind("<Leave>", self.leave)
        lbl.configure(image=Cell.default_tile)
        self.label_obj = lbl

    def hover(self, *event):
        if self.is_opened and not Game.lost_or_won:
            self.label_obj.configure(
                image=Cell.numbered_tiles[self.surrounded_cells_enemies_length]
                )
    
    def leave(self, *event):
        if self.is_opened:
            self.label_obj.configure(
                image=Cell.tiles[self.surrounded_cells_enemies_length]
                )


    def define_tiles(style, chapter):
        style_offset = STYLES.index(style)
        with Image.open(TILESET_PATH) as tileset:
            # default cell
            default = tileset.crop((0, 160, 16, 176))
            bigger_default = default.resize((64, 64), resample=Image.Resampling.NEAREST)
            Cell.default_tile = ImageTk.PhotoImage(bigger_default)

            # flagged cell
            flag = tileset.crop((0, 144, 16, 160))
            bigger_flag = flag.resize((64, 64), resample=Image.Resampling.NEAREST)
            Cell.flag_tile = ImageTk.PhotoImage(bigger_flag)

            # enemy cell
            enemy = tileset.crop((
                16*(Game.chapter) + 16*5*style_offset,
                16*9,
                16*(Game.chapter + 1) + 16*5*style_offset,
                16*10
                ))
            bigger_enemy =  enemy.resize((64, 64), resample=Image.Resampling.NEAREST)
            Cell.enemy_tile = ImageTk.PhotoImage(bigger_enemy)

            # tiles and numbered tiles
            Cell.tiles = []
            Cell.numbered_tiles = []

            for num in range(9):
                COORD = (
                    16*(Game.chapter) + 16*5*style_offset,
                    16*num,
                    16*(Game.chapter + 1) + 16*5*style_offset,
                    16*(num+1)
                    )
                cell = tileset.crop(COORD)

                number = tileset.crop((0, 16*num, 16, 16*(num+1)))
                num_cell = cell.copy()
                num_cell.paste(number, (0, 0), number.convert('RGBA'))

                bigger_cell = cell.resize((64, 64), resample=Image.Resampling.NEAREST)
                bigger_num_cell = num_cell.resize((64, 64), resample=Image.Resampling.NEAREST)

                Cell.tiles.append(ImageTk.PhotoImage(bigger_cell))
                Cell.numbered_tiles.append(ImageTk.PhotoImage(bigger_num_cell))

    def left_click(self, *event):
        if not Game.lost_or_won:
            if self.is_enemy:
                self.show_enemy()
            else:
                self.show_cell()
                if self.surrounded_cells_enemies_length == 0:
                    for cell_obj in self.surrounded_cells:
                        cell_obj.show_cell(False)

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_enemies_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_enemy:
                counter += 1
        return counter

    def show_cell(self, clicked = True):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.label_obj.unbind("<Button-1>")
            self.label_obj.unbind("<Button-3>")

            index = self.surrounded_cells_enemies_length
            if clicked:
                self.label_obj.configure(image=Cell.numbered_tiles[index])
            else:
                self.label_obj.configure(image=Cell.tiles[index])


            self.is_opened = True
            Text.tiles_text.label_obj.configure(
                text=f"REMAINING TILES\n{Cell.cell_count}"
                )
            if Cell.cell_count == 0:
                Cell.reveal_all(False)
                Game.win_chapter()

    def show_enemy(self):
        self.label_obj.configure(image=Cell.enemy_tile)
        Text.game_over.label_obj.place(relx=0.5, rely=0.9, anchor="center")
        Game.lost_or_won = True
        Audio.death()
        Cell.reveal_all()

    def right_click(self, *event):
        if not Game.lost_or_won:
            if not self.is_flagged:
                self.label_obj.configure(image=Cell.flag_tile)
                self.is_flagged = True
                Cell.enemy_count -= 1
            else:
                self.label_obj.configure(image=Cell.default_tile)
                self.is_flagged = False
                Cell.enemy_count += 1

            Text.enemies_text.label_obj.configure(
                text=f"ENEMIES LEFT\n{Cell.enemy_count}")

    @staticmethod
    def randomize_enemies():
        picked_cells = random.sample(Cell.all, Cell.enemy_count)
        for cell in picked_cells:
            cell.is_enemy = True
            if Game.DEBUGGING:
                cell.label_obj.configure(bg="red") # DEBUG
        
    @staticmethod
    def reveal_all(show_enemies = True):
        for cell in Cell.all:
            if cell.is_enemy:
                    if show_enemies:
                        cell.label_obj.configure(image=Cell.enemy_tile)
                        cell.label_obj.configure(bg="red")
                    else:
                        cell.label_obj.configure(image=Cell.flag_tile)
            elif not cell.is_opened:
                index = cell.surrounded_cells_enemies_length
                cell.label_obj.configure(image=Cell.tiles[index])