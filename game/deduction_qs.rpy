default deduction_1 = ""
default deduction_2 = ""
default deduction_3 = ""
default deduction_4 = ""
default deduction_5 = ""

default deja_culprit_points = 0
default maddie_culprit_points = 0
default taffy_culprit_points = 0

label deduction_q1:
    menu:
        "How did the killer get in?"

        "The victim let them in" if "phone" in purse_dict["desc"]:

            "That'd explain why the phone was missing."

            $ deduction_1 = "let in"

            jump deduction_check

        "??? (disabled)" if "phone" not in purse_dict["desc"]:
            pass

        "Through the front door" if footprints_dict["action"] == "Belongs to" and footprints_dict["herring_action"] != "Doesn't matter":

            "There were plenty of footprints, it wouldn't be weird for anyone to come in through the front door."
            "But if they did, their shoes would probably have to be dirty."

            $ deduction_1 = "door"

            jump deduction_check

        "??? (disabled)" if footprints_dict["action"] != "Belongs to" or footprints_dict["herring_action"] == "Doesn't matter":
            pass

        "Over the fence, through the back door" if black_fabric_dict["action"] == "Was on" or black_fabric_dict["action"] == "Was dropped by" or black_fabric_dict["action"] == "Belongs to":

            "That piece of black fabric was caught on the fence."
            "Maddie normally wears all black, and Deja's black dress was a little torn."

            $ deduction_1 = "fence"

            jump deduction_check

        "??? (disabled)" if black_fabric_dict["action"] != "Was on" or black_fabric_dict["action"] != "Was dropped by" or black_fabric_dict["action"] != "Belongs to":
            pass

        "Turned into mist":

            "Well, I saw it for myself, right?"
            "Vampires {i}can{/i} turn into mist, or really anything if they're good enough."
            "Maybe they snuck in and just hid out for a while."

            $ deduction_1 = "mist"

            jump deduction_check

label deduction_q2:
    menu:
        "Why did they kill the victim?"

        "??? (disabled)" if know_samantha == False:
            pass

        "Out of revenge" if know_samantha == True:

            $ deduction_2 = "revenge"

            "I know there's nothing Maddie hates more than having hands tied on {i}anything{/i} when it comes to making a movie, but {i}especially{/i} actors and scripts."
            "She can live with a bad location or pretty weird sound design. Even awful effects and cinematography."
            "But if the actors can't carry it and the script's too hard to work with, she crumbles."
            "...I wouldn't be surprised if she killed Samantha for this."

            jump deduction_check

        "??? (disabled)" if jason_money == False:
            pass

        "For money" if jason_money == True:

            $ deduction_2 = "money"

            "Jason does owe a lot of people a lot of money."
            if know_samantha == True:
                "And if he's sugaring Samantha, killing her could free up some cash."
            else:
                "If someone was trying to steal from him and get rid of any witnesses, killing the only person there is kind of an obvious choice."

            jump deduction_check

        "Out of love" if deduction_3 == "jason" and mail_dict["state_changed"] == True:

            $ deduction_2 = "love"

            "Maddie {i}did{/i} have that letter to Jason."
            "And she saw that woman in the house with him. She might've gotten fed up."
            "Especially since she's a lot more..."
            "I'm not finishing that sentence. There's no way to say that without sounding like a dick."

            jump deduction_check

        "??? (disabled)" if "killer" not in bite_dict["desc"]:
            pass

        "In the way" if "killer" in bite_dict["desc"] or deduction_3 == "jason":

            $ deduction_2 = "in the way"

            "Jason was the real target."
            if know_samantha == True:
                "Samantha was probably just in the way and already visiting him."
            else:
                "The vampire was probably just in the way and already visiting him."
            "It might've been some form of an unfortunate accident."

            jump deduction_check

        "No idea":
            $ deduction_2 = "idk"
            "...Is there anything that definitively points one way or the other?"
            "Every motive I've been looking at was for {b}Jason.{/b} Not the vampire."
            "Ugh... I don't think I could bring her up."
            "I feel like even mentioning her name would make me look suspicious."
            if know_samantha == True:
                "I know Maddie didn't like her, but Maddie doesn't like anyone. That's not enough to kill her."
                "...Right?"

            jump deduction_check

label deduction_q3:
    menu:
        "Who was the real target?"

        "??? (disabled)" if know_samantha == False:
            pass

        "Samantha" if know_samantha == True:
            $ deduction_3 = "sam"

            "Samantha was the vampire, and the culprit pointed at {i}me{/i} after they rolled her head down the stairs."
            "The culprit could've killed me. Easily. But they didn't."
            "She might have been the real target."

            jump deduction_check

        "Jason":
            $ deduction_3 = "jason"

            "The killer {i}actually{/i} wanted to kill Jason, but the vampire was already there."
            "There's a lot of reasons to kill Jason. And he has a ton of enemies."
            "It could've been him."

            jump deduction_check

        "Levi":
            $ deduction_3 = "levi"

            "The killer {i}did{/i} point at me specifically."
            "It'd be weirder if I wasn't the target."
            "It'd be even weirder if they didn't do that just to psych me out. Keep my blood pressure up whenever they finally kill me."
            "...I have no idea if I'll be able to sleep tonight knowing there's someone out there waiting to kill me."
            "Someone that read my mind {b}knowing{/b} I went to this party just to kill a target."
            "I take a deep breath to avoid spiralling."
            "We don't know for sure."
            "There's a very good chance it's just my paranoia talking."

            jump deduction_check

label deduction_q4:
    menu:
        "How did the killer get out?"

        "Mist":
            $ deduction_4 = "mist"

            "Well, doy. I {i}saw{/i} them turn into a cloud of mist."
            "Still doesn't hurt to keep it in mind."
            "And remember that vampires usually can't shapeshift back and forth that quickly."
            "Not unless they've been a vampire for a few hundred years. At least."

            jump deduction_check

label deduction_q5:
    menu:
        "How did the killer cover their tracks?"

        "??? (disabled)" if broken_door_dict["herring_action"] != "Was broken by":
            pass

        "Broke the back door" if broken_door_dict["herring_action"] == "Was broken by":
            $ deduction_5 = "broke door"
            "If the killer broke the back door, it'd get rid of any reason for someone to think they jumped the fence."

            jump deduction_check

        "??? (disabled)" if black_fabric_dict["herring_action"] != "Was planted by":
            pass

        "Planted the black fabric on the fence" if black_fabric_dict["herring_action"] == "Was planted by" or black_fabric_dict["state_changed"] == True:
            $ deduction_5 = "planted fabric"

            if "black dress" not in champagne_dict["desc"] or black_fabric not in inventory_sprites:
                "The black fabric could've been torn from Deja's dress."

            else:
                "The black fabric could've been torn from Deja or Maddie's dress."

            jump deduction_check

        "??? (disabled)" if "phone" not in purse_dict["desc"] and deduction_1 != "let in":
            pass

        "Stole the victim's phone" if "phone" in purse_dict["desc"] and deduction_1 == "let in":
            $ deduction_5 = "stole phone"

            "The victim's phone wasn't in her purse."
            "If the killer knew the victim and called her to say they were coming, taking the phone would get rid of the record."
            "At least if she was using a burner. But I don't know if she was."
            if know_samantha == False:
                "I don't even know her name..."

            jump deduction_check

        "Who knows?":
            "Who knows indeed."

            jump deduction_check

label deduction_check:
    if deduction_1 == "fence":
        $ deja_culprit_points += 1
        $ maddie_culprit_points += 1

    elif deduction_1 == "door":
        $ taffy_culprit_points += 1

    elif deduction_1 == "let in":
        $ taffy_culprit_points += 1

    if deduction_2 == "money" or deduction_2 == "in the way":
        $ deja_culprit_points += 1

    elif deduction_2 == "love":
        $ maddie_culprit_points += 1

    elif deduction_2 == "revenge":
        $ maddie_culprit_points += 1
        $ taffy_culprit_points += 1

    elif deduction_2 == "idk":
        $ taffy_culprit_points += 1

    if deduction_3 == "jason":
        $ deja_culprit_points += 1
        $ taffy_culprit_points += 1

    elif deduction_3 == "sam":
        $ maddie_culprit_points += 1
        $ taffy_culprit_points += 1

    elif deduction_3 == "levi":
        $ taffy_culprit_points += 1

    if deduction_5 == "broke door":
        $ deja_culprit_points += 1

    elif deduction_5 == "planted fabric":
        $ maddie_culprit_points += 1

    elif deduction_5 == "stole phone":
        $ taffy_culprit_points += 1

    $ print("taffy points: " + str(taffy_culprit_points))
    $ print("maddie points: " + str(maddie_culprit_points))
    $ print("deja points: " + str(deja_culprit_points))

    #hide deduction_page

    if deja_culprit_points >= 4:
        "So, let's get this story straight."
        "Deja knew Maddie lived next door to Jason and got to the party before me on purpose."
        "She knew about Maddie and the victim's affair with Jason."
        "So she got rid of Maddie's alibi by popping the champagne and forcing her to change."
        "Deja tried to climb in through the back, but her dress got caught on the fence."
        "And the back door was broken. She figured people could mistake it for Maddie's and left out the front door."
        "Mh'elkug told her when to go and where to step so her footprints would match the victim's."

        menu:
            "Is this really how it happened?"

            "Yes":
                "Yeah. Definitely Deja."
                "I can't see any other reason for her to get here so much earlier than me unless she wanted to get away with murder."
                "...Am I in danger?"

                $ MainMenu(confirm=False)()

            "No":
                $ taffy_culprit_points = 0
                $ maddie_culprit_points = 0
                $ deja_culprit_points = 0
                "No, if Deja is that strong, she wouldn't be sending me after these vampires in the first place."
                "And she might be obsessed with money, but there's no way she'd {i}kill{/i} someone over it, right?"
                "...That's... what she has me for..."
                "...Right?"

                $ renpy.hide_screen("say")

                $ renpy.call_screen(current_scene)

    elif maddie_culprit_points >= 4:
        "So, let's get this story straight."
        "Maddie was fed up with Jason and wanted to confront him about the {i}other{/i} woman he's cheating on her with: Samantha."
        "Before the party, she tried to get in through the front door, but he wouldn't answer."
        "So she climbed her fence and caught her dress on it."
        "She came in through the back, sucked all of Jason's blood, and killed Samantha when she realized she was still in the house."
        "And after that, she jammed the back door. Even if someone thought she did it, there'd be no point of entry."
        "She even cleaned up her shoes so she wouldn't leave any footprints."
        "And made Deja spill the champagne on the floor so anyone could confuse the tear for {i}Deja's{/i} dress."

        menu:
            "Is this really how it happened?"

            "Yes":
                "Anyone would be pissed if they were double cheated on."
                "Of course it's Maddie. Who else could write that letter?"

                $ MainMenu(confirm=False)()

            "No":
                $ taffy_culprit_points = 0
                $ maddie_culprit_points = 0
                $ deja_culprit_points = 0
                "No, that's... That's just ridiculous."
                "Maddie never mixes sex with work."
                "She's too... professional to do something like that."
                "...Right?"
                "Plus, Taffy was the one that made Deja spill the champagne, not Maddie."

                $ renpy.hide_screen("say")

                $ renpy.call_screen(current_scene)

    elif taffy_culprit_points >= 4:
        "So, let's get this story straight."
        "Taffy called the victim to get let into Jason's house."
        "He, um... You know what, I don't know why he was going to Jason's house."
        "I don't even feel 100% confident about who the real target is."
        "But the phone was missing from her purse, and by process of elimination he's the only person who'd probably have her number."
        menu:

            "Is this really how it happened?"

            "Yes":
                "Yeah... Taffy did it."
                "I don't know why he did it, but I believe this story makes sense."

                $ MainMenu(confirm=False)()

            "No":
                $ taffy_culprit_points = 0
                $ maddie_culprit_points = 0
                $ deja_culprit_points = 0
                "Nah... That... doesn't make any sense."
                if "black_fabric" in inventory_sprites and mail_dict["state_changed"] == True:
                    "It doesn't explain the fabric on the fence."
                    "And how would Taffy be able to force that letter that perfectly?"
                elif mail_dict["state_changed"] == True:
                    "How would Taffy be able to forge that letter that perfectly?"
                elif "black_fabric" in inventory_sprites:
                    "It doesn't explain the fabric on the fence."
                "I don't think there's any conclusion that's gonna be a perfect fit, but I can't even figure out a motive for Taffy."

                $ renpy.hide_screen("say")

                $ renpy.call_screen(current_scene)

    else:
        $ taffy_culprit_points = 0
        $ maddie_culprit_points = 0
        $ deja_culprit_points = 0

        window hide

        $ renpy.call_screen(current_scene)

    ## deja's deductions:
    ## 1) jumped the fence and got her dress caught on it
    ## 2) killed samantha for money OR because she was in the way
    ## 3) jason was the real target
    ## 5) broke the door to cover her tracks

    ## maddie's deductions:
    ## 1) walked in through the front door
    ## 2) killed samantha out of love OR out of revenge
    ## 3) samantha was the real target
    ## 5) planted the black fabric to cover her tracks

    ## taffy's deductions:
    ## 1) taffy was let in by samantha OR walk in through the front door
    ## 2) out of revenge OR no idea
    ## 3) mortimer was the real target
    ## 5) stole the victim's phone to cover his tracks
