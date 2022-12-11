import pygame as pg
from source_code.Engine import Mouse_Mode as M_Eng
from source_code.Visualisation.Game import Text_Before_Game as TBG
from source_code.Visualisation.Menu import Vis_Start_Menu as VSM
from source_code.Classes import Classes as CL


class Button:

    def __init__(self, x, y, xsize, ysize, text):
        """ constructor of class "Button" """
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        """ return True if you click on the Button """
        if self.x < event.pos[0] < self.x + self.xsize and self.y < event.pos[1] < self.y + self.ysize:
            return True

    def write_text_on_button(self, screen):
        """ writing text on the element of class "Button" """
        myfont = pg.font.SysFont("monospace", 30)
        text = myfont.render(str(self.text), 1, (255, 255, 255))
        screen.blit(text, (self.x, self.y))


menu = True
trek_choice = CL.NumVariables(0)
trek_number = CL.NumVariables()


class PlayButton(Button):
    def __init__(self, *args):
        """ constructor of class "PlayButton" which the subclass of class "Button" """
        super().__init__(*args)

    def start_game(self, mode):
        """ Using for run game if player click on the element of PlayButton """
        trek_choice.setter(mode)


class TrekButton(Button):
    def __init__(self, *args, trek_number):
        """ constructor of class "TrekButton" which the subclass of class "Button" """
        super().__init__(*args)
        self.trek_number = trek_number

    def get_trek_number(self):
        """ Return number of trek for which the element of TrekButton is responsible"""
        return self.trek_number


surf = M_Eng.screen
menu_screen = VSM.DrawAMenuButton(surf)

"""def draw_menu_buttons():"""
""" the function responsible for drawing the "play" and "exit" buttons """
"""global play_button
global quit_button
M_Eng.screen.fill((0, 0, 0))
play_button = PlayButton(480, 200, 320, 180, 'play_button')
quit_button = Button(540, 450, 200, 138, 'quit_button')
menu_screen.all_menu_drawer_pressed('none')
pg.display.update()"""


def logic_of_menu_buttons(running, trek_choice, clock, pressing_start, pressing_quit, mode_type):
    """ describes the logic of menu buttons """
    global play_button
    global quit_button
    M_Eng.screen.fill((0, 0, 0))
    play_button = PlayButton(480, 200, 320, 180, 'play_button')
    quit_button = Button(540, 450, 200, 138, 'quit_button')
    for event in pg.event.get():
        if not pressing_start.getter() and not pressing_quit.getter():
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_button.is_click(event):  # PLAY/QUIT menu
                    M_Eng.screen.fill((0, 0, 0))
                    menu_screen.all_menu_drawer_pressed('start')
                    pg.display.update()
                    clock.tick(0.99)
                    pressing_start.setter(True)
                    menu_running = False
                if quit_button.is_click(event):
                    M_Eng.screen.fill((0, 0, 0))
                    menu_screen.all_menu_drawer_pressed('quit')
                    pg.display.update()
                    clock.tick(0.99)
                    pressing_quit.setter(True)
            if event.type == pg.QUIT:
                running.setter(False)
            else:
                if not pressing_start.getter() and not pressing_quit.getter():
                    menu_screen.all_menu_drawer_pressed('none')
        else:
            if event.type == pg.MOUSEBUTTONUP:  # MM/KM menu
                if play_button.is_click(event):
                    mm_button = Button(480, 200, 320, 180, 'mouse_mode')
                    km_button = Button(540, 450, 200, 138, 'keyboard_mode')
                    mm_button.write_text_on_button(M_Eng.screen)
                    km_button.write_text_on_button(M_Eng.screen)
                    pg.display.update()
                    mode_choice = True
                    # mode = 0
                    while mode_choice:
                        for event in pg.event.get():
                            if event.type == pg.MOUSEBUTTONDOWN:
                                if mm_button.is_click(event):
                                    mode_type.setter(1)
                                    # mode = 1
                                    mode_choice = False
                                elif km_button.is_click(event):
                                    mode_type.setter(2)
                                    mode_choice = False
                            elif event.type == pg.QUIT:
                                mode_choice = False
                                running.setter(False)
                        if mode_type.getter() == 1:  # mode == 1:
                            play_button.start_game(1)
                            menu_running = False
                            pressing_start.setter(False)
                        elif mode_type.getter() == 2:
                            play_button.start_game(2)
                            menu_running = False
                            pressing_start.setter(False)  # здесь будет меню выбора трека для клавиатура_режим
                elif quit_button.is_click(event):
                    running.setter(False)
                    pressing_quit.setter(False)
    if not pg.event.get():
        if not pressing_start.getter() and not pressing_quit.getter():
            menu_screen.all_menu_drawer_pressed('none')
            pg.display.update()
    if trek_choice.getter() == 1:  # MM Trek Choicing menu
        choice_running = True
        while choice_running:
            M_Eng.screen.fill((0, 0, 0))
            amount_of_buttons = 5
            trek_button = [0] * amount_of_buttons
            for i in range(amount_of_buttons):
                trek_button[i] = TrekButton(100, i * 70 + 70, 50, 50, f'trek_button_{i + 1}',
                                            trek_number=i + 1)
                trek_button[i].write_text_on_button(M_Eng.screen)
            back_to_menu = Button(500, 100, 50, 50, 'Back')
            back_to_menu.write_text_on_button(M_Eng.screen)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(amount_of_buttons):
                        if trek_button[i].is_click(event):
                            clock.tick(1)
                            for j in [4, 3, 2, 1, 0]:
                                TBG.countdown(j)
                            trek_number.setter(i + 1)
                            choice_running = False
                    if back_to_menu.is_click(event):
                        menu_running = True
                        choice_running = False
                        trek_choice.setter(0)
                elif event.type == pg.QUIT:
                    choice_running = False
                    running.setter(False)
                pause(event, clock, running)


def pause(event, clock, running):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            run_pause = True
            while run_pause:
                M_Eng.screen.fill((0, 0, 0))
                resume = Button(200, 200, 50, 50, 'Resume')
                resume.write_text_on_button(M_Eng.screen)
                to_menu = Button(200, 300, 50, 50, 'Exit_to_menu')
                to_menu.write_text_on_button(M_Eng.screen)
                pg.display.update()
                clock.tick(100)
                for action in pg.event.get():
                    if action.type == pg.QUIT:
                        running.setter(False)
                        # FIXME не закрывается при нажатии на крестик :(
                    elif action.type == pg.MOUSEBUTTONDOWN:
                        if resume.is_click(action):
                            run_pause = False
                            # FIXME должна продолжаться игра ( по идее если сунуть эту функцию туда куда надо,
                            # то все должно быть окей: меню паузы закроется и продолжится игра,
                            # но как это будет на практике хз если честно)

                        if to_menu.is_click(action):
                            run_pause = False
                            # FIXME должно открываться меню выбора трека (возможно стоит заново вызывать функцию отображения меню выбора,
                            # либо как-то выходить из этого цикла и запуска меню выбора, путем деланья trek_choice трушным
