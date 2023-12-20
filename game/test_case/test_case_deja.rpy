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
            d "What about The All Seer?"
            l "He's always talking to you through that necklace, right?"
            d "That's right."
            d "He sees everything and tells me everything I need to know."
            d "Right down to the blades of grass I should walk on."
            d "Are you finally interested in joining the Cult?"
            d "He's been {i}very{/i} interested in you."
            l "Um... I'm still thinking about it."
            l "...What does he represent again?"
            l "The unknown?"
            d "The {i}fear{/i} of the unknown."
            "Not as bad as I remember."
            "Don't know why, but I felt like getting her shill was important. Oh, wait."
            l "Is he interested enough to help me with something?"
            d "...No."
            jump deja_ask

        "Roses" if "roses" in inventory_items:
            jump deja_default

        "Mail" if "mail" in inventory_items:
            d "Jason Hughes is having an affair with our dearest Madeline...?"
            l "Yeah. Weird, huh?"
            d "Weird in regards to {i}Madeline.{/i} Not so much for Jason."
            l "Really?"
            "Deja starts filing her nails as she rants off about him."
            d "Of course. He owes me, like, a shit ton of money."
            jump deja_ask

        "Black Fabric" if "black_fabric" in inventory_items:
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
            if inventory_item_desc[3] == "Caught on the fence in \nMaddie's backyard.":
                $ inventory_item_desc[3] += " Smells \nlike champagne."
            jump deja_ask

        "Shoes" if "footprints" in inventory_items:
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
                jump deja_ask

            else:
                l "...Hey, do you and Maddie have the same shoe size?"
                d "I didn't think that kind of information would concern you."
                l "Can you please just answer the question? It's hard enough to ask."
                "I can't even pretend that I'm okay with looking her in the eye."
                d "Yes, we did notice that we're wearing the same shoes."
                d "And the same size."
                d "It was like swapping glasses in class... surprisingly fun."
                jump deja_ask

        "Champagne" if "champagne" in inventory_items:
            d "Oh, the champagne was me."
            "I sigh."
            l "Was it the same way as last time?"
            d "Not exactly."
            d "Everyone still has both of their eyes."
            "I sigh again."
            jump deja_ask

        "Head" if "head" in inventory_items:
            d "Excellent work."
            l "Do you have any idea who this is?"
            d "No one you need to know."
            jump deja_ask

        "Jason's House" if "broken_door" or "security_system" in inventory_items:
            l "Have you ever been to Jason's house?"
            d "Jason...?"
            l "Hughes."
            d "Yes, a couple of times. But not for very long."
            d "Purely for business."
            if "security_system" in inventory_items:
                "So Deja definitely knew about the security system..."
            if "broken_door" in inventory_items:
                "Did she know about the broken door?"
            jump deja_ask

        "Never mind.":
            jump deja_ask_end

label deja_default:
    d "Unfamiliar."

    jump deja_ask

label deja_ask_end:

    hide deja
    show screen dnd_ui

    call screen maddies_backyard_scene
