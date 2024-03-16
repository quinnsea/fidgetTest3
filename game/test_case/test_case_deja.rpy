default deja_bite_ask = False

label deja_intro:
    show deja investigate at center
    hide screen dnd_ui

    if seen_body == False:
        d "Don't talk to me until you've gotten the head."
        "Oh, there's a vampire to kill next door. Gotcha."

        jump deja_ask_end

    if seen_deja == False:
        $ seen_deja = True
        d "Good evening, Levi."
        l "Not so great when there's a murder..."
        "But I know she doesn't care about that."
        "I can feel her smile getting wider as I think that."
        l "Something happen to your dress?"
        d "Oh, no, the designer made it that way."
        "...To look torn?"
        "If that's the style, I guess that's the style."

label deja_ask:
    menu:
        "What should I ask her about?"

        "Mh'elkug":
            jump deja_bite_end

        "Mail" if "mail" in inventory_items:
            jump deja_mail

        "Black Fabric" if "black_fabric" in inventory_items:
            jump deja_black_fabric

        "Shoes" if "footprints" in inventory_items:
            jump deja_footprints

        "Champagne" if "champagne" in inventory_items:
            jump deja_champagne

        "Head" if "head" in inventory_items:
            jump deja_head

        "Jason's House" if "broken_door" or "security_system" in inventory_items:
            jump deja_broken_door

        "Never mind.":
            jump deja_ask_end

label deja_mail:
    
    d "Jason Hughes is having an affair with our dearest Madeline...?"
    l "Yeah. Weird, huh?"
    d "Weird in regards to {i}Madeline.{/i} Not so much for Jason."
    l "Really?"
    "Deja starts filing her nails as she rants off about him."
    d "Of course. He owes me, like, a shit ton of money."

    jump deja_ask_end

label deja_black_fabric:

    d "Oh, that."
    d "I have no idea where it came from."
    l "...Did you even notice it until I pointed it out."
    d "Nope."
    l "...Do you {i}know{/i} where it could've come from?"
    d "It looks a lot like the dress Madeline was wearing before I spilled champagne all over it."
    "I take a whiff of the piece of fabric. It sure smells like it."
    l "How'd you spill it?"
    d "Do you remember how a certain former acquaintance of ours {i}became{/i} a former acquaintance?"
    "I sigh. I'm so disappointed in her."
    l "Someone let you pop a champagne cork?"
    d "Taffy insisted! He told me he could help!"
    l "Thanks, Deja..."
    if "champagne" not in black_fabric_dict["desc"]:
        $ black_fabric_dict["desc"] += " Smells like champagne."

    jump deja_ask_end

label deja_bite:
    if deja_bite_asked == True:
        jump deja_default
    else:
        $ deja_bite_asked = True

        d "So you were a little too late?"
        l "More like a lot too late."
        l "Or..."
        d "Or...?"
        "I blink when I realize I'm not sure whoever bit him."

        menu:

            "Jason was bitten by the victim.":

                $ bite_dict["desc"] += " Was bitten by the victim."

                l "Or she completely drained him out."
                d "Vampires usually drink a lot more from people they're familiar with."
                d "Kind of like serial killers."
                "Classic Deja."

                jump deja_bite_end

            "Jason was bitten by the killer.":

                $ bite_dict["desc"] += " Was bitten by the killer."

                l "Or the killer had a snack before they left."
                d "Or before killing your target?"
                l "How'd you know I didn't kill my target?"
                d "Mh'elkug told me."
                l "Did Mh'elkug tell you who did it?"
                "Even after knowing her for all these years, her laugh still sends a chill up my spine."
                d "He told me not to tell you."

                jump deja_bite_end

label deja_bite_end:

    d "Actually, that reminds me."
    d "Mh'elkug, The All Seer, wants to know if you're interested in joining the Cult."
    l "He always talks to you through that necklace, right?"
    d "That's right."
    d "He sees everything and tells me everything I need to know."
    d "Right down to the blades of grass I should walk on."
    l "Um... No. Still pass."
    "She keeps her empty smile at me, like she knows something I don't."
    l "...Is he interested enough to help me out?"
    d "No."

    jump deja_ask_end

label deja_purse:
    jump deja_default

label deja_wedding_ring:
    jump deja_default

label deja_body:
    if " Was bitten by the killer." in bite_dict["desc"]:
        "Do I really need to ask her about this?"
        "She knows I didn't do it."
        "And I know Mh'elkug doesn't give her information that quickly."
        "...Right?"
        d "Do you need something?"

        jump deja_body_end

    else:
        "Deja's the only person I can ask about these things."
        "I mean, she's the one that always points me to the vampires to kill anyways."
        l "So... I went over there."
        l "And I found the target's corpse."
        d "Oh?"
        d "Did you have another... episode?"
        "God, don't remind me. I'd like to think these hunts don't freak me out anymore."
        l "No. It was dead."
        l "And someone was at the top of the stairs."
        l "They pointed at me and rolled the head down the stairs..."

        jump deja_body_end

label deja_body_end:

    l "...Any idea who might've beat me?"
    d "Another vampire, maybe."
    d "I know there aren't any other vampire hunters in LA."
    l "After they dropped the head, they pointed at me."
    l "Like they knew me."
    d "Hm. They probably did."

label deja_grocery_list:
    jump deja_default

label deja_broken_door:
    l "Have you ever been to Jason's house?"
    d "Jason...?"
    l "Hughes."
    d "Yes, a couple of times. But not for very long."
    d "Purely for business."
    if "security_system" in inventory_items:
        "So Deja definitely knew about the security system..."
    "Did she break the door? Or was it broken before and she already knew about it?"

    jump deja_ask_end

label deja_footprints:
    "I take a look at Deja's shoes."
    $ seen_deja_shoes = True
    if seen_maddie_shoes == False:
        "Stilettos, just like the victim."
        "Size looks the same too."
        "A little dirty, she probably didn't stick to the path."
        "I never get why people don't do it, I know it's inconvenient but..."
        "I need to stop looking at Deja's feet, I feel like a freak."
        d "Is there something you want to ask me about, Levi?"
        l "...Not really."
        jump deja_ask_end

    else:
        l "...Hey, do you and Maddie have the same shoe size?"
        d "I didn't think that kind of information would concern you."
        l "Can you please just answer the question? It's hard enough to ask."
        "I can't even pretend that I'm okay with looking her in the eye."
        d "Yes, we did notice that we're wearing the same shoes."
        d "And the same size."
        d "It was like swapping glasses in class... surprisingly fun."
        jump deja_ask_end

label deja_champagne:
    d "Oh, the champagne was me."
    "I sigh."
    l "Was it the same way as last time?"
    d "Not exactly."
    d "Everyone still has both of their eyes."
    "I sigh again."
    jump deja_ask_end

label deja_head:
    d "Excellent work."
    l "Do you have any idea who this is?"
    d "No one you need to know."
    jump deja_ask_end

label deja_security_system:
    jump deja_broken_door

label deja_default:
    d "Unfamiliar."

    jump deja_ask

label deja_ask_end:

    hide deja
    show screen dnd_ui

    call screen maddies_backyard_scene
