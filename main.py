def on_button_pressed_a():
    global whichone
    whichone += -1
    whichone = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global whichone
    whichone += 1
    whichone = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

whichone = 0
basic.clear_screen()
makerbit.connect_lcd(39)
makerbit.clear_lcd1602()
makerbit.set_lcd_backlight(LcdBacklight.ON)
basic.pause(2000)
makerbit.show_string_on_lcd1602("hello", makerbit.position1602(LcdPosition1602.POS1), 5)
basic.pause(1000)
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.UNTIL_DONE)
makerbit.clear_lcd1602()

def on_forever():
    global whichone
    if whichone == 0:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("3", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 2:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("4", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 3:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("5", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 4:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("6", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 5:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("7", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 6:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("8", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 7:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("9", makerbit.position1602(LcdPosition1602.POS1), 1)
    if whichone == 8:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("10", makerbit.position1602(LcdPosition1602.POS1), 2)
    if whichone == 9:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("jack", makerbit.position1602(LcdPosition1602.POS1), 4)
    if whichone == 10:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("queen", makerbit.position1602(LcdPosition1602.POS1), 5)
    if whichone == 11:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("king", makerbit.position1602(LcdPosition1602.POS1), 4)
    if whichone == 12:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("ace", makerbit.position1602(LcdPosition1602.POS1), 3)
    if whichone == 13:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("2", makerbit.position1602(LcdPosition1602.POS1), 3)
    if whichone == 14:
        makerbit.clear_lcd1602()
        makerbit.show_string_on_lcd1602("joker", makerbit.position1602(LcdPosition1602.POS1), 5)
    if whichone == 15:
        whichone = 0
    if whichone == -1:
        whichone = 14
basic.forever(on_forever)
