default food_inventory = []
default hates_sweets = False
default called_dion = False
default talk_writing = False

label dialogue_demo_start:

    scene bg rest

    "20 minutes..."
    "Most people would leave after 20 minutes, wouldn't they?"
    "But traffic is really bad in this city. Maybe they just got stuck or lost."
    "A waiter offers me some salad."
    "I don't like eating before my dates, but I'm so hungry I might have to break that rule."

menu:
    "Thanks.":
        $ food_inventory.append("salad")
        w "Of course. And more water?"
        jump salad_end

    "No thanks.":
        w "Alright. Let me know if you need anything else."
        w "Want some more water?"
        jump salad_end

label salad_end:
    "I nod quietly."
    w "If you weren't such a klutz, I'd leave the whole pitcher."
    "I end up glaring daggers back at her. God dammit. I know she's just teasing, but my knee jerk reaction just takes it personally."
    "She looks a little scared to talk to me now, but she clears her throat and tries to recover."
    w "But it's okay! That rug was hideous! Glad we had an excuse to get rid of it!"
    "A lot of actors are a lot more sociable than I am."
    "But I just feel like I'm too famous."
    "I can't help but think every time I click with someone, they're just playing games."
    "They don't want a friend, they want a connection. I'm just a shot at a conversation with Maddie to them."
    "Before I get a chance to dig myself that hole, a tall man framed with long, blond curls walks up to my table."
    "This must be Taffy."
    "I stand up and offer my hand to shake. He gently holds it, but doesn't move his hand."
    "His piercing pink eyes look me up and down. It's a little... It's different. I've never been on the receiving end of a look like this before."
    "With a hummed chuckle, he kisses the back of my hand before sitting down. I can feel a heat rush to my cheeks and my heartbeat feels heavier. I sit back down."
    "My throat closes up. I don't know if I'm more afraid of him or how much I'm already falling for him."
    "When Taffy sits down I realize that I didn't hear a word he said."
    mc "...Sorry, what was that?"
    t "I said I like your glasses."
    mc "Oh. Thanks, I guess."
    t "Mortimer, right?"
    "He's not using my stage name."
    mc "Yeah, and you're Taffy?"
    t "That's right. Taffeta for long."
    "...Huh?"
    "Oh. Like Taffy for short."
    "The laugh that comes out of me is late and way too forced. I see a couple of people turning their heads to look at the noise."
    "I take a couple of deep breaths in shame. I need to calm down. It's showtime."

    $ fail_label = "m1_fail"
    $ choice_menu = "m1_start"
    $ do_start_timer = True

    jump m1_start

label m1_start:

    if wait_dialogue == 1:
        $ menu_dialogue = "I might need a minute, I was too busy looking at {i}you{/i} to look at the menu."

    elif wait_dialogue == 2:
        $ menu_dialogue = "Don't worry so much about what you're gonna order. I won't judge."

    else:
        $ wait_dialogue = 0
        $ menu_dialogue = "Do you know what you want?"

    menu:
        t "[menu_dialogue]"

        "Why didn't you call me Dion?":
            $ key_list = ["w", "2"]
            $ pass_label = "m1_c1_pass"
            $ mash_label = "m1_c1"

            jump m1_c1

        "No, I really thought it was funny.":
            # eye contact and smile
            $ key_list = ["q", "w"]
            $ pass_label = "m1_c2_pass"
            $ mash_label = "m1_c2"

            jump m1_c2

        "I'm really nervous.":
            $ key_list = ["2"]
            $ pass_label = "m1_c3_pass"
            $ mash_label = "m1_c3"

            jump m1_c3

label m1_c1:

    if len(key_list) == 2:
        "Oh, that's a big question isn't it? I'm a little scared to ask it."

    else:
        "But it's an important one. What if he's avoiding it on purpose? There's no way he doesn't know about me, but what if I sound like a freak?"

label m1_c1_pass:

    $ called_dion = True

    t "{i}Is{/i} that your name?"
    t "Carol told me it was just your stage name."
    "Oh. Duh."
    mc "No, she's right."
    mc "I'm just used to people calling me Dion, I guess."
    t "Well, that doesn't sound very fair."
    "He bats his eyelashes, like he wants me to ask. I'll give it to him."
    mc "What makes you say that?"
    t "You aren't always on the clock, are you?"
    t "You're not Dion, you're Mortimer."
    "Huh. Weirdly nice to hear."

    jump dion_q1

label m1_c2:

    if len(key_list) == 2:
        "That's easy. I just can't look fake."

    else:
        "I can't leave Taffy hanging. I already feel bad for taking too long to laugh."

label m1_c2_pass:

    mc "It just took me a minute to realize what you were saying."
    "I say it with a light chuckle, but that was too blunt, wasn't it?"
    t "Sorry! Ahaha!"
    t "I promise, I have better ones. Give me another chance."
    mc "...I'll think about it."
    t "Heyyy!"
    "I'm so relieved that managed to come across as a joke."

    jump m1_end

label m1_c3:

    "I can't just {i}say{/i} that, can I?! If he knows I'm nervous, he's just gonna freak out and run away!"

label m1_c3_pass:

    "Taffy smiles eagerly at that, shifting his eyes left and right before leaning in."
    "His hand stays cupped around the corner of his mouth like he's telling me a secret."
    t "{i}I haven't been on a date in eight years.{/i}"
    mc "I haven't been on a {i}good{/i} date in six."
    "The words slip out without me thinking about it, and I'd seriously put my hands over my mouth if I wasn't playing a character."
    "But Taffy rewards me with his sweet, sweet laugh, and all that worry just melts away."
    "It really is like music to my ears, and while my heart races, the pace feels a lot... lighter."

    jump m1_end

label m1_fail:

    "My voice dies in my throat, and I can't get myself to speak."
    "Taffy gives me a confused look with the dead air... but he's still smiling."
    t "Cute."
    "I can feel my soul melting in this chair."

    jump m1_end

label m1_end:

    if "salad" in food_inventory:

        "Taffy finally looks down at my half-eaten salad."
        "Shit. {i}Shit.{/i} I knew that was a terrible idea. I look like an even bigger asshole than I usually do."
        t "Did I take that long?"
        mc "I just didn't eat lunch."
        t "Does that happen a lot?"
        "Ohhhh no, he's worried. I can tell. I quickly shake my head and one of my hands before he gets any ideas."
        mc "N-No, no. It's rare, but I got really sucked into this script for my next movie."
        mc "It's always exciting to get a new role, especially when it's so different from what I usually do. But this script is really special. Spent the whole day reading it."
        t "Oh? What was it about?"
        mc "Can't tell you. Signed an NDA."
        "It's the worst thing about acting, but I feel like it makes me interview better."
        "The second I finally get a chance to say something, I don't shut up about it. Until then it feels awful."
        "Taffy pouts, but he moves on."

        jump salad_end1

    else:

        jump salad_end1

label dion_q1:

    mc "So, um... How do you know Carol?"
    t "I'm her story editor."
    mc "For her shows?"
    t "Yeah."
    "The tension floats out of my shoulders and throat. Film and TV aren't {i}that{/i} far apart, but writing and acting is."
    "There's nothing Taffy would want to gain out of me that he can't already get."
    t "You ever think about getting into TV?"
    "The question makes me feel like he's in my head, but the tone implies more interest than that. Like he thinks I'd be good at it."
    "I get that tone from Deja a lot. I just shake my head as I sip my water."
    mc "Too much work."
    "That spits a good laugh out of Taffy. Ohhh, it's such a cute laugh..."
    t "You're kidding!"
    mc "Am I {i}wrong?{/i}"
    t "Nooo, noooo... I guess not."
    t "...{i}Is{/i} it?"
    mc "Well, {i}now{/i} we gotta find out."
    t "How long does it take you to film a movie again?"
    mc "Like a couple months."
    mc "How long does it take you to record a season?"
    t "6 months."
    "{b}Six months?!?!{/b}"
    "I can't resist it. I can't even take a breath to hide it through a performance. I'm frowning."
    "I'm pouting. My brows are furrowed. Because I know TV shows make less than movies."
    "If I have one blockbuster, I don't have to do shit for the rest of the year."
    "If I get an award, I don't even have to {i}audition{/i} for a few years."
    mc "And you just... edit? You never pitch your own stuff?"
    t "Hey, whose turn is it?"
    mc "Yours..."
    "He beams at me for going along with his mildly obvious power trip."
    "Taffy hums and looks around the restaurant before a question pops into his head."
    t "Do you do your own stunts?"
    mc "Yep."
    "I answer with a little bit too much speed and eagerness."
    "You'd think that I'd get that question a lot more. I don't. I never get that question."
    "People just assume that I don't, and I find it a little insulting."
    mc "Including that tuck and roll out of the exploding car in Blueberry Sunset. All practical effects, too."
    t "Whoa! So you... actually could've died!"
    "A smile finds itself worming into my cheeks in spite of his worry."
    mc "Yep."
    mc "I {i}did{/i} get hurt on set once."
    "He leans in, demanding the story with his gaze."
    mc "So... Did you see Unholy Ghost?"
    t "That movie about the spy that can talk to ghosts? Yeah, like three times."
    mc "And that scene where I'm running and I throw down the little card that turns into a motorcycle?"
    t "And you ride the motorcycle off a cliff to cut off that gang of exorcists?"
    mc "Yeah, I tripped."
    t "Ooooooohhhh..."
    mc "The motorcycle fell on my leg, and..."
    "I pull up my pant leg and gesture for Taffy to duck down and look at it."
    "A huge scar goes up my shin where my fibula got cracked."
    t "That's why it got delayed?!"
    mc "Yeah."
    "I don't really get embarrassed about my injuries or stunt work."
    "For me, it's what makes acting fun."

    jump sweets_end

label salad_end1:

    t "You come here often?"
    mc "Yeah, {i}too{/i} often. They give me free dessert all the time."
    "Taffy sits upright with a slam of his hand onto the table. I jump in my seat. Did... Did I say something wrong?"
    "His head turns to look at the kitchen door and back at me a few times before finally telling me what he wants to say."
    t "...You think that's a bad thing?"
    mc "U-Um..."

    $ fail_label = "sweets_fail"
    $ choice_menu = "sweets_menu"

    jump sweets_menu

label sweets_menu:
    if wait_dialogue == 1:
        $ menu_dialogue = "What about chocolate mousse? Ugh, I've been on this diet and it's just killing me!"

    elif wait_dialogue == 2:
        $ menu_dialogue = "I think I miss ice cream the most, but this place is fancy. I bet they have tiramisu."

    elif wait_dialogue == 3:
        $ menu_dialogue = "If they offer you some, I can have it if you don't want it."

    elif wait_dialogue == 4:
        ## show taffy batting his eyelashes or whatever
        $ menu_dialogue = "...Please. I meant 'Can I have it if you don't want it? ...Pretty please?'"

    else:
        ## reset taffy's sprite
        $ wait_dialogue = 0
        $ menu_dialogue = "I love sweets! Do they ever bring you chocolate cake?"

    menu:
        t "[menu_dialogue]"

        "I'd rather have extra bread.":
            $ key_list = ["w", "2"]
            $ pass_label = "sweets_c1_pass"
            $ mash_label = "sweets_c1"

            jump sweets_c1

        "I didn't say that. (Lie)":
            $ key_list = ["w"]
            $ pass_label = "sweets_c2_pass"
            $ mash_label = "sweets_c2"

            jump sweets_c2

label sweets_c1:

    if len(key_list) == 2:
        "God, sometimes the truth is a lot harder to tell. I don't want him to think I'm weird."
    else:
        "But I gotta look like I mean it, too. Maybe... confidence is what he wants? I dunno..."

label sweets_c2:

    "It's... Okay, I guess it's a half-truth. It doesn't make lying any easier."

label sweets_c1_pass:

    t "{i}Really?{/i} Is the bread here that good?"
    mc "I just don't like sweets."
    "Taffy seems pretty confused about that answer."
    "But I don't think it's the answer he's confused about. More that I'm nervous about confessing that in the first place."
    "Like he can see right through the fact that I don't know if this will work if we don't agree on everything."
    "He slides his hand across the table towards me and gestures for me to give him mine."
    "I hesitantly put my hand in his."
    "Taffy holds it gently, and his thumb lightly rubs the back."
    "He's still smiling at me. This much eye contact would normally kill me, but with Taffy I feel... calm."
    "I take a deep breath."
    t "Then that means more for me."
    "It's a really dumb epiphany."
    "It's not even an epiphany, it's just a painfully obvious fact."
    "I feel so embarrassed. I can't look at him when I laugh."
    "Taffy laughs along with me, it's nice to finally be around someone I can really let loose around."
    "I feel really vulnerable around him."
    "In a weirdly good way."

    jump sweets_end

label sweets_c2_pass:
    "It's not about the sweets, even though I don't really like sweets that much. It's about getting recognized as a regular."
    "I don't really need these people acknowledging me and getting familiar."
    "My eye contact breaks, and Taffy sees that as an opening."
    t "Then what's the real problem?"
    "I'm a little embarrassed to admit that…"
    #omg it'd be very cool if i could add mashing to the middle of the dialogue can we try to put a nervous cue here and prevent progressing dialogue until you do it successfullyyyy omg
    #maybe put a timer???? idk there should be SOME indication that you can mash here
    #nested mash success:
    #if successful, skip the menu where you order the main course and automatically go to an option not in the dialogue choices
    mc "I just really don't like strangers looking at me."
    mc "I'm always getting judged. I know people don't always say what they're thinking."
    mc "And I can be really careless about what I say. What if people think I'm a dick? What if I slip up once around the wrong person and I can't work in this town again?!"
    mc "I love acting, but the social politics is just so…"
    "I've been avoiding looking at Taffy up to this point, looking at my hands as I try to squeeze them in an attempt to calm down. I can't tell if it's helping."
    "But Taffy's gaze does. I don't look at him directly, I don't know if I can anymore. That was way too vulnerable."
    "He doesn't look like he thinks I'm being stupid, at least. Taffy's smile is soft and patient. My mind is completely at ease around it."
    "I just need to stay in the moment."
    t "I get how that can be scary."
    t "Especially when you're as big as you are. People expect a lot out of you. Even off the set."
    "I quietly nod, realizing my throat has been tense. I've been gritting my teeth the whole time, too. My dentist is gonna kill me."
    "The thought makes a chuckle huff out my nose."
    mc "Sorry."
    t "I'm just sorry you don't have anyone else you can talk to about this."
    t "But it's alright. Take all the time you need."
    t "Want a drink?"
    t "My treat. Don't even try to fight me on that."
    mc "...Alright."
    "He waves down a waiter to pour me a glass of wine."

    $ food_inventory.append("wine")

    jump sweets_end

label sweets_fail:

    "I stare him down, trying to look tough with my arms crossed. But I can feel the tension in my shoulders hike up no matter how much I try to fight it."
    t "Alright, alright. My bad for trying to get a free cake outta this."
    "Ugh. No, Taffy. It's my bad for not being able to tell that's what you were getting at."
    "I sigh like the silent treatment was intentional. Feigning disappointment that Taffy was trying to toy with me. I think that story is good enough to sell."

    jump sweets_end

label sweets_end:

    "The lull that comes in throws me off."
    "An awkward bit of silence between our talking. I don't wanna give my mind the chance to go off on another spiral."
    "I look into Taffy's eyes for a path. The way his curls bounce with his giggle is perfect."
    "Those pink eyes are so easy to get trapped in. I'm completely hypnotized."
    "I'm afraid to talk, my lips part and a noise comes out."
    "Taffy tilts his head, perfectly patient. Not realizing that I was going to just blubber and babble complete nonsense."
    "I'm really not good at small talk. He was doing such a good job carrying it before."
    "But I gotta show him that I'm interested too. Even though this character isn't interested in anyone."
    mc "So... Who are you wearing?"
    "That not-joke got him so good he snorted."
    t "Excuse me?"
    mc "Oh, do you not know the designer?"
    mc "It's a really unique blouse, I figured someone handmade it for you."
    t "It's cute that you think I make enough money to shell out a few thousand for a shirt."

    if called_dion == True:

        mc "I thought you worked with Carol."

    else:

        mc "I thought you knew Carol."

    t "She pays better than everyone else, but the bar is in the Earth's core."
    t "But that's on me, I'm not picking up a lot of jobs right now."
    mc "Are you not picking 'em up or is no one biting?"
    t "I said I'm not picking them up."
    "Damn, I didn't know he could bite so hard."
    t "Editing means I have to care, and I don't really care much about what's out right now."

    if called_dion == False:

        mc "Really? What kind of editor are you?"
        t "Script editor. I'd like to think I'm one of the best, but I don't have to think."
        t "I know."

    mc "Then why not try writing?"
    t "I don't think I'm ready. Walk before I can run, y'know?"

    $ fail_label = "m2_fail"
    $ choice_menu = "m2_start"

    jump m2_start

label m2_start:
    if wait_dialogue == 1:
        $ menu_dialogue = "I might need a minute, I was too busy looking at {i}you{/i} to look at the menu."

    elif wait_dialogue == 2:
        $ menu_dialogue = "Don't worry so much about what you're gonna order. I won't judge."

    else:
        $ wait_dialogue = 0
        $ menu_dialogue = "\'I\'m sure you\'re a great writer!\' Would be nice to say if I could without a lick of snark."

    menu:
        "[menu_dialogue]"

        "What'd you edit?":
            $ key_list = ["w"]
            $ pass_label = "m2_c1_pass"
            $ mash_label = "m2_c1"

            jump m2_c1

        "I struggled too.":
            $ key_list = ["w", "2", "q"]
            $ pass_label = "m2_c2_pass"
            $ mash_label = "m2_c2"

            jump m2_c2

        "I might have a script you can look at." if "salad" in food_inventory:

            $ renpy.hide_screen("countdown")

            t "Don’t."
            "What does he mean?"
            t "This is a date."
            t "I’m not here to network. I’m here to spend time with you."
            "I don’t know how I forgot that for a second."
            "...Wait, am I the problem?"
            "No, Taffy’s just different."
            "His passion for being an editor looks a little flaky at best, I think."
            "And even then, I’m not exactly the right person to go to for something like that."
            "I close my eyes and take a deep breath, accepting the fact that he wasn’t trying to get something out of me."
            "But even if I thought he was, it’s weird how effortlessly I fell for it."
            "The whole point of playing the asshole is to make it clear that it’s not gonna work."
            "Huh. Did he catch that?"
            mc "Thanks. Again."
            t "Well, I couldn’t just sit here and have fun without you."
            mc "Hm?"
            t "If you’re not having fun, {i}I’m{/i} not having fun, silly."
            "A noise squeaks out of the back of my throat."
            "I’m so embarrassed I sink a little bit in my chair. I could’ve hid under the tablecloth and ran off in shame. I really could have. I almost did."

            jump m2_end

        "I might have a script you can look at. (disabled)" if "salad" not in food_inventory:

            pass

label m2_c1:

    "You know, I know next to nothing about the editing process. It’d actually be pretty good to hear about."

label m2_c1_pass:

    $ talk_writing = True

    t "Daybreak, Crushing Nightmares, Escape from Santa Cruz… Actually, I did some work on Jude Candle, too."
    mc "Escape from Santa Cruz?!?!"
    mc "I almost killed my agent over not getting that one!"
    t "And I almost killed the writer for seriously thinking catchphrase comedy is funny."
    t "Didn’t know you were interested in comedies, I thought you only did dramas and action movies."
    mc "Action movies are just overproduced comedies these days."
    mc "You said you did some editing on Jude Candle. You know that."
    t "Of course, that’s your best movie."
    mc "Maddie’s too."
    mc "She actually hates making action movies, but there was something special about that one."
    mc "We had a ton of fun with it."
    t "That scene where you got patched up was exactly how I pictured it in my head."
    t "I’m so glad you and Azar are such good actors. And Maddie’s a director that actually knows what she’s doing. It would’ve killed me if those jokes didn’t land."
    mc "That was my favorite part! You wrote that?!"
    t "Pretty much. Writer said it didn’t need it, so thanks for proving them wrong."
    mc "See? You’re a great writer!"
    mc "That was one of my first gigs, and it completely ruined those scenes for me in other movies."
    mc "You just made it sound so natural. It was heavy, but light enough to not completely break the tone."
    mc "And the humor made you really appreciate the characters and see their chemistry."
    t "Y’know if you think something sounds weird in a script you don’t have to follow it perfectly, right?"
    mc "Yeah, I’m just…"
    "Taffy bats his eyelashes in surprise. I was so in it, I really did love every movie that he edited for."
    "I can’t believe I didn’t notice his name in the credits, but maybe he used a pseudonym."
    mc "I can’t do improv."
    mc "Thinking on my feet just isn’t a thing for me."
    t "Well, I bet it makes you pretty easy to work with."
    t "And you’re doing a pretty good job talking to me."
    "No, Taffy. You’re doing a fucking great job carrying me."
    t "If you figure out improv, I don’t think anyone would forget you."
    t "You’d be like… Humphrey Bogart."
    mc "{i}You think I could be Bogie?{/i}"
    "That’s the greatest compliment anyone has ever given me. Ignoring the weird stuff about him."
    "I didn’t even notice some of the people at other tables jumping a bit when my voice got louder."
    "Well, until now. Even better, it only kinda bothers me."

    jump m2_end

label m2_c2:

    if len(key_list) == 3:

        "That’s a lot to admit on a first date, especially the reason why."

    elif len(key_list) == 2:

        "I don’t know what’s harder, the sell or just growing the balls to say it."

    else:

        "If he has any connections to any tabloids, I think it’d kill me."

label m2_c2_pass:

    mc "My connections got me in this industry, not my talent."
    mc "It’s easy to get impostor syndrome, but if you wanna do it you gotta give it a try."
    "That’s definitely a better way to phrase it than the truth."
    "Hunting vampires in exchange for roles, hah! Like he’d believe that."
    "He’d run. With good reason."
    "I hum and look up for a bit. Did Deja tell me I had a target nearby tonight?"
    t "No, connections get you started."
    t "Talent makes you stay."
    t "Unless you’re someone’s kid."
    mc "Or you have a lot of dirt on the right person."
    mc "So are you someone’s kid, or do you have a lot of dirt?"
    "Taffy gives me a very wide, exaggerated smile. I can’t tell if he’s trying to be creepy or tell a joke."
    "Probably both."
    t "Oh, I have dirt on everyone."
    "I’m 90% sure it’s supposed to be a joke, but it’s not gonna stop me from tensing up."
    "His warm gaze gets ice cold, piercing daggers into my skin."
    "It feels real, is it real? What does he know about me? Was this all a set up to–"
    "Spiraling, Mortimer. Get a hold of yourself."
    "I laugh too hard. Way too hard. My chest even hurt a little bit, but I can’t let him know I’m a little tense."

    jump m2_end

label m2_fail:

    mc "Yeah, I bet you\’re a {i}great{/i} writer."
    "What the fuck is wrong with me. That was such an easy line, normally I {i}don’t{/i} say anything when I’m stuck. Suddenly, this one time, where it’s the worst thing possible I could say?"
    "I cross my arms to hide my frustration with myself, and Taffy rightfully rolls his eyes."
    "I am so horribly sorry, but too afraid to admit it."
    "The tone carries better if I act like I don’t care, right?"

    jump m2_end

label m2_end:

    if "wine" in food_inventory:

        "The waitress comes back with a bottle of the merlot Taffy got for me earlier."
        w "More wine? This is the one Hank got you, right?"
        t "Yep. If you want some more, Mortimer, go for it. My treat."
        "Well, if you insist."
        "I nod and let her refill my glass."
        w "And are you guys ready to order, or do you need some more time?"

    else:

        "The waitress comes back with a pitcher of water to top me off."
        "She flashes a smile at me, but I’m really not sure why."
        "She’s seen me here plenty of times, and I’ve always been a little bit of an ass to her."
        "I bet she’s just excited that someone else is talking to me for this long."
        "Weird. I didn’t think she cared."
        w "Are you guys ready to order, or do you want some more time?"

    "Taffy glances at his phone for a brief moment and his eyes widen a bit."
    t "Nothing for me."
    mc "...Gotta go?"
    t "Nah, just intermittent fasting. I got here way too late."
    t "And time flies when you’re having fun."
    "Be still my beating heart…"
    "Either way, I’m still hungry."
    "Do I go with my usual or something that makes me seem less like a pretentious wad?"

    $ do_start_timer = False
    $ choice_menu = "food_menu"

label food_menu:

    menu:

        "Duck Confit with Dauphinoise":

            $ food_inventory.append("duck")

            jump food_choice_end

        "Burger":

            $ food_inventory.append("burger")
            "Why did I say that? Why did I say that?"
            "I could’ve picked {i}anything{/i} and I picked the burger. I hate beef. She knows that. Her eyes are even widening in shock at me picking that."
            w "...Will that be the beef chuck, veal, or lamb?"
            "{b}Thank you.{/b}"
            mc "{i}I’ll take the lamb.{/i}"

            jump food_choice_end

label food_choice_end:

    "I can’t help it. I do so much shit for this money."
    "Vampire hunting, blackmail, interviews, co-starring with Adrian Miller. Like eight times."
    "I have to make it a little bougie."
    "But Taffy doesn’t seem to mind. Or care."
    w "I’ll send this to the kitchen right away."
    "She’s as quick as ever, but the restaurant is pretty busy."

    if "salad" in food_inventory:

        "I can wait."
        "Taffy sort of watches her leave, and I wonder if he regrets ordering something for himself."
        "But it’s not really my business."
        "I still look at him like he’ll have a new topic on his forehead."
        t "You know her?"
        mc "Yeah, sort of. Been here a lot."
        mc "Wouldn’t really call her a friend."
        mc "But I know she isn’t into guys."
        "The jealousy seeps out of my mouth. I can’t hide the acidity."
        "It feels ridiculous that I’m even jealous at all. I just met Taffy."
        "I don’t really hit it off this well with a lot of people, either."
        "The last thing I want is to lose the chance at something good just because I slipped."
        "It’s a bad sign, though. A really bad sign to bite that soon."
        "But Taffy’s smile just gets wider."
        t "I’m not into girls."
        t "Or seeing any more than one person at a time."
        "Phew."
        mc "Me neither."
        "Taffy hums a brief giggle, leaning in and actually looking more comfortable."
        ##there could maybe be a detection point here maybe i’d have to look at the code again tho
        t "I just really wish I could have those eclairs…"
        mc "I could probably get ‘em to go for you when she comes back."
        t "Nah, it’s alright."
        mc "...You sure?"
        "I can practically hear him drooling."
        t "Yeah, I can’t really change my mind on it."
        t "I don’t do intermittent fasting because I’m trying to lose weight or anything like that."
        t "I have a heart condition. It’s the only thing that really helps."

        jump heart_cond

    else:

        "...I should’ve gotten that damn salad."
        "Now {i}I’m{/i} gonna have to make conversation so I can avoid thinking about how hungry I am."
        mc "How’s the intermittent fasting working for you?"
        "Really? Did I {i}have{/i} to make it about food?"
        t "Pretty good, actually."
        t "I have a little bit of a heart condition. Surprised it’s helping."
        "Damn, that {i}sucks.{/i}"

        if called_dion == True:

            "If I couldn’t do my own stunts, I’d blow my brains out."

        jump heart_cond

label heart_cond:

    mc "What kinda heart condition?"
    t "Cardiomyopathy. My heartbeat’s weaker."
    t "Had it my whole life. Really, it’s not too bad. It got me outta gym."
    mc "You didn’t like gym?"
    t "You did?"

    if called_dion == True:

        t "I guess I shouldn’t be surprised, Evel Knievel."

    t "I’ve never heard of a theater kid that likes gym."
    mc "I actually wasn’t a theater kid."
    mc "I was a..."

    $ do_start_timer = True
    $ fail_label = "m3_fail"
    $ choice_menu = "m3_start"

    $ current_time = 6.0
    $ total_time = 6.0

label m3_start:

    if wait_dialogue == 1:
        $ menu_dialogue = "Honesty’s the best policy, but not when it’ll out me."

    elif wait_dialogue == 2:
        $ menu_dialogue = "I know that cheerleaders aren’t always girls. It’s still... The stigma, or whatever."

    else:
        $ wait_dialogue = 0
        $ menu_dialogue = "I don’t wanna tell him, I don’t wanna tell him, I so badly don’t wanna tell him."

    menu:
        "[menu_dialogue]"

        "Gymnast":
            $ key_list = ["2", "q"]
            $ pass_label = "m3_c1_pass"
            $ mash_label = "m3_c1"

            jump m3_c1

        "Football Player":
            if "wine" in food_inventory and "salad" not in food_inventory:
                $ max_mash = 15.0
            $ key_list = ["w", "q"]
            $ pass_label = "m3_c2_pass"
            $ mash_label = "m3_c2"

            jump m3_c2

        "Cheerleader (Truth)":
            if "wine" in food_inventory and "salad" not in food_inventory:
                $ max_mash = 15.0
            $ key_list = ["2", "q", "w"]
            $ pass_label = "m3_c3_pass"
            $ mash_label = "m3_c3"

            jump m3_c3

label m3_c1:

    if len(key_list) == 2:

        "I don’t really like the idea of me in spandex. It sounds weird."

    else:

        "I had body image issues before, and I have body image issues now. But I can’t look that way. I gotta look happy with my body."

label m3_c1_pass:

    t "{i}Really?{/i}"
    mc "You’re surprised?"
    t "Well, yeah. Carol told me you were a bit of a klutz."
    "It was {b}one{/b} time!"
    "...Huh, I didn’t remember her being there."
    mc "It’s really not that bad."
    t "I don’t doubt it."
    t "But you {i}are{/i} a lot braver than I am."
    t "I’ll trip once in a new pair of shoes, and I’ll burn them."
    mc "Sounds more superstitious than scared."
    t "Hahah, well you’re not wrong about that."
    t "I’ve seen a ghost."
    mc "Oh, yeah?"
    t "Yeah. I had a vacation in Savannah, and there was this guy walking around my hotel."
    t "Puffing a cigarette and playing pool."
    t "Asked a maid about him, and she said he was a… special guest."
    t "But I don’t think the maid was real either!"
    mc "Whoa…"
    "I have no idea if I actually sounded impressed."
    mc "It’s supposed to be the most haunted city in the country, isn’t it?"
    t "Something like that."
    t "I think New Orleans is probably haunteder."
    t "...More haunted, oh my god I can’t believe I said that."
    "We have a pretty decent chuckle about it. Honestly, I probably would’ve said the same thing."
    mc "It should be a real word."
    t "You know what, you’re right. It should."

    jump m3_end

label m3_c2:

    if len(key_list) == 2:

        "I’m almost laughing at myself for coming up with that one. That’s a hard sell."

    else:

        "You know what, maybe laughing will keep the edge off the lie if looking at him doesn’t work.."

label m3_c2_pass:

    "He’s laughing too. Good. We agree it's a ridiculous bold-faced lie."
    t "You’re not buff!"
    "Okay, that kinda hurts. I spin my head around my neck to avoid showing the pain. Taffy’s little snort eases the burn a little."
    t "Sorry, sorry!"
    mc "It’s alright. I’m sure you use that on every guy."
    "Taffy laughs even harder. God, his snorting is so cute."
    t "What was it like being the most popular kid in school?"
    "Oh my god, of course he asked that. {i}{b}Why did I say that?!{/b}{/i}"
    mc "Uh... I-I... My... grades were, um..."
    t "What did you {i}actually{/i} do?"
    mc "I... danced."
    t "What kinda dance?"
    mc "Um..."
    "Stop looking at me, I’m trying to come up with a better lie than ‘football player’."
    t "It’s okay if you don’t wanna tell me."
    mc "...Sorry."
    t "You sound so sweet when you apologize, I don’t think anyone’s heard you do that outside of a role before."
    t "Spoiling me a little."
    extend " It’s like I’m seeing the real you."

    if talked_writing == True:

        t "Improv just takes a bit of practice."
        mc "Yeah, I just hate practicing."
        mc "I know acting is lying, but just talking to people shouldn’t be like that."
        t "Fine, then you don’t gotta practice with me."

label m3_c3:

    if len(key_list) == 3:

        "God, please, no, I know the truth will set you free or whatever, but I don't believe it. Not this time."

    elif len(key_list) == 2:

        "I don’t know, I just don’t know. This is just a little too personal, especially for a first date."

    else:

        "I can’t trust that he’s gonna be normal about it or think I was a male cheerleader. It’s LA, I know everyone’s more progressive but it’s not 100%. It’s never 100%. I don’t even think he’s from here."

label m3_c3_end:

label m3_end:

    $ max_mash = 10.0
    $ current_time = 5.0
    $ total_time = 5.0
