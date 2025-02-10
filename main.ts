input.onButtonPressed(Button.A, function () {
    whichone += -1
})
input.onButtonPressed(Button.B, function () {
    whichone += 1
})
basic.clearScreen()
makerbit.connectLcd(39)
makerbit.clearLcd1602()
makerbit.setLcdBacklight(LcdBacklight.On)
basic.pause(2000)
makerbit.showStringOnLcd1602("hello", makerbit.position1602(LcdPosition1602.Pos1), 5)
basic.pause(1000)
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
makerbit.clearLcd1602()
let whichone = 1
basic.forever(function () {
    if (whichone == 1) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("3", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 2) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("4", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 3) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("5", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 4) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("6", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 5) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("7", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 6) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("8", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 7) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("9", makerbit.position1602(LcdPosition1602.Pos1), 1)
    }
    if (whichone == 8) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("10", makerbit.position1602(LcdPosition1602.Pos1), 2)
    }
    if (whichone == 9) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("jack", makerbit.position1602(LcdPosition1602.Pos1), 4)
    }
    if (whichone == 10) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("queen", makerbit.position1602(LcdPosition1602.Pos1), 5)
    }
    if (whichone == 11) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("king", makerbit.position1602(LcdPosition1602.Pos1), 4)
    }
    if (whichone == 12) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("ace", makerbit.position1602(LcdPosition1602.Pos1), 3)
    }
    if (whichone == 13) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("2", makerbit.position1602(LcdPosition1602.Pos1), 3)
    }
    if (whichone == 14) {
        makerbit.clearLcd1602()
        makerbit.showStringOnLcd1602("joker", makerbit.position1602(LcdPosition1602.Pos1), 5)
    }
    if (whichone == 15) {
        whichone = 1
    }
    if (whichone == 0) {
        whichone = 14
    }
})
