# How much time should pass before the sprite gets changed?
default time_sprite_change = 1.0

# Sprites for mid-choice changes
default sprite1 = None
default sprite2 = None
default current_sprite = None
default sprite_changed = False

# Where do we go if we catch a change in expression?
default sprite_catch_label = None

screen sprite_change_screen:
    zorder -1

    if time_sprite_change == 0.0:
        $ current_sprite = sprite1
    else:
        $ current_sprite = sprite2

    # change the sprite to sprite2
    # set a timer for a few seconds
    # when the timer goes to zero, change it back to the first sprite
    # currently technically working, but i'd like to make it so people can still press the button after the sprite reverts back

    add current_sprite xalign 0.5 yalign 1.0 ## show the sprite

    key "K_r" action [SetVariable("sprite1", None), Hide("countdown"), ## successfully call out the change
    SetVariable("qte_mash", 0), SetVariable("time_sprite_change", 1.0), SetVariable("can_mash", False), SetVariable("sprite_changed", False),
    Hide("sprite_change_screen"), Jump(sprite_catch_label), Hide("qte_screen")]

    timer 0.01 repeat True action If(time_sprite_change > 0.0, true=SetVariable("time_sprite_change", time_sprite_change-0.01),
    false=(SetVariable("time_sprite_change", 1.0), SetVariable("sprite_changed", True), Hide("sprite_change_screen")))

    #timer 0.01 repeat True action [If(current_time > time_sprite_change and current_time < time_sprite_return,
    #true=SetVariable("current_sprite", sprite2),
    #false=SetVariable("current_sprite", sprite1)),
    #Hide("sprite_change_screen"), Show("sprite_change_screen")
    #]
