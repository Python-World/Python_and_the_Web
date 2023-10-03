import random
import time
from tkinter import CENTER, Frame, Label, PhotoImage, StringVar

import constants as c
from logic import convert_time, is_solvable, is_solved


class Puzzle(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title("15 Puzzle :: Made With ❤️ By Advik")

        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

        self.master.bind("<Escape>", self.new_game)

        self.score = StringVar(self.master)
        self.init_grid()
        self.new_game()

        self.mainloop()

    def new_game(self, *args):
        # remove the game over dialog
        self.game_over_dialog.place_forget()

        # reset the game state
        self.moves = 25
        self.start_time = time.time() - 54
        self.game_grid = list(range(1, c.GRID_LEN**2)) + [0]
        self.game_grid = list(range(0, c.GRID_LEN * c.GRID_LEN))
        random.shuffle(self.game_grid)
        while not is_solvable(self.game_grid):
            random.shuffle(self.game_grid)
        self.empty_cell_location = self.game_grid.index(0)

        # update the grid
        self.update_grid()

    def game_over(self, *args):
        self.score.set(
            f"{self.moves} moves and {convert_time(time.time() - self.start_time)}"
        )
        self.game_over_dialog.place(relx=0.5, rely=0.5, anchor=CENTER)

    def init_grid(self):
        self.grid_cells = []

        # the background
        self.game_scene = Frame(
            self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE
        )
        self.game_scene.grid()

        # game grid
        for i in range(c.GRID_LEN * c.GRID_LEN):
            cell = Frame(self.game_scene, bg=c.CELL_COLOR_EMPTY)
            cell.grid(
                row=i // c.GRID_LEN,
                column=i % c.GRID_LEN,
                padx=c.GRID_PADDING,
                pady=c.GRID_PADDING,
            )
            t = Label(
                master=cell,
                text="",
                bg=c.CELL_COLOR_EMPTY,
                fg=c.TEXT_COLOR,
                justify=CENTER,
                font=c.FONT,
                width=4,
                height=2,
            )
            t.bind("<Button-1>", lambda event, i=i: self.move_cell(i))
            t.grid()

            self.grid_cells.append(t)

        # create game over dialog but dont place it
        self.game_over_dialog = Frame(self)
        f = Frame(self.game_over_dialog, bg="white", padx=10, pady=10)
        f.grid()
        # the excellent image
        image = PhotoImage(file="excellent.png")
        l = Label(f, image=image)
        l.image = image
        l.grid(columnspan=2, padx=10, pady=5)
        # tell the performance
        Label(
            f, text="It took you", bg="white", fg="#534648", font="Arial 16"
        ).grid(row=1, column=0, pady=10)
        Label(
            f,
            textvariable=self.score,
            bg="white",
            fg="#534648",
            font="Arial 16 bold",
        ).grid(row=1, column=1, pady=10)
        # play again button
        btn = Label(
            f,
            text="Play Again",
            bg="#3d2963",
            fg="white",
            font="Arial 22 bold",
            justify=CENTER,
            pady=10,
            padx=20,
            cursor="hand2",
        )
        btn.bind("<Enter>", lambda event: btn.config(bg="tomato"))
        btn.bind("<Leave>", lambda event: btn.config(bg="#3d2963"))
        btn.bind("<Button-1>", self.new_game)
        btn.grid(columnspan=2, pady=5)

    def update_grid(self):
        i = 1
        for num, cell in zip(self.game_grid, self.grid_cells):
            bg = c.CELL_COLOR_EMPTY
            text = ""
            if num > 0:
                text = num
                if i == num:
                    bg = c.CELL_COLOR_CORRECT
                else:
                    bg = c.CELL_COLOR_INCORRECT

            cell.configure(bg=bg, text=text)
            i += 1

    def swap_cells(self, x, y):
        self.moves += 1
        self.game_grid[x], self.game_grid[y] = (
            self.game_grid[y],
            self.game_grid[x],
        )
        self.update_grid()
        # check if grid is solved
        if is_solved(self.game_grid):
            self.game_over()

    def move_cell(self, pos):
        print(pos)
        for i in (1, -1, c.GRID_LEN, -c.GRID_LEN):
            if pos + i == self.empty_cell_location:
                self.swap_cells(pos, pos + i)
                self.empty_cell_location -= i
                return

    def move_up(self, *args):
        print(self.empty_cell_location)
        x = self.empty_cell_location
        if x // c.GRID_LEN < c.GRID_LEN - 1:
            self.swap_cells(x + c.GRID_LEN, x)
            self.empty_cell_location += c.GRID_LEN

    def move_down(self, *args):
        print(self.empty_cell_location)
        x = self.empty_cell_location
        if x // c.GRID_LEN > 0:
            self.swap_cells(x - c.GRID_LEN, x)
            self.empty_cell_location -= c.GRID_LEN

    def move_left(self, *args):
        print(self.empty_cell_location)
        x = self.empty_cell_location
        if x % c.GRID_LEN < c.GRID_LEN - 1:
            self.swap_cells(x + 1, x)
            self.empty_cell_location += 1

    def move_right(self, *args):
        print(self.empty_cell_location)
        x = self.empty_cell_location
        if x % c.GRID_LEN > 0:
            self.swap_cells(x - 1, x)
            self.empty_cell_location -= 1


puzzle = Puzzle()
