label mash_test_start:
###### qte setup

    $ menu_dialogue = ""
    $ aff = 0
    $ order = ""
    $ french_talk = False
    $ timedout_3 = False
    $ do_start_timer = False
    $ list_length = 0

    "Hi! Do you want a quick tutorial of the controls and rules?"

menu:
    "Yes.":
        jump tutorial_start

    "No.":
        jump game_start

label tutorial_start:
    $ fail_label = "tut_m1_fail"
    $ pass_label = "tut_m1_pass"
    $ mash_label = "tut_m1_c1"
    $ choice_menu = "tut_menu1"
    $ do_start_timer = True

    "Alright! This game is about tying body language to what you want to say."
    "You'll choose a line of dialogue, and then you'll only have a few seconds to figure out what body language you should show."
    "Let's try it now! Can you pick this choice?"

label tut_menu1:
    menu:
        "Sure!":
            $ key_list = ["w"]
            $ current_time = 5.0
            $ can_mash = True
            jump tut_m1_c1

label tut_m1_c1:

    "And now that you picked it, can you mash \'W\' for me?"

label tut_m1_fail:

    "Oops! Let's try that again!"
    $ current_time = 5.0
    $ can_mash = True
    show screen countdown

    jump tut_m1_c1

label tut_m1_pass:

    "Nice job! That one's for making eye contact. It's good for showing someone you're interested, but it can intimidate people too."
    "Body language can be unclear, so you might need to show more than one form to get the right point across."
    "After you compliment me, can you give me eye contact and smile with \'Q\' and \'E\' to show me you mean it?"

    $ fail_label = "tut_m2_fail"
    $ pass_label = "tut_m2_pass"
    $ mash_label = "tut_m2_c1"
    $ choice_menu = "tut_menu2"

label tut_menu2:
    menu:
        "Yeah, you look beautiful today!":
            $ key_list = ["w", "q"]
            jump tut_m2_c1

label tut_m2_c1:
    $ current_time = 5.0
    $ can_mash = True
    #show screen countdown

    "Now go ahead and mash!"

label tut_m2_fail:
    "You wanna try that again? Remember: \'W\' {i}then{/i} \'Q\' and \'E\'."
    $ key_list = ["w", "q"]
    show screen countdown

    jump tut_m2_c1

label tut_m2_pass:
    "Thanks, and so do you!"
    "You can perform your body language in any order you want, by the way!"
    "The last thing you can mash is \'2\' to wring your hands."
    "It shows people you\'re nervous, but hey. You\'re about to go on a blind date."
    "Honesty might be the best policy sometimes. Hope you have fun!"

label game_start:
    scene bg rest

    "The worst thing about these blind dates is always waiting for the other person to show up. No question."
    "I always show up early. I don't want the other person to think I'm not interested."
    "I check my phone for what feels like the 30th time. He's ten minutes late."
    "The waiter finally drops by with someone. I think that's him."

    show taffy smile at center

    t "Levi?"
    l "Yeah... I-I mean, hey."

    $ choice_menu = "menu1"
    $ fail_label = "menu1_end"
    $ can_mash = False
    $ do_start_timer = False

label menu1:
    if wait_dialogue == 1:
        $ menu_dialogue = "I haven't been on a blind date in forever."

    elif wait_dialogue == 2:
        $ menu_dialogue = "Sorry if I'm kinda... rusty."

    else:
        $ wait_dialogue = 0
        $ menu_dialogue = "Nice to meet you!"

    menu:
        t "[menu_dialogue]"

        "You're late.":
            t "{i}And{/i} worth it if you behave."
            l "Um... Yes... sir...?"
            "I can't tell if I'm dreading this or excited."

            jump menu1_end

        "You're Taffy, right?":
            $ aff += 1
            $ french_talk = True
            t "{i}Taffeta de la Foucherie,{/i} that's me."
            l "...The butcher's taffeta?"
            t "Hah! You're thinking of Taffeta de la {i}Boucherie.{/i}"
            t "But interesting that you know French."

label menu1_end:

    t "Have you been here before?"
    l "All the time."
    "His smile gets a bit wider at that, and I hear a soft hum from his lips."
    "Taffy takes in the sights of the restaurant as the waiter comes back asking for our order."

    $ sprite1 = "sprites/taffy1.png"
    $ sprite2 = "sprites/taffy3.png"

    "I take a deep breath as I start feigning confidence for the sake of the waiter."

    # set the time the player has
    $ fail_label = "timeout2"
    $ choice_menu = "menu2"
    $ do_start_timer = True

    $ sprite_catch_label = "bodyread2"

    $ current_time = 5.0
    $ total_time = 5.0

label menu2:
    if wait_dialogue == 1:
        $ menu_dialogue = "I might need a minute, I was too busy looking at {i}you{/i} to look at the menu."

    elif wait_dialogue == 2:
        $ menu_dialogue = "Don't worry so much about what you're gonna order. I won't judge."

    else:
        $ wait_dialogue = 0
        $ menu_dialogue = "Do you know what you want?"

    menu:
        t "[menu_dialogue]"

        "Can you get us started with some wine?":
            $ pass_label = "m2_c1_pass"
            $ mash_label = "m2_c1"
            $ key_list = ["2"]
            jump m2_c1

        "What do you want, Taffy?":
            $ pass_label = "m2_c2_pass"
            $ mash_label = "m2_c2"
            $ key_list = ["w", "q"]
            jump m2_c2

        "Is it wrong that I wanna start with dessert?":
            $ pass_label = "m2_c3_pass"
            $ mash_label = "m2_c3"
            $ key_list = ["2", "q"]
            jump m2_c3

label m2_c1:

    "Is it bad to {i}start{/i} with wine? I need something to loosen me up, though..."

label m2_c1_pass:
    $ order = "wine"

    l "Is that alright?"

    show taffy smile

    t "As long as it's the best malbec on the menu."
    "The waiter nods before leaving to get the bottle."

    jump menu2_end

label m2_c2:
    if len(key_list) == 2:
        "Oh fuck, is that patronizing? He hasn't had a chance to look yet..."
    else:
        "It's gonna be really hard to make it look sincere."

label m2_c2_pass:
    show taffy w_smile

    t "Well... I'm not sure yet either. Can I get some more time to look?"
    "The waiter leaves and gives us some more time with the menu."

jump menu2_end

label m2_c3:
    if len(key_list) == 2:
        "It's so wrong. The sugar is gonna destroy my stomach lining."
    else:
        "But if I look like I totally regret it, he's gonna know. And no confidence means it's all over. He seems too nice for that."

label m2_c3_pass:
    $ aff += 2
    $ order = "cake"

    show taffy smile

    t "Oh, I like you."
    t "I'd join you if I wasn't on a diet, but I'll keep looking."
    l "Why? You look great."
    "Taffy's smile widens as the waiter leaves to get my usual order."
    "Phew... The stomach ache'll be worth it."

    jump menu2_end

label timeout2:
    $ aff += 1

    show taffy smile

    t "Hahaha! We still need some time to look, is that ok?"
    "The waiter nods and leaves us to mull over the menu."
    t "I heard that you were a good actor."
    l "I'm better without an audience."

    jump menu2_end

label bodyread2:
    $ aff += 2

    l "What was that?"

    show taffy pout

    t "What?"
    l "Your little lip twitch?"
    t "Oh, I just hate it when waiters don't give me any time to look."

    jump menu2_end

label menu2_end:

    l "...Can I ask you something?"

    show taffy smile

    l "Why are you wearing gloves?"
    t "Eczema. The pollen count in this city is killing me."

    if french_talk == True:
        l "Did you just move here from France?"

    else:
        l "Did you just move here? From where?"

    t "Minneapolis."
    l "L.A. must be a huge..."

    # set the time the player has
    $ current_time = 6.0
    $ total_time = 6.0
    $ do_start_timer = True

    $ fail_label = "timeout3"
    $ choice_menu = "menu3"

label menu3:
    if wait_dialogue == 1:
        $ menu_dialogue = "This city is so big I'm having a hard time figuring it out..."

    elif wait_dialogue == 2:
        $ menu_dialogue = "Oh, you think this city is big too? Haven't you lived in L.A. for a long time?"

    elif wait_dialogue == 3:
        $ menu_dialogue = "...There sure are a lot of, um... palm trees. Too. Are you sure you're okay?"

    else:
        $ wait_dialogue = 0
        $ menu_dialogue = "Are you from L.A.? Or did you move too?"

    menu:
        t "[menu_dialogue]"

        "Culture shock.":
            $ can_mash = True
            $ pass_label = "m3_c1_pass"
            $ mash_label = "m3_c1"
            $ key_list = ["w", "2", "q"]
            jump m3_c1

        "Temperature adjustment.":
            $ can_mash = True
            $ pass_label = "m3_c2_pass"
            $ mash_label = "m3_c2"
            $ key_list = ["2", "w"]
            jump m3_c2

        "City next to Minneapolis.":
            $ can_mash = True
            $ pass_label = "m3_c3_pass"
            $ mash_label = "m3_c3"
            $ key_list = ["q", "w"]
            jump m3_c3

label m3_c1:

    if len(key_list) == 3:
        "Really? The obvious? That's the best I could come up with?"
    elif len(key_list) == 2:
        "I might as well tell him the sky is blue. Totally boring response."
    else:
        "I should've asked my stunt double to do this. He's way better than 'culture shock'."

label m3_c1_pass:

    t "A little bit."
    l "A lotta bit?"
    t "A lotta bit..."
    t "You okay?"
    l "Yeah! Um... Fine. Totally fine."
    if start_key == "2":
        "I quickly tuck my hands back under the table."

    jump menu3_end

label m3_c2:

    if len(key_list) == 2:
        "Yeah. Very natural way to put that."
    else:
        "Talking about the weather is always a great icebreaker too. As everyone knows."

label m3_c2_pass:

    $ aff += 1

    t "Yeah, this is the lightest shirt I have."
    t "Am I sweating?"
    l "You look {i}hot,{i} but..."
    t "Hmhm... I better."

    jump menu3_end

label m3_c3:

    if len(key_list) == 2:
        "Is it clear enough that I actually wanna hear about what life was like over there?"
    else:
        "I mean everyone knows the big ones like New York and L.A., but I never hear about kinda underdog cities."

label m3_c3_pass:

    t "Yeah, this place feels like four cities in one!"
    t "And the traffic is insane! How do you get anywhere on time?!"
    l "I leave two hours early for everything."

    show taffy w_smile

    t "You're so strong. I can't get up any earlier than noon."

    jump menu3_end

label timeout3:

    show taffy worry

    $ timedout_3 = True

    "Taffy just starts fiddling with his coaster after he ran out of ways to fill the empty air."
    "God, I'm so sorry, Taffy..."

    jump menu3_end

label menu3_end:

    $ do_start_timer = False
    $ can_mash = False
    $ choice_menu = ""

    if timedout_3 == True:
        "The waiter mercifully comes back with my order."

    else:
        "The waiter comes back with my order."

    show taffy smile

    t "I think I'll have a steak. Rare."

    menu:
        "Really?!":
            $ aff += 1

            t "That much of a surprise?"
            l "Well... Yeah."
            t "I like keeping people on their toes."

            jump menu4_end

        "(Don't comment, just order your own food)":
            jump menu4_end

label menu4_end:

    if order == "cake":
        "I actually think this cake is so rich it's already spoiled my dinner."
        l "Just a bruschetta for me."

    elif order == "wine":
        "Steak actually sounds great with this wine."
        l "A ribeye. Medium."

    else:
        l "Seared salmon?"

    "The waiter nods before returning to the kitchen again."

    python:
        renpy.full_restart()
