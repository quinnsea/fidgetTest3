label taffy_intro:
    show taffy investigate
    hide screen dnd_ui

    if seen_taffy == False:
        $ seen_taffy = True
        l "Um... hi."
        #"I find myself weirdly starstruck."
        #"Even though I've never heard of this guy before."
        ta "Oh, Dion! You were in this movie?"
        l "No, just a friend of Maddie's."
        "I take the stranger's hand to shake." #His skin is so smooth."
        ta "Taffy. I helped with the writing."
        l "Levi. Dion's just my stage name."

    #if seen_body == False:
    #    jump taffy_ask_end
    #else:
    #    jump taffy_ask
    jump taffy_ask

label taffy_ask:
    menu:
        "What should I ask him about?"

        "Mail" if "mail" in inventory_items:
            show taffy investigate
            jump taffy_mail

        "Black Fabric" if "black_fabric" in inventory_items:
            show taffy investigate
            jump taffy_default

        "Shoes" if "footprints" in inventory_items:
            show taffy investigate
            jump taffy_footprints

        "Champagne" if "champagne" in inventory_items:
            show taffy investigate
            jump taffy_champagne

        "Head" if "head" in inventory_items:
            show taffy investigate
            jump taffy_head

        "Jason's House" if ("broken_door" or "security_system" in inventory_items) and taffy_ask_jason == True:
            show taffy investigate
            jump taffy_broken_door

        "Never mind.":

            jump taffy_ask_end

label taffy_mail:
    "Taffy leans in after I read out the letter."
    #"I can feel my legs turning to jello when he whispers in my ear."
    ta "Where'd you get this?" ##THIS WOULD BE AN APPROPRIATE DIALOGUE FREAK OUT PLACE
    l "Maddie's end table."
    "Taffy blinks in surprise with a hand up to his mouth."
    l "...Do you believe it?"
    ta "Well, Jason lives right next door, doesn't he?"
    ta "And they do work on a lot of projects together..." ## this would also be a good place for taffy to do a twitch, but for now i'll just put a nested option

    if taffy_ask_jason == False:

        menu:

            "You know Jason?":
                $ taffy_ask_jason = True

                ta "Hard not to. He's a pretty big producer."
                ta "Or {i}was.{/i} I think Maddie's his last lifeline."
                ta "And now... we know why..."
                jump taffy_mail_cont

            "(Don't say anything)":

                jump taffy_mail_cont

    else:
        jump taffy_mail_cont

label taffy_mail_cont:

    ta "{i}I'll keep it between us.{/i}"
    "Oh no. If Taffy is a writer, he probably knows every tabloid in Hollywood."
    "This really {i}could{/i} ruin Maddie."
    "And make whoever calls it out a {b}shit ton of money...{/b}"
    ta "Are you okay?"
    l "Y-Yeah. Just... Sorry, wasn't thinking."
    ta "You're fine."
    #"I didn't realize how close I was to tears until he broke me out of it."

    jump taffy_ask_end

label taffy_black_fabric:

    jump taffy_default

label taffy_bite:

    jump taffy_default

label taffy_purse:

    jump taffy_default

label taffy_wedding_ring:

    jump taffy_default

label taffy_body:

    jump taffy_default

label taffy_grocery_list:

    jump taffy_default

label taffy_broken_door:

    if taffy_ask_jason == False:
        jump taffy_default

    else:
        l "Have you ever been to Jason's house before?"
        ta "Jason Hughes?"
        l "Mhm."
        ta "Nope! Looking to rob it?"
        l "What?"
        ta "What?"
        ta "I'm kidding."
        "I laugh a lot harder than I should at that."

        jump taffy_ask_end

label taffy_footprints:

    "I glance down at Taffy's shoes and blurt it out without thinking."
    l "Do we have the same shoes?"
    "He looks down with me and lets out a little laugh when I point it out."
    ta "Oh my god, we do!"
    "These shoes are so common, I run into people that wear them all the time."
    ta "Here, I wanna see if we have the same size."
    "I put my foot down next to his."
    "Huh. Sure enough, same size."

    jump taffy_ask_end

label taffy_champagne:

    "Taffy hisses a slow breath of air after I bring up the champagne."
    ta "{i}Yeah, that was a mistake...{/i}"
    ta "I was trying to teach Deja how to pop it. My bad."
    ta "You think Maddie is mad about the dress?"
    l "Maybe, but she'll get over it."

    jump taffy_ask_end

label taffy_head:

    "I can't show it to him, but I might be able to figure out who it is if I {i}describe{/i} it."

    if taffy_ask_jason == True:

        l "Hey, you've seen Jason, right?"
        ta "Like once, why?"
        l "Oh, I was just curious if you ever saw him with a woman with long, blonde hair."
        l "Pale with these... really pretty yellow eyes."
        ta "Hmm..."
        ta "Nnnnope, can't say I have."
        "Damn."

        jump taffy_ask_end

    else:
        "...I feel like her description alone would be too vague."
        "Maybe if he knew about her relationship with Jason?"

        jump taffy_ask_end

label taffy_default:

    show taffy investigate

    ta "Hm? What's that?"

    jump taffy_ask_end

label taffy_ask_end:

    hide taffy
    show screen dnd_ui

    call screen maddies_house_scene
