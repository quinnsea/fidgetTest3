label maddie_intro:
    show maddie investigate
    hide screen dnd_ui
    hide screen inventory

    if seen_maddie == False:
        $ seen_maddie = True
        l "Hey, Maddie."
        m "Hey, Levi."
        "Everything feels wrong about looking at her."
        "Why is she smiling? Why isn't she wearing all black?"
        menu:
            "What's with the green?":
                $ champagne_dict["desc"] += " Got Maddie's black dress dirty."
                m "Oh, y'know."
                m "Deja popped the champagne and almost took my eye out."
                l "You alright?"
                m "Yeah, just wish I had a better dress."
                jump maddie_intro_cont
            "What's with the smile?":
                m "I-Is it that weird to smile at someone I haven't seen in over a year?"
                jump maddie_intro_cont
    else:
        jump maddie_ask

label maddie_intro_cont:
    m "Anyways, gotta host. Hope you're having fun."
    m "Deja told me to let you know that there's... something you should check out next door? At Jason's?"
    m "She's out back if you need her. Or some quiet."
    m "...And it's good to see you."

label maddie_ask:
    menu:
        "What should I ask her about?"

        "Mail" if "mail" in inventory_items:
            $ maddie_ask_jason = True

            m "You looked through my mail?"
            l "It was just laying there!"
            "Maddie glances at the table where I got it from, and sure enough there's plenty of other letters just laying on it."
            m "Ugh... I need to hire a new maid."
            l "...Did you write this?"
            m "No! Me and Jason aren't like that."
            m "We're just friends."
            "...Alright."

            jump maddie_ask

        "Black Fabric" if "black_fabric" in inventory_items:
            m "Huh."
            l "What?"
            m "Looks like my old dress."
            m "...Not old. The dress I was wearing before Deja got champagne all over it."
            l "Kinda old."
            m "I guess."
            m "I kinda think she did it on purpose. Our dresses weren't the {i}same,{/i} but they were pretty close."
            "Deja can get pretty... {b}territorial{/b} about her fashion."

            jump maddie_ask

        "Shoes" if "footprints" in inventory_items:
            $ seen_maddie_shoes = True
            if seen_deja_shoes == True:
                "I look down at her shoes, and yeah. Stilettos, just like the victim and Deja's."
                l "Hey, weird question, but are you and Deja the same shoe size?"
                m "Yeah. Can you steal her platforms for me?"
                m "It'd make a great birthday gift."
                "I laugh a little with her. Maddie loves the outdoors, they'd make a terrible birthday gift."
                "But her shoes are weirdly clean."

                jump maddie_ask

            else:
                "I look down at her shoes, and yeah. Stilettos, just like the victim's."
                "Size looks like it's probably the same, too."
                "But... weirdly clean."
                m "If you're about to ask if those WikiFeet are real, they're not."
                l "I don't care about your WikiFeet profile, Maddie. Just wanted to..."
                "She raises an eyebrow, there's no good way to phrase this."
                l "...{i}Figure out your shoe size.{/i}"
                m "Eight and a half, like Deja's."

                jump maddie_ask

        "Champagne" if "champagne" in inventory_items:
            m "Oh, you saw that?"
            l "Just the spill, what happened?"
            m "I dunno, Taffy gave Deja a champagne bottle."
            m "I could tell that it was gonna be a disaster, so I had to take off my shoes."
            m "Then I ran."
            m "I tried to stop her from popping it, but I figured 'DUCK!' would be a more useful thing to shout at a party than 'STOP!'"
            l "...So you weren't near her when she popped it?"
            m "No, I was. If I didn't, I'd lose a window."
            m "I made her point it down, so both of our dresses got fucked."
            m "It was close, though. The cork bounced off and hit the bottom of the table."
            l "Why did you even get a glass house?"
            m "It was cheap for the area and moving is haaaaard..."

            jump maddie_ask

        "Head" if "head" in inventory_items and maddie_ask_jason == True:
            $ know_samantha = True
            l "Do you know if Jason ever hung out with a blonde woman with yellow eyes?"
            m "...Yeah, I've seen his arm around someone like that."
            m "Samantha. She's an actress."
            m "A terrible one, but hey. If she was doing some 'favors' for Jason, it doesn't really matter."
            l "Terrible as in 'hard to work with' or terrible as in 'no talent'?"
            m "You want me to {i}choose?{/i}"
            m "She's an heiress to some huge company, it's all of the above."

            jump maddie_ask

        "Jason's House" if ("broken_door" or "security_system" in inventory_items) and maddie_ask_jason == True:
            l "You ever been to Jason's house?"
            m "Yeah, all the time. He has the best whisky."
            m "I would've borrowed some for tonight if he wasn't busy."
            l "Did you call him?"
            m "Why would I do that when he lives right next door?"
            m "I rang and he didn't answer, so I just left."

            jump maddie_ask

        "Never mind.":
            jump maddie_ask_end

label maddie_default:
    m "Why're you showing me that?"

    jump maddie_ask

label maddie_ask_end:
    hide maddie
    show screen dnd_ui

    call screen maddies_house_scene
