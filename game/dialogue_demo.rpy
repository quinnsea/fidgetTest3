default has_salad = False
label dialogue_demo_start:
    "20 minutes..."
    "Most people would leave after 20 minutes, wouldn’t they?"
    "But... traffic is really bad in this city. Maybe they just got stuck... Or lost."
    "A waiter offers me some salad."
    "I don’t like eating before my dates, but I’m so hungry I might have to break that rule."

menu:
    "Thanks.":
        $ has_salad = True
        w "Of course. And more water?"
        jump m1_end

    "No thanks.":
        w "Alright. Let me know if you need anything else."
        w "Want some more water?"
        jump m1_end

label m1_end:
    "I nod quietly."
    w "If you weren’t such a klutz, I’d leave the whole pitcher."
    l "Heh... I’m still so sorry about last time."
    w "It’s okay! That rug was hideous! Glad we had an excuse to get rid of it!"
    "A lot of actors are a lot more sociable than I am."
    "But... I dunno, I just feel like I’m too famous."
    "I can’t help but think that every time I click with someone, they’re trying to manipulate me into getting a role."
    "...I wonder if they think I just hate them."
    "Before I get a chance to dig myself that hole, a tall man framed with long, blond curls walks up to my table."
    "This must be Taffy."
    "I stand up and offer my hand to shake. He gently holds it, but doesn’t move his hand."
    "His piercing pink eyes look me up and down. It’s a little... It’s different. I’ve never been on the receiving end of a look like this before."
    "With a hummed chuckle, he kisses the back of my hand before sitting down. I can feel a heat rush to my cheeks and my heartbeat feels heavier. I sit back down."
    "My throat closes up... I don’t know if I’m afraid of him or how much I’m already falling for him."
    "When Taffy sits down I realize that I didn’t hear a word he said."
    l "...Sorry, what was that?"
    t "I said I like your glasses."
    l "Oh, um... Th-Thanks."
    t "Levi, right?"
    "He’s not using my stage name..."
    l "Yeah... And you’re Taffy?"
    t "That’s right. Taffeta for long."
    "...Huh?"
    "Oh. Like Taffy for short."
    "The laugh that comes out of me is late and a bit forced."
    "I take a couple of deep breaths in shame. I need to calm down. It’s showtime."
    ## timer GO
    $ timer_dialogue = "It was a pretty bad joke, wasn’t it?"
    $ timer_dialogue = "Sorry, you get it when something sounds better in your head, don’t you?"
    $ fail_label = "m1_fail"

    menu:
        t "{timer_dialogue}"

        "Why didn’t you call me Dion?":
            $ key_list = ["w", "2"]
            $ pass_label = "m1_c1_pass"
            $ mash_label = "m1_c1"
            # eye contact and nerves
             # timer text
             # timer text
            # success text
            t "{i}Is{/i} that your name?"
            t "Carol told me it was just your stage name."
            "...Oh. Duh."
            l "No, she’s right."
            l "I’m just... used to people calling me Dion, I guess."
            t "Well, that doesn’t sound very fair."
            "He bats his eyelashes, like he wants me to ask. I’ll give it to him."
            l "...What makes you say that?"
            t "You aren’t always on the clock, are you?"
            t "You’re not Dion, you’re Levi."
            "...Is he reading my mind?"
            jump dion_q1

        "No, I really thought it was funny.":
            # eye contact and smile
            $ key_list = ["q", "w"]
            $ pass_label = "m1_c2_pass"
            $ mash_label = "m1_c2"
            "That’s easy. I just can’t look fake." # timer text
            "I can’t leave Taffy hanging. I already feel bad for taking too long to laugh..." # timer text
            # success text
            l "It just took me a minute to realize what you were saying."
            "I say it with a light chuckle, but that was too blunt and honest, wasn’t it?"
            t "Sorry! Ahaha!"
            t "I promise, I have better ones. Give me another chance."
            l "...I’ll think about it."
            t "Heyyy!"
            "That recovery was so smooth. I’m a bit jealous."
            jump m1_end

        "I’m really nervous.":
            $ key_list = ["2"]
            $ pass_label = "m1_c3_pass"
            $ mash_label = "m1_c3"
            "I can’t just {i}say{/i} that, can I?! If he knows I’m nervous, he’s just gonna freak out and run away!" # timer text
            # success text
            "Taffy smiles eagerly at that, shifting his eyes left and right before leaning in."
            "His hand stays cupped around the corner of his mouth like he’s telling me a secret."
            t "{i}I haven’t been on a date in eight years.{/i}"
            l "I haven’t been on a {i}good{/i} date in six."
            "The words slip out without me thinking about it, and I’d seriously put my hands over my mouth if I wasn’t playing a character."
            "But Taffy rewards me with his sweet, sweet laugh, and all that worry just melts away."
            "It really is like music to my ears, and while my heart races, the pace feels a lot... lighter."
            jump m1_end

label m1_c1:

    if len(key_list) == 2:
        "Oh, that’s a big question isn’t it? I’m a little scared to ask it."

    else:
        "But it’s an important one. What if he’s avoiding it on purpose? There’s no way he doesn’t know about me, but what if I sound like a freak?"

label m1_fail:

    "My voice dies in my throat, and I can’t get myself to speak."
    "Taffy gives me a confused look with the dead air... but he’s still smiling."
    t "Cute."
    "I can feel my soul melting in this chair."
    jump m1_end

# failure text end
# overall end (unless they successfully picked the dion question)

if has_salad == True:
    "Taffy finally looks down at my half-eaten salad."
    "Oh no..."
    t "Did I take that long?"
    l "I just... didn’t eat lunch. Wasn’t hungry."
    t "Does that happen a lot?"
    "Ohhhh no, he’s worried. I can tell. I quickly shake my head and one of my hands before he gets any ideas."
    l "N-No, no. I just got sucked into the new script I got."
    l "I spent the whole day reading it."
    t "Oh? What was it about?"
    l "Can’t tell you. Signed an NDA."
    "He didn’t even bring up that I’m a movie star... I wonder if there’s a reason for that."
    "Taffy pouts, but he moves on."
    jump salad_end1
else:
    jump salad_end1

label dion_q1:
    l "So, um... How do you know Carol?"
    t "I’m her story editor."
    l "For her shows?"
    t "Yeah."
    "The tension floats out of my shoulders and throat. Film and TV aren’t {i}that{/i} far apart, but writing and acting is."
    "There’s nothing Taffy would want to gain out of me that he can’t already get."
    t "You ever think about getting into TV?"
    "The question makes me feel like he’s in my head, but the tone implies more interest than that. Like he thinks I’d be good at it."
    "I get that tone from Deja a lot. I just shake my head as I sip my water."
    l "Too much work."
    "That spits a good laugh out of Taffy. Ohhh, it’s such a cute laugh..."
    t "You’re kidding!"
    l "Am I {i}wrong?{/i}"
    t "Nooo, noooo... I guess not."
    t "...{i}Is{/i} it?"
    l "Well, {i}now{/i} we gotta find out."
    t "How long does it take you to film a movie again?"
    l "Like a couple months."
    l "How long does it take you to record a season?"
    t "6 months."
    "{b}Six months?!?!{/b}"
    "I can’t resist it. I can’t even take a breath to hide it through a performance. I’m frowning."
    "I’m pouting. My brows are furrowed. Because I know TV shows make less than movies."
    "If I have one blockbuster, I don’t have to do shit for the rest of the year."
    "If I get an award, I don’t even have to {i}audition{/i} for a few years."
    l "And you just... edit? You never pitch your own stuff?"
    t "Hey, whose turn is it?"
    l "Yours..."
    "He beams at me for going along with his mildly obvious power trip."
    "Taffy hums and looks around the restaurant before a question pops into his head."
    t "Do you do your own stunts?"
    l "Yep."
    "I answer with a little bit too much speed and eagerness."
    "You’d think that I’d get that question a lot more. I don’t. I never get that question."
    "People just assume that I don’t, and I find it a little insulting."
    l "Including that tuck and roll out of the exploding car in Blueberry Sunset. All practical effects, too."
    t "Whoa! So you... actually could’ve died!"
    "A smile finds itself worming into my cheeks in spite of his worry."
    l "Yep."
    l "I {i}did{/i} get hurt on set once."
    "He leans in, demanding the story with his gaze."
    l "So... Did you see Unholy Ghost?"
    t "That movie about the spy that can talk to ghosts? Yeah, like three times."
    l "And that scene where I’m running and I throw down the little card that turns into a motorcycle?"
    t "And you ride the motorcycle off a cliff to cut off that gang of exorcists?"
    l "Yeah, I tripped."
    t "Ooooooohhhh..."
    l "The motorcycle fell on my leg, and..."
    "I pull up my pant leg and gesture for Taffy to duck down and look at it."
    "A huge scar goes up my shin where my fibula got cracked."
    t "That’s why it got delayed?!"
    l "Yeah."
    "I don’t really get embarrassed about my injuries or stunt work."
    "For me, it’s what makes acting fun."
    ## jump to after the sweets question

label salad_end1:
t "You come here often?"
l "Yeah, {i}too{/i} often. They give me free dessert all the time."
"Taffy sits upright in a snap with a slam of his hand onto the table. I jump with him. Did... Did I say something wrong?"
"His head turns to look at the kitchen door and back at me a few times before finally telling me what he wants to say."
t "...You think that’s a bad thing?"
l "U-Um..."

#timer GO
$ timer_dialogue = "I love sweets! Do they ever bring you chocolate cake?"
$ timer_dialogue = "What about chocolate mousse? Ugh, I’ve been on this diet and it’s just killing me!"
$ timer_dialogue = "I think I miss ice cream the most, but this place is fancy. I bet they have tiramisu."
$ timer_dialogue = "If they offer you some, I can have it if you don’t want it."
$ timer_dialogue = "...Please. I meant ‘Can I have it if you don’t want it? ...Pretty please?’"
