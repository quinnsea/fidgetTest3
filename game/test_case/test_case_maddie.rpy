default maddie_purse_talked = False

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
                if "champagne" not in black_fabric_dict["desc"]:
                    $ black_fabric_dict["desc"] += " Has champagne on it."
                m "Oh, y'know."
                m "Deja popped the champagne and almost took my eye out."
                l "You alright?"
                m "Yeah, just wish I had another black dress."
                jump maddie_intro_cont

            "What's with the smile?":
                m "I-Is it that weird to smile at someone I haven't seen in over a year?"
                jump maddie_intro_cont
    else:
        m "Hope you're having fun."
        jump maddie_ask_end

label maddie_intro_cont:
    m "Anyways, gotta host. Hope you're having fun."
    m "Deja told me to let you know that there's... something you should check out next door? At Jason's?"
    m "She's out back if you need her. Or some quiet."
    m "...And it's good to see you."

    jump maddie_ask_end

label maddie_ask:
    menu:
        "What should I ask her about?"

        "Mail" if "mail" in inventory_items:
            jump maddie_mail

        "Black Fabric" if "black_fabric" in inventory_items:
            jump maddie_black_fabric

        "Shoes" if "footprints" in inventory_items:
            jump maddie_footprints

        "Champagne" if "champagne" in inventory_items:
            jump maddie_champagne

        "Head" if "head" in inventory_items and maddie_ask_jason == True:
            jump maddie_head

        "Jason's House" if ("broken_door" or "security_system" in inventory_items) and maddie_ask_jason == True:
            jump maddie_broken_door

        "Never mind.":
            jump maddie_ask_end

label maddie_default:
    m "Why're you showing me that?"

    jump maddie_ask_end

label maddie_mail:
    $ maddie_ask_jason = True

    m "You looked through my mail?"
    l "It was just laying there!"
    "Maddie glances at the table where I got it from, and sure enough there's plenty of other letters just laying on it."
    m "Ugh... I need to hire a new maid."
    l "...Did you write this?"
    m "No! Me and Jason aren't like that."
    m "We're just friends."
    "...Alright."

    jump maddie_ask_end

label maddie_black_fabric:
    m "Huh."
    l "What?"
    m "Looks like my old dress."
    m "...Not old. The dress I was wearing before Deja got champagne all over it."
    l "Kinda old."
    m "I guess."
    m "I kinda think she did it on purpose. Our dresses weren't the {i}same,{/i} but they were pretty close."
    "Deja can get pretty... {b}territorial{/b} about her fashion."

    jump maddie_ask_end

label maddie_footprints:
    $ seen_maddie_shoes = True
    if seen_deja_shoes == True:
        "I look down at her shoes, and yeah. Stilettos, just like the victim and Deja's."
        l "Hey, weird question, but are you and Deja the same shoe size?"
        m "Yeah. Can you steal her platforms for me?"
        m "It'd make a great birthday gift."
        "I laugh a little with her. Maddie loves the outdoors, they'd make a terrible birthday gift."
        "But her shoes are weirdly clean."

        jump maddie_ask_end

    else:
        "I look down at her shoes, and yeah. Stilettos, just like the victim's."
        "Size looks like it's probably the same, too."
        "But... weirdly clean."
        m "If you're about to ask if those WikiFeet are real, they're not."
        l "I don't care about your WikiFeet profile, Maddie. Just wanted to..."
        "She raises an eyebrow, there's no good way to phrase this."
        l "...{i}Figure out your shoe size.{/i}"
        m "Eight and a half, like Deja's."

        jump maddie_ask_end

label maddie_champagne:
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

    jump maddie_ask_end

label maddie_head:
    $ know_samantha = True
    l "Do you know if Jason ever hung out with a blonde woman with yellow eyes?"
    m "...Yeah, I've seen his arm around someone like that."
    m "Samantha. She's an actress."
    m "A terrible one, but hey. If she was doing some 'favors' for Jason, it doesn't really matter."
    l "Terrible as in 'hard to work with' or terrible as in 'no talent'?"
    m "You want me to {i}choose?{/i}"
    m "I'd seriously kick her off my cast if I could, but my hands are tied every time I gotta work with Jason."
    "Maddie seems to be tensing up at the mention of that. If I squint, I think I can see her shaking a bit."
    "This must really piss her off."
    l "You alright?"
    m "What?"
    m "Oh, yeah. Yeah, I'm fine."
    m "Just considering the existential dread of probably having to make her the lead one day."

    jump maddie_ask_end

label maddie_broken_door:
    l "You ever been to Jason's house?"
    m "Yeah, all the time. He has the best whisky."
    m "I would've borrowed some for tonight if he wasn't busy."
    l "Did you call him?"
    m "Why would I do that when he lives right next door?"
    m "I rang and he didn't answer, so I just left."

    jump maddie_ask_end

label maddie_security_system:

    jump maddie_broken_door

label maddie_grocery_list:
    m "Why do you have my grocery list?"
    l "I wanted to see what kind of cheese you got for tonight."
    m "You never had manchego with truffle before?"
    l "Uh, no. I can't say I have."
    "I wanna save it with scoffing and pretending like it's a joke, but it came out way too mean. I can't save that."
    m "I can bring you some next time we hang out."
    l "Sounds like a plan. Thanks."
    "Maddie takes the grocery list from my hands... Fair, but it still sucks."
    python:
        for item in inventory_sprites:
            if item.type == "grocery_list":
                removeInventoryItem(item)

    jump maddie_ask_end

label maddie_purse:

    if maddie_purse_talked == False:
        $ maddie_purse_talked = True
        m "Where'd you get that ugly thing?"

        $ choice_menu = "maddie_purse_choice"
        $ do_start_timer = True

        $ current_time = 5.0
        $ total_time = 5.0

        jump maddie_purse_choice

    else:

        jump maddie_default

label maddie_purse_choice:

    if wait_dialogue == 1:
        $ menu_dialogue = "Maddie, help me out here."
    elif wait_dialogue == 2:
        $ menu_dialogue = "If you do, I'll let you keep it."
    else:
        $ wait_dialogue = 0
        if know_samantha == True:
            $ menu_dialogue = "Shit, shit. She might know that it's Samantha's."
        else:
            $ menu_dialogue = "Ugh. No, I thought you'd know the designer or something."

    $ do_start_timer = True

    menu:
        "[menu_dialogue]"
        "I thought someone lost it.":
            $ pass_label = "maddie_purse1_pass"
            $ mash_label = "maddie_purse1"
            $ fail_label = "maddie_purse1_fail"
            $ key_list = ["2", "q"]

            jump maddie_purse1

        "How much could you fit in this?":
            $ pass_label = "maddie_purse2_pass"
            $ mash_label = "maddie_purse2"
            $ fail_label = "maddie_purse2_fail"
            $ key_list = ["w"]

            jump maddie_purse2

label maddie_purse1:
    if len(key_list) == 2:
        "Oh, no. There's no way she's gonna believe that. Maybe if I act shy about it."
    else:
        "Wait, I'm trying to look like I'm helping. I can't just be shy, I gotta make it look like I have good intentions."

label maddie_purse1_pass:
    m "No one here would carry anything like that."
    m "There's no wallet in there that says whose it is?"
    l "Nope. Totally empty."
    m "Pfft, it might be a present."
    m "Maybe their partner wanted to see 'em bring it, but they were too embarrassed to say it was ugly."
    m "Or something."
    l "Are you speaking from experience?"
    "Maddie avoids eye contact with a nervous smile. It's hard not to laugh, and I start getting nervous when I let out a snort."
    "My chest gets tight when I realize I insulted her, but she laughs with me."
    m "At least someone appreciates my trauma dumping."

    jump maddie_purse_pass_cont

label maddie_purse1_fail:
    "My throat dries up. My mouth opens, but I can't get myself to say anything."
    "What if she doesn't believe it? What if she finds out there's a murder and she thinks I did it?"
    m "...Sorry. Did you like it?"
    l "No, don't apologize."
    "I get too embarrassed to even try bringing it up and tuck the purse back away."

    jump maddie_ask_end

label maddie_purse2:
    "It's just a question. An honest question. This one should be easy, just make it clear."

label maddie_purse2_pass:
    $ purse_dict["desc"] += " Could've had her phone in it."
    m "The basics. Phone, wallet, keys."
    m "Keys might be pushing it, though. It's a little small."
    l "But not too small to be just an accessory?"
    m "No purse is just an accessory, we don't have pockets."
    m "And even the ones that {i}do{/i} have pockets are so tiny you can only fit your thumbs in it."
    "I clear my throat. I forgot. It's been too long since I wore womens' pants, I try to forget the nightmares."
    l "Right..."
    "That makes it extra weird that it's empty."

    jump maddie_purse_pass_cont

label maddie_purse2_fail:
    "I wanna beat my head against the wall. I can't even get the nerve to ask a question."
    m "Are you alright, Levi?"
    "I didn't even realize that I'm tearing up a little bit when she asks."
    l "Yeah, it's nothing."
    l "Allergies is all."
    "I can lie about that but I can't even ask a question?!"
    m "Alright."

    jump maddie_ask_end

label maddie_purse_pass_cont:
    m "So, where'd you find it?"
    "God, why didn't I take those improv classes when I had the chance?"
    "I almost call out asking for a line, but she manages to save me."
    m "Doesn't matter. Enjoy the free purse, I guess."

    jump maddie_ask_end

label maddie_bite:
    jump maddie_default

label maddie_wedding_ring:
    jump maddie_default

label maddie_body:
    jump maddie_default

label maddie_ask_end:
    $ do_start_timer = False
    hide maddie
    show screen dnd_ui

    call screen maddies_house_scene
