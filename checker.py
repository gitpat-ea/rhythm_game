import pygame as pg
from source_code.Visualisation.Background import Background as bg

from source_code.Visualisation.Menu import Vis_Choose_a_song_Menu as csm
from source_code.Visualisation.Menu import Vis_Pause_Menu as pm
from source_code.Visualisation.Menu import Vis_Start_Menu as sm
from source_code.Visualisation.Game import Vis_Mouse_Mode as vmm
from source_code.Visualisation.Menu import Vis_Choose_mode_menu as vcm
from source_code.Visualisation.Menu import Vis_End_menu as vem

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

finished = False

cs_menu = csm.VisualisationInChooseSongMenu(screen)

start_menu = sm.DrawAMenuButton(screen)

pause_menu = pm.DrawAMenuButton(screen)

chm_menu = vcm.DrawAMenuButton(screen)

end_menu = vem.DrawAMenuButton(screen, 10)

while not finished:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))
            end_menu.all_menu_drawer_pressed('to_menu')
            pg.display.update()
        else:
            screen.fill((0, 0, 0))
            end_menu.all_menu_drawer_pressed('to_menu')
            pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            finished = True


pg.quit()
