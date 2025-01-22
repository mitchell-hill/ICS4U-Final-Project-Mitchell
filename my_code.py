class SpriteKindLegacy(Enum):
    Player = 0
    Projectile = 1
    Food = 2
    Enemy = 3
class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
    Looking = 3
    MoveLeft = 4
    MoveRight = 5
    MoveDown = 6

def on_up_pressed():
    animation.set_action(mySprite, ActionKind.MoveDown)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_released():
    animation.set_action(mySprite, ActionKind.Idle)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    animation.set_action(mySprite, ActionKind.MoveLeft)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.set_action(mySprite, ActionKind.Idle)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.set_action(mySprite, ActionKind.Idle)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_overlap_player_food(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKindLegacy.Player,
    SpriteKindLegacy.Food,
    on_overlap_player_food)

def populateDigits():
    global one, one2, one3, one4, one5, one6, one7, one8, one9, one10, one11, one12, one13, one14, one15, one16, one17, one18, one19, one20, one21, one22, one24, one25, one26, one27, one28, one29, zero, zero2, zero3, zero4, zero5, zero6, zero7, zero8, zero9, zero10, zero11, zero12, zero13, zero14, zero15, zero16, zero17, zero18, zero19, zero20, zero21, zero22, zero23, zero24, zero25, zero26
    one = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one2 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one3 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one4 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one5 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one6 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one7 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one8 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one9 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one10 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one11 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one12 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one13 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one14 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one15 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one16 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one17 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one18 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one19 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one20 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one21 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one22 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one24 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one25 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one26 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one27 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one28 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    one29 = sprites.create(img("""
            . . . 1 1 . . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        SpriteKindLegacy.Food)
    zero = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero2 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero3 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero4 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero5 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero6 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero7 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero8 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero9 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero10 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero11 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero12 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero13 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero14 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero15 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero16 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero17 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero18 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero19 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero20 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero21 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero22 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero23 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero24 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero25 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    zero26 = sprites.create(img("""
            . . 1 1 1 1 . . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . 1 1 . . 1 1 . 
                    . . 1 1 1 1 . .
        """),
        SpriteKindLegacy.Food)
    one12.set_position(50, 32)
    one.set_position(70, 32)
    zero.set_position(90, 32)
    one2.set_position(110, 32)
    zero2.set_position(128, 32)
    one6.set_position(148, 32)
    zero4.set_position(168, 32)
    one7.set_position(188, 32)
    one8.set_position(208, 32)
    one3.set_position(128, 52)
    one4.set_position(128, 72)
    zero3.set_position(128, 92)
    one5.set_position(128, 109)
    one9.set_position(128, 128)
    zero5.set_position(108, 128)
    zero6.set_position(88, 128)
    zero7.set_position(68, 128)
    one11.set_position(48, 128)
    one13.set_position(32, 32)
    one10.set_position(32, 52)
    zero8.set_position(32, 72)
    zero9.set_position(32, 92)
    one14.set_position(32, 109)
    zero10.set_position(32, 128)
    zero11.set_position(32, 150)
    one15.set_position(32, 170)
    zero12.set_position(32, 191)
    one16.set_position(50, 191)
    one17.set_position(69, 191)
    one18.set_position(88, 191)
    zero13.set_position(108, 191)
    zero14.set_position(128, 191)
    one19.set_position(128, 171)
    one20.set_position(128, 151)
    zero15.set_position(148, 128)
    one21.set_position(165, 128)
    zero16.set_position(183, 128)
    zero17.set_position(202, 128)
    zero18.set_position(220, 128)
    one22.set_position(240, 128)
    one24.set_position(240, 108)
    one25.set_position(240, 88)
    zero19.set_position(240, 68)
    zero20.set_position(240, 49)
    one26.set_position(240, 32)
    zero21.set_position(224, 32)
    one27.set_position(240, 145)
    zero22.set_position(240, 160)
    zero23.set_position(240, 175)
    one28.set_position(240, 190)
    zero24.set_position(148, 190)
    zero25.set_position(168, 190)
    zero26.set_position(188, 190)
    one15.set_position(208, 190)
    one29.set_position(222, 190)

def on_right_pressed():
    animation.set_action(mySprite, ActionKind.MoveRight)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    animation.set_action(mySprite, ActionKind.Idle)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    animation.set_action(mySprite, ActionKind.MoveDown)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def createPlayer():
    global anim, anim1, anim3, anim4, mySprite
    anim = animation.create_animation(ActionKind.MoveLeft, 200)
    anim1 = animation.create_animation(ActionKind.MoveRight, 200)
    anim3 = animation.create_animation(ActionKind.Idle, 200)
    anim4 = animation.create_animation(ActionKind.MoveDown, 200)
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . f f 5 5 5 5 5 f f . . . . 
                    . . f 5 5 5 5 5 5 5 5 5 f . . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    f f f f f f f f f f f f f f f . 
                    f 5 f 1 1 f f f f 1 1 f f 5 f . 
                    f 5 f 1 f f f 5 f 1 f f f 5 f . 
                    f 5 5 f f f 5 5 5 f f f 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    . f 5 5 5 5 5 5 5 5 f 5 5 f . . 
                    . f 5 5 5 f f f f f 5 5 5 f . . 
                    . . f 5 5 5 5 5 5 5 5 5 f . . . 
                    . . . f f 5 5 5 5 5 f f . . . . 
                    . . . . . f f f f f . . . . . .
        """),
        SpriteKindLegacy.Player)
    anim.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                f 5 f f f f f f f f f f f 5 f . 
                f 5 f 1 1 f f 5 5 5 5 5 5 5 f . 
                f 5 f f 1 f f 5 5 5 5 5 5 5 f . 
                f 5 5 f f f 5 5 5 5 5 5 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f f f f f f f f f 5 5 5 f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f 5 5 5 5 5 5 f f . . . . 
                . . . . f f f f f f . . . . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f f 5 5 5 5 5 5 5 f f . . . 
                . f f 5 5 5 5 5 5 5 5 5 f f . . 
                . f f f f f f f f f f f 5 f . . 
                f 5 f 1 1 f f 5 5 5 5 5 5 5 f . 
                f 5 f f 1 f f 5 5 5 5 5 5 5 f . 
                f 5 5 f f f f 5 5 5 5 5 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                f f f f f f f f f f 5 5 5 5 f . 
                f f f f f f f f f f f 5 5 5 f . 
                . f f f f f f f f f f 5 5 f . . 
                . f f f f f f f f f 5 5 5 f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f 5 5 5 5 5 5 f f . . . . 
                . . . . f f f f f f . . . . . .
    """))
    anim1.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                f 5 5 f f f f f f f f f f 5 f . 
                f 5 5 5 5 5 5 5 f f 1 1 f 5 f . 
                f 5 5 5 5 5 5 5 f f 1 f f 5 f . 
                f 5 5 5 5 5 5 5 5 f f 5 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f 5 5 5 f f f f f f f f f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f 5 5 5 5 5 5 f f . . . . 
                . . . . f f f f f f . . . . . .
    """))
    anim1.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f f 5 5 5 5 5 5 5 f f . . . 
                . f f 5 5 5 5 5 5 5 5 5 f f . . 
                . f 5 5 f f f f f f f f f f . . 
                f 5 5 5 5 5 5 5 f f 1 1 f 5 f . 
                f 5 5 5 5 5 5 5 f f 1 f f 5 f . 
                f 5 5 5 5 5 5 5 f f f f 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                f 5 5 5 5 f f f f f f f f f f . 
                f 5 5 5 f f f f f f f f f f f . 
                . f 5 5 f f f f f f f f f f . . 
                . f 5 5 5 f f f f f f f f f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f 5 5 5 5 5 5 f f . . . . 
                . . . . f f f f f f . . . . . .
    """))
    anim3.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                f f f f f f f f f f f f f f f . 
                f 5 f 1 1 f f f f 1 1 f f 5 f . 
                f 5 f 1 f f f 5 f 1 f f f 5 f . 
                f 5 5 f f f 5 5 5 f f f 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                . f 5 5 5 5 5 5 5 5 f 5 5 f . . 
                . f 5 5 5 f f f f f 5 5 5 f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . . . . f f f f f . . . . . .
    """))
    anim4.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f f f f f f f f f f f f f . . 
                . f f 1 1 f f f f 1 1 f f f . . 
                f f f 1 f f f f f 1 f f f f f . 
                f 5 f f f f 5 5 f f f f f 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                f 5 5 f f f f f f f f f 5 5 f . 
                . f 5 f f f f f f f f f 5 f . . 
                . f 5 5 f f f f f f f 5 5 f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . . . . f f f f f . . . . . .
    """))
    anim4.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                f f f f f f f f f f f f f f f . 
                f 5 f 1 1 f f f f 1 1 f f 5 f . 
                f 5 f 1 f f f 5 f 1 f f f 5 f . 
                f 5 5 f f f 5 5 5 f f f 5 5 f . 
                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                . f 5 5 5 5 5 5 5 5 f 5 5 f . . 
                . f 5 5 5 f f f f f 5 5 5 f . . 
                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                . . . f f 5 5 5 5 5 f f . . . . 
                . . . . . f f f f f . . . . . .
    """))
    animation.attach_animation(mySprite, anim)
    animation.attach_animation(mySprite, anim1)
    animation.attach_animation(mySprite, anim3)
    animation.attach_animation(mySprite, anim4)
    controller.move_sprite(mySprite)
    scene.camera_follow_sprite(mySprite)
    mySprite.set_position(128, 128)
def createBugs():
    global bug1Direction, bug2Direction, bug3Direction, bug4Direction, bug5Direction, bug6Direction, bug1, bug2, bug3, bug4, bug5, bug6
    bug1Direction = 0
    bug2Direction = 0
    bug3Direction = 0
    bug4Direction = 0
    bug5Direction = 0
    bug6Direction = 0
    bug1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . 5 5 5 5 5 5 . . . . . 
                    . . . . 5 5 5 5 5 5 5 5 . . . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 5 1 1 5 5 5 5 1 1 5 5 5 . . 
                    . . 1 1 1 1 5 5 1 1 1 1 5 5 . . 
                    . . 8 8 1 1 5 5 8 8 1 1 5 5 . . 
                    . 5 8 8 1 1 5 5 8 8 1 1 5 5 5 . 
                    . 5 5 1 1 5 5 5 5 1 1 5 5 5 5 . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . 5 5 . 5 5 5 . . 5 5 5 . 5 5 . 
                    . 5 . . . 5 5 . . 5 5 . . . 5 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Enemy)
    bug2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 7 7 7 7 . . . . . . 
                    . . . . . 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 7 7 7 7 7 7 . . . . 
                    . . . 7 7 7 7 7 7 7 7 7 7 . . . 
                    . . 7 1 1 7 7 7 7 1 1 7 7 7 . . 
                    . . 1 1 1 1 7 7 1 1 1 1 7 7 . . 
                    . . 8 8 1 1 7 7 8 8 1 1 7 7 . . 
                    . 7 8 8 1 1 7 7 8 8 1 1 7 7 7 . 
                    . 7 7 1 1 7 7 7 7 1 1 7 7 7 7 . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                    . 7 7 . 7 7 7 . . 7 7 7 . 7 7 . 
                    . 7 . . . 7 7 . . 7 7 . . . 7 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Enemy)
    bug3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 3 3 3 3 . . . . . . 
                    . . . . . 3 3 3 3 3 3 . . . . . 
                    . . . . 3 3 3 3 3 3 3 3 . . . . 
                    . . . 3 3 3 3 3 3 3 3 3 3 . . . 
                    . . 3 1 1 3 3 3 3 1 1 3 3 3 . . 
                    . . 1 1 1 1 3 3 1 1 1 1 3 3 . . 
                    . . 8 8 1 1 3 3 8 8 1 1 3 3 . . 
                    . 3 8 8 1 1 3 3 8 8 1 1 3 3 3 . 
                    . 3 3 1 1 3 3 3 3 1 1 3 3 3 3 . 
                    . 3 3 3 3 3 3 3 3 3 3 3 3 3 3 . 
                    . 3 3 3 3 3 3 3 3 3 3 3 3 3 3 . 
                    . 3 3 3 3 3 3 3 3 3 3 3 3 3 3 . 
                    . 3 3 . 3 3 3 . . 3 3 3 . 3 3 . 
                    . 3 . . . 3 3 . . 3 3 . . . 3 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Enemy)
    bug4 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . a a a a . . . . . . 
                    . . . . . a a a a a a . . . . . 
                    . . . . a a a a a a a a . . . . 
                    . . . a a a a a a a a a a . . . 
                    . . a 1 1 a a a a 1 1 a a a . . 
                    . . 1 1 1 1 a a 1 1 1 1 a a . . 
                    . . 8 8 1 1 a a 8 8 1 1 a a . . 
                    . a 8 8 1 1 a a 8 8 1 1 a a a . 
                    . a a 1 1 a a a a 1 1 a a a a . 
                    . a a a a a a a a a a a a a a . 
                    . a a a a a a a a a a a a a a . 
                    . a a a a a a a a a a a a a a . 
                    . a a . a a a . . a a a . a a . 
                    . a . . . a a . . a a . . . a . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Enemy)
    bug5 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . d d d d . . . . . . 
                    . . . . . d d d d d d . . . . . 
                    . . . . d d d d d d d d . . . . 
                    . . . d d d d d d d d d d . . . 
                    . . d 1 1 d d d d 1 1 d d d . . 
                    . . 1 1 1 1 d d 1 1 1 1 d d . . 
                    . . 8 8 1 1 d d 8 8 1 1 d d . . 
                    . d 8 8 1 1 d d 8 8 1 1 d d d . 
                    . d d 1 1 d d d d 1 1 d d d d . 
                    . d d d d d d d d d d d d d d . 
                    . d d d d d d d d d d d d d d . 
                    . d d d d d d d d d d d d d d . 
                    . d d . d d d . . d d d . d d . 
                    . d . . . d d . . d d . . . d . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Enemy)
    bug6 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 2 2 . . . . . . 
                    . . . . . 2 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                    . . . 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 1 1 2 2 2 2 1 1 2 2 2 . . 
                    . . 1 1 1 1 2 2 1 1 1 1 2 2 . . 
                    . . 8 8 1 1 2 2 8 8 1 1 2 2 . . 
                    . 2 8 8 1 1 2 2 8 8 1 1 2 2 2 . 
                    . 2 2 1 1 2 2 2 2 1 1 2 2 2 2 . 
                    . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 
                    . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 
                    . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 
                    . 2 2 . 2 2 2 . . 2 2 2 . 2 2 . 
                    . 2 . . . 2 2 . . 2 2 . . . 2 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Enemy)
    bug1.set_position(150, 32)
    bug2.set_position(220, 130)
    bug3.set_position(32, 190)
    bug4.set_position(128, 32)
    bug5.set_position(32, 150)
    bug6.set_position(240, 32)
def reset():
    populateDigits()
    createPlayer()
    createBugs()
bug6: Sprite = None
bug5: Sprite = None
bug4: Sprite = None
bug3: Sprite = None
bug2: Sprite = None
bug1: Sprite = None
bug6Direction = 0
bug5Direction = 0
bug4Direction = 0
bug3Direction = 0
bug2Direction = 0
bug1Direction = 0
anim4: animation.Animation = None
anim3: animation.Animation = None
anim1: animation.Animation = None
anim: animation.Animation = None
zero26: Sprite = None
zero25: Sprite = None
zero24: Sprite = None
zero23: Sprite = None
zero22: Sprite = None
zero21: Sprite = None
zero20: Sprite = None
zero19: Sprite = None
zero18: Sprite = None
zero17: Sprite = None
zero16: Sprite = None
zero15: Sprite = None
zero14: Sprite = None
zero13: Sprite = None
zero12: Sprite = None
zero11: Sprite = None
zero10: Sprite = None
zero9: Sprite = None
zero8: Sprite = None
zero7: Sprite = None
zero6: Sprite = None
zero5: Sprite = None
zero4: Sprite = None
zero3: Sprite = None
zero2: Sprite = None
zero: Sprite = None
one29: Sprite = None
one28: Sprite = None
one27: Sprite = None
one26: Sprite = None
one25: Sprite = None
one24: Sprite = None
one22: Sprite = None
one21: Sprite = None
one20: Sprite = None
one19: Sprite = None
one18: Sprite = None
one17: Sprite = None
one16: Sprite = None
one15: Sprite = None
one14: Sprite = None
one13: Sprite = None
one12: Sprite = None
one11: Sprite = None
one10: Sprite = None
one9: Sprite = None
one8: Sprite = None
one7: Sprite = None
one6: Sprite = None
one5: Sprite = None
one4: Sprite = None
one3: Sprite = None
one2: Sprite = None
one: Sprite = None
mySprite: Sprite = None
info.set_score(0)
info.set_life(3)
scene.set_tile_map(img("""
    88888888888888888888888888888888
        8fffffffffffffff88888ffffffffff8
        8fffffffffffffff88888ffffffffff8
        8ff8888ff88888ff88888888ff888ff8
        8ff8ff8ff8fff8ff88888ff8ff8f8ff8
        8ff8ff8ff8fff8ff888888f8ff8f8ff8
        8ff8888ff88888ff88888888ff888ff8
        8fffffffffffffff888888fffffffff8
        8fffffffffffffff888888fffffffff8
        8ff8888ff88888ff888888f8ff888ff8
        8ff8888ff88888ff888888f8ff888ff8
        8fffffffffffffff888888f8fffffff8
        8fffffffffffffff88888888fffffff8
        888888888888888888888ff8ff888888
        888888888888888888888ff8ff888888
        888888888888888888888fffffffffff
        888888888888888888888fffffffffff
        8888888ff8ff8fffffff8ff8ff888888
        8ffffffff8ff8fffffff8ff8fffffff8
        8ffffffff8ff8fffffff8ff8fffffff8
        8ff8888ff8ff888888888ff8ff888ff8
        8fffff8ff8fffffffffffff8ff8ffff8
        8fffff8fffffffffffffffffff8ffff8
        8888ff8fffff888888888fffff8ff888
        8888ff8ff888888888888888ff8ff888
        8fffffffffffffff8ffffffffffffff8
        8fffffffffffffff8ffffffffffffff8
        8ff88888888888ff8ff8888888888ff8
        8ff88888888888ff8ff8888888888ff8
        8fffffffffffffff8ffffffffffffff8
        8ffffffffffffffffffffffffffffff8
        88888888888888888888888888888888
"""))
scene.set_tile(8,
    img("""
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 f f f f f f f f f f f f 8 8 
            8 f 8 f f f f f f f f f f 8 f 8 
            8 f f 8 f f f f f f f f 8 f f 8 
            8 f f f 8 f f f f f f 8 f f f 8 
            8 f f f f 8 f f f f 8 f f f f 8 
            8 f f f f f 8 f f 8 f f f f f 8 
            8 f f f f f f 8 8 f f f f f f 8 
            8 f f f f f f 8 8 f f f f f f 8 
            8 f f f f f 8 f f 8 f f f f f 8 
            8 f f f f 8 f f f f 8 f f f f 8 
            8 f f f 8 f f f f f f 8 f f f 8 
            8 f f 8 f f f f f f f f 8 f f 8 
            8 f 8 f f f f f f f f f f 8 f 8 
            8 8 f f f f f f f f f f f f 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    """),
    True)
populateDigits()
createPlayer()
createBugs()

def on_forever():
    global bug1Direction, bug2Direction, bug3Direction, bug4Direction, bug5Direction, bug6Direction
    if bug1.x > 239:
        bug1Direction = 1
    if bug1.x < 30:
        bug1Direction = 0
    if bug1Direction == 0:
        bug1.set_velocity(50, 0)
    else:
        bug1.set_velocity(-50, 0)
    if bug2.x > 239:
        bug2Direction = 1
    if bug2.x < 30:
        bug2Direction = 0
    if bug2Direction == 0:
        bug2.set_velocity(50, 0)
    else:
        bug2.set_velocity(-50, 0)
    if bug3.x > 239:
        bug3Direction = 1
    if bug3.x < 30:
        bug3Direction = 0
    if bug3Direction == 0:
        bug3.set_velocity(50, 0)
    else:
        bug3.set_velocity(-50, 0)
    if bug4.y < 30:
        bug4Direction = 0
    if bug4.y > 190:
        bug4Direction = 1
    if bug4Direction == 0:
        bug4.set_velocity(0, 50)
    else:
        bug4.set_velocity(0, -50)
    if bug5.y < 30:
        bug5Direction = 0
    if bug5.y > 190:
        bug5Direction = 1
    if bug5Direction == 0:
        bug5.set_velocity(0, 50)
    else:
        bug5.set_velocity(0, -50)
    if bug6.y < 30:
        bug6Direction = 0
    if bug6.y > 190:
        bug6Direction = 1
    if bug6Direction == 0:
        bug6.set_velocity(0, 50)
    else:
        bug6.set_velocity(0, -50)
forever(on_forever)
