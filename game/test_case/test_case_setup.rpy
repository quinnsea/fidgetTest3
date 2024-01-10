screen dnd_ui:
    zorder 1
    image "dnd_test_files/UI/inventory-icon-bg.png" xpos 0.0 ypos 0.8
    imagebutton auto "dnd_test_files/UI/inventory-icon-%s.png" action If(renpy.get_screen("inventory") == None, true=Show("inventory"), false=Hide("inventory")) xpos 0.03 ypos 0.835

screen inventory:
    image "dnd_test_files/UI/inventory-bg.png" xpos 0.17 ypos 0.81
    image "dnd_test_files/UI/inventory-slots.png" xpos 0.25 ypos 0.85

    imagebutton idle If(inventory_rb_enabled == True,
    true="dnd_test_files/UI/inventory-arrow-right-enabled-idle.png",
    false="dnd_test_files/UI/inventory-arrow-right-disabled.png") hover If(inventory_rb_enabled == True,
    true="dnd_test_files/UI/inventory-arrow-right-enabled-hover.png",
    false="dnd_test_files/UI/inventory-arrow-right-disabled.png") action Function(inventoryArrows, button = "right") xpos 0.91 ypos 0.872

    imagebutton idle If(inventory_lb_enabled == True,
    true="dnd_test_files/UI/inventory-arrow-left-enabled-idle.png",
    false="dnd_test_files/UI/inventory-arrow-left-disabled.png") hover If(inventory_lb_enabled == True,
    true="dnd_test_files/UI/inventory-arrow-left-enabled-hover.png",
    false="dnd_test_files/UI/inventory-arrow-left-disabled.png") action Function(inventoryArrows, button = "left") xpos 0.192 ypos 0.872

    add inventory_SM

default dict_item_search = ""

screen inventoryItemMenu(item):
    zorder 7
    frame:
        xysize (inventory_slot_size[0], inventory_slot_size[1])
        background "#ffffff30"
        xpos item.x
        ypos item.y ## was feeling p lazy when it came to resizing at this point, feel free to remove all "at two_third_size" and the transform for "two_third_size" when constructing. you're smart and sexy, you'll make everything the right size

        $ dict_item_search = item.type.replace(" ", "_")

        python:
            print(dict_item_search)

        imagebutton auto "dnd_test_files/UI/view-inventory-item-%s.png" at two_third_size align (0.0, 0.5) action [SetVariable("inspect_dict", dict_list[inventory_item_names.index(dict_item_search)]), Show("inspectItem", items = [item.type]), Hide("inventoryItemMenu")]
        imagebutton auto "dnd_test_files/UI/use-inventory-item-%s.png" at two_third_size align (1.0, 0.5) action [Function(startDrag, item = item), Hide("inventoryItemMenu")]
        ## might wanna do this differently by making this a collapsible list of options or a couple of text buttons that say "View" and "Use" that are stacked on top of each other

default inspect_dict = {
    "current_item": "",
    "action": "",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": ""
}

default dict_list = []

default current_item = ""

default suspect_bio = {
    "current_item": "",
    "action": "",
    "culprit_image": "",
    "culprit_name": "",
    "desc": "",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": ""
}

default evidence_options_list_a = ["Was taken by", "Was used by", "Was planted by", "Was broken by", "Was hidden by", "Was on", "Was dropped by", "Belongs to"]
default evidence_options_list_b = ["Deja", "Taffy", "Maddie"] ## update this list when discovering new people
default suspect_list_padding = 50
default dropdown_visible = False

default chosen_culprit_image = "gui/profiles/default_icon.png"
default is_inspecting = ""

screen suspect_list():
    modal True
    zorder 10

    $ is_inspecting = renpy.get_screen("inspectItem")

    button:
        # everything outside the frame is a transparent button to hide the screen
        background None
        action Hide("suspect_list")

    frame:
        ysize 400
        xsize 700
        align (0.5, 0.5)

        hbox:
            spacing 50
            xpos 50

            for suspect in evidence_options_list_b:

                if evidence_options_list_b.index(suspect) <= 2: ## needs a way to accommodate for multiple lines of suspects/people of interest, should probably compare to a list of possible suspects and fill with default profiles

                    button:
                        image "gui/profiles/{}_icon.png".format(suspect)
                        ypos 50
                        action If((is_inspecting != None), true=[SetDict(inspect_dict, "culprit_name", suspect),
                        SetDict(inspect_dict, "culprit_image", "gui/profiles/{}_icon.png".format(suspect)),
                        SetDict(inspect_dict, "deduction", inspect_dict["action"] + " " + inspect_dict["culprit_name"]),
                        SetVariable("{}_dict".format(current_item), inspect_dict),
                        Hide("suspect_list")], false=Show("suspect_info", suspect = suspect))

        hbox:
            spacing 125
            xpos 90

            for suspect in evidence_options_list_b:

                textbutton suspect:
                    ypos 225
                    action If((is_inspecting != None), true=[SetDict(inspect_dict, "culprit_name", suspect),
                    SetDict(inspect_dict, "culprit_image", "gui/profiles/{}_icon.png".format(suspect)),
                    SetDict(inspect_dict, "deduction", inspect_dict["action"] + " " + inspect_dict["culprit_name"]),
                    SetVariable("{}_dict".format(current_item), inspect_dict),
                    Hide("suspect_list")], false=Show("suspect_info", suspect = suspect))

screen suspect_info(suspect):
    modal True
    zorder 11

    button:
        # everything outside the frame is a transparent button to hide the screen
        background None
        action Hide("suspect_info")

    for dict in dict_list:
        if dict["current_item"] == suspect:
            $ suspect_bio = dict

    frame:
        ysize 400
        xsize 700
        align (0.5, 0.5)

        vbox:
            xpos 50
            yalign 0.4

            image suspect_bio["culprit_image"]
            text suspect ypos 25 xpos 25

        hbox:
            xsize 450
            xpos 225
            ypos 75

            text suspect_bio["desc"]

## descs could also open up the door for the "remember" mechanic, and if you store the right piece of dialogue you might have extra dialogue to use against someone else
screen dropdown_menu():
    modal True
    zorder 5
    $ current_item = inspect_dict.get("current_item") ## get the item that's currently being inspected
    $ current_item = current_item.replace(" ", "_").lower() ## change the format to be code compliant

    button:
        # everything outside the frame is a transparent button to hide the screen
        background None
        action Hide("dropdown_menu")

    frame:
        align (0.6, 0.65)
        ysize 200
        xsize 350

        viewport id "vp":
            mousewheel True
            draggable True

            vbox:
                spacing 2

                for option in evidence_options_list_a:
                    textbutton option:
                        xpos 20
                        action [SetDict(inspect_dict, "action", option), ##set the inspect dictionary's action to the option
                        SetVariable("{}_dict".format(current_item), inspect_dict), ##copy the inspect dictionary back onto the original item's dictionary
                        Hide("dropdown_menu")] ##hide the dropdown

        vbar value YScrollValue("vp")

screen redHerring(item):
    modal True
    zorder 6

    #frame:

screen inspectItem(items):
    modal True
    zorder 4
    button:
        xfill True
        yfill True
        action [If(len(items) > 1, true=RemoveFromSet(items, items[0]), false=[Hide("inspectItem"), If(len(dnd_dialogue) > 0, true=Show("characterSay"), false=NullAction())]), Hide("dropdown_menu")]
        image "dnd_test_files/Items Pop Up/items-pop-up-bg.png" align (0.5, 0.5)
        if "mail" in inventory_items:
            $ mail_state = inventory_sprites[inventory_items.index("mail")].state

        python:
            item_name = ""
            item_desc = ""
            #item_state = ""
            for name in inventory_item_names: ## gets the name of the item from the inventory_item_names list
                temp_name = name.replace(" ", "_")
                if temp_name.lower() == items[0]:
                    item_name = name
            for desc in inventory_item_desc:
                if inventory_item_desc.index(desc) == inventory_item_names.index(item_name):
                    item_desc = desc
                elif item_name == "Mail" and mail_state == "checked":
                    item_desc = "Confirmed to be Maddie's handwriting."
            ## get the description from a list
            ## check if the index of the item and the index of the description matches, and if it does you have your description

        if items[0] == "mail":
            image "test_case/evidence popup/{}_{}_popup.png".format("mail", mail_state) at half_size align (0.4, 0.5)
        else:
            image "test_case/evidence popup/{}_popup.png".format(items[0]) at half_size align (0.4, 0.5)

        text "{}".format(inspect_dict["current_item"]) size 30 align (0.5, 0.28) color "#000000"
        text "{}".format(inspect_dict["desc"]) size 25 align (0.6, 0.4) xsize 300 ## show the description to the right of the image below

        button:
            align (0.6, 0.56)
            action [SetVariable("current_item", item_name), Show("dropdown_menu")]
            frame:
                text "▼ " + inspect_dict["action"]

        textbutton inspect_dict["culprit_name"]:
            align (0.6, 0.7)
            action Show("suspect_list")

screen characterSay(who = None, what = None): ## default values
    modal True ## prevent interactions from happening underneath dialogue as it's showing
    zorder 6
    style_prefix "say"

    window:
        id "window"
        window:
            padding (20, 20)

            if who is not None:
                text who id "who"
            else:
                id "namebox"
                style "namebox"
                text dnd_dialogue["who"]

        if what is not None:
            text what id "what" xpos 0.25 ypos 0.4 xanchor 0.0
        else:
            text dnd_dialogue["what"][0] xpos 0.25 ypos 0.4 xanchor 0.0

    button:
        xfill True
        yfill True

        if what is None:
            action If(len(dnd_dialogue["what"]) > 1, true=RemoveFromSet(dnd_dialogue["what"], dnd_dialogue["what"][0]), false=[Hide("characterSay"), SetVariable("dnd_dialogue", {})])
        else:
            action Return(True)


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen maddies_house_scene:
    add environment_SM
    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.3, 0.3)
        action [Hide("inventory"), Jump("setup_scene_maddies_backyard")]
        text "Go to the backyard" color "#000000" size 18

    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.9, 0.8)
        action [Hide("inventory"), Jump("setup_scene_jasons_house")]
        text "Go next door" color "#000000" size 18

    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.8, 0.8)
        action Show("suspect_list")
        text "Open suspects list" color "#000000" size 18

    imagebutton:
        auto "images/sprites/maddie_invest_%s.png" at half_size
        align(0.6, 0.8)
        action [Hide("inventory"), Jump("maddie_intro")]

    imagebutton:
        auto "images/sprites/taffy_invest_%s.png" at half_size
        align(0.3, 0.6)
        action [Hide("inventory"), Jump("taffy_intro")]

screen maddies_backyard_scene:
    add environment_SM
    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.3, 0.3)
        action [Hide("inventory"), Jump("setup_scene_maddies_house")]
        text "Go back inside" color "#000000" size 18

    imagebutton:
        auto "images/sprites/deja_invest_%s.png"
        align(0.9, 0.8)
        action [Hide("inventory"), Jump("deja_intro")]

screen jasons_corpse_scene:
    add environment_SM
    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.3, 0.3)
        action [Hide("inventory"), Jump("setup_scene_jasons_house")]
        text "Go back" color "#000000" size 18

screen jasons_house_scene:
    add environment_SM
    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.5, 0.25)
        action [Hide("inventory"), Jump("setup_scene_jasons_corpse")]
        text "Go upstairs" color "#000000" size 18

    button:
        background "#FFFFFF"
        padding(25, 10)
        align(0.8, 0.5)
        action [Hide("inventory"), Jump("setup_scene_maddies_house")]
        text "Go back to Maddie's" color "#000000" size 18

## sprite transform
transform two_third_size:
    zoom 0.7

transform half_size:
    zoom 0.5

# point and click setup
label setup_scene_maddies_house:

    $ environment_items = ["mail", "grocery_list", "champagne"]
    $ current_scene = "maddies_house_scene"

    python:
        ## delete any potential items from other scenes carrying over
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        ## reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes
        i_overlap = False
        ie_overlap = False

    python:
        for item in environment_items: # getting all the item info into an array FUCK arrays just DON'T touch this unless you absolutely have to
            if item not in environment_items_deleted:
                idle_image = Image("test_case/house evidence env/{}_idle.png".format(item))
                hover_image = Image("test_case/house evidence env/{}_hover.png".format(item))
                t = Transform(child = idle_image)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item # -1 is the index for the last item in a list
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

                if item == "grocery_list":
                    environment_sprites[-1].width = 71
                    environment_sprites[-1].height = 76
                    environment_sprites[-1].x = 1710
                    environment_sprites[-1].y = 410

                elif item == "mail":
                    environment_sprites[-1].width = 117
                    environment_sprites[-1].height = 65
                    environment_sprites[-1].x = 10
                    environment_sprites[-1].y = 525

                elif item == "champagne":
                    environment_sprites[-1].width = 179
                    environment_sprites[-1].height = 56
                    environment_sprites[-1].x = 55
                    environment_sprites[-1].y = 700

                renpy.retain_after_load()

    scene maddies_house

    call screen maddies_house_scene

label setup_scene_maddies_backyard:

    $ environment_items = ["black_fabric"]
    $ current_scene = "maddies_backyard_scene"

    python:
        ## delete any potential items from other scenes carrying over
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        ## reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes
        i_overlap = False
        ie_overlap = False

    python:
        for item in environment_items: # getting all the item info into an array FUCK arrays just DON'T touch this unless you absolutely have to
            if item not in environment_items_deleted:
                idle_image = Image("test_case/backyard evidence env/{}_idle.png".format(item))
                hover_image = Image("test_case/backyard evidence env/{}_hover.png".format(item))
                t = Transform(child = idle_image)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item # -1 is the index for the last item in a list
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

                if item == "black_fabric": ## list of properties for each object
                    environment_sprites[-1].width = 253 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 141
                    environment_sprites[-1].x = 795 # positioning of each object in the scene
                    environment_sprites[-1].y = 200

                renpy.retain_after_load()

    scene maddies_backyard

    call screen maddies_backyard_scene

label setup_scene_jasons_house:

    $ environment_items = ["body", "head", "broken_door", "security_system", "purse"]
    $ current_scene = "jasons_house_scene"

    python:
        ## delete any potential items from other scenes carrying over
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        ## reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes
        i_overlap = False
        ie_overlap = False

        if "footprints" not in inventory_items:
            characterSay(who = "", what = ["Ah, damn.", "It looks like there were footprints going to this place.", "Could've been helpful if I didn't step all over them. Whoops."])
            addToInventory(["footprints"])

    python:
        for item in environment_items: # getting all the item info into an array FUCK arrays just DON'T touch this unless you absolutely have to
            if item not in environment_items_deleted:
                idle_image = Image("test_case/j house evidence env/{}_idle.png".format(item))
                hover_image = Image("test_case/j house evidence env/{}_hover.png".format(item))
                t = Transform(child = idle_image)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item # -1 is the index for the last item in a list
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

                if item == "body": ## list of properties for each object
                    environment_sprites[-1].width = 701 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 261
                    environment_sprites[-1].x = 1095 # positioning of each object in the scene
                    environment_sprites[-1].y = 800

                elif item == "broken_door": ## list of properties for each object
                    environment_sprites[-1].width = 148 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 224
                    environment_sprites[-1].x = 595 # positioning of each object in the scene
                    environment_sprites[-1].y = 450

                elif item == "head": ## list of properties for each object
                    environment_sprites[-1].width = 156 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 99
                    environment_sprites[-1].x = 1255 # positioning of each object in the scene
                    environment_sprites[-1].y = 650

                elif item == "security_system": ## list of properties for each object
                    environment_sprites[-1].width = 127 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 99
                    environment_sprites[-1].x = 1300 # positioning of each object in the scene
                    environment_sprites[-1].y = 450

                elif item == "purse": ## list of properties for each object
                    environment_sprites[-1].width = 227 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 121
                    environment_sprites[-1].x = 825 # positioning of each object in the scene
                    environment_sprites[-1].y = 700

                renpy.retain_after_load()

    scene jasons_house

    call screen jasons_house_scene

label setup_scene_jasons_corpse:

    $ environment_items = ["bite", "wedding_ring"]
    $ current_scene = "jasons_corpse"

    python:
        ## delete any potential items from other scenes carrying over
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        ## reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes
        i_overlap = False
        ie_overlap = False

    python:
        for item in environment_items: # getting all the item info into an array FUCK arrays just DON'T touch this unless you absolutely have to
            if item not in environment_items_deleted:
                idle_image = Image("test_case/corpse evidence env/{}_idle.png".format(item))
                hover_image = Image("test_case/corpse evidence env/{}_hover.png".format(item))
                t = Transform(child = idle_image)
                environment_sprites.append(environment_SM.create(t))
                environment_sprites[-1].type = item # -1 is the index for the last item in a list
                environment_sprites[-1].idle_image = idle_image
                environment_sprites[-1].hover_image = hover_image

                if item == "bite": ## list of properties for each object
                    environment_sprites[-1].width = 87 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 80
                    environment_sprites[-1].x = 295 # positioning of each object in the scene
                    environment_sprites[-1].y = 300

                if item == "wedding_ring": ## list of properties for each object
                    environment_sprites[-1].width = 67 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 74
                    environment_sprites[-1].x = 645 # positioning of each object in the scene
                    environment_sprites[-1].y = 825

                renpy.retain_after_load()

    scene jasons_corpse

    call screen jasons_corpse_scene

label conclusion_grading:
    if (evidence_button_text_mail == "Was written by Taffy" or evidence_button_text_mail == "Was planted by Taffy") and evidence_button_text_purse == "Was taken from by Taffy" and evidence_button_text_bite == "Was left by Samantha" and evidence_button_text_head == "Was left by Taffy": ## and conclusions list has taffy
        "So, let's get this story straight."
        "Taffy forged a letter in Maddie's handwriting that made it look like she's going to confront Jason about their affair."
        "He did that to frame {i}her{/i} for the murder, because he already planned on killing that woman."
        "He got Deja to pop the champagne so Maddie had an excuse to change."
        "That way, he could plant the fabric that looks like Deja's dress."
        "And Taffy knew the victim. It's why he took her phone."
        "They talked before he came in and he didn't want anyone to know."
        menu:
            "Is this really how it happened?"
            "Yes":
                "Yeah... Taffy did it."
                "I don't know why he did it, but I believe this story makes sense."
                return

            "No":
                "Nah... That... doesn't make any sense."
                "How would Taffy be able to forge that letter that perfectly?"
                "And that doesn't explain how Taffy knew about the affair."
                "Unless..."
                $ evidence_button_text_mail = "???"
                $ evidence_button_text_head = "Who did it?"

                jump end_grading

    ## deja: champagne "Was left by Deja" black fabric "Was planted by Deja" footprints "Was hidden by Deja"
    elif (evidence_button_text_black_fabric == "Was planted by Deja" or evidence_button_text_black_fabric == "Was left by Deja") and (evidence_button_footprints == "Was hidden by Deja" or evidence_button_footprints == "Belongs to Deja") and evidence_button_text_head == "Was left by Deja":
        "So, let's get this story straight."
        "Deja knew Maddie lived next door to Jason and got to the party early on purpose."
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
                return

            "No":
                "No, if Deja is that strong, she wouldn't be sending me after these vampires in the first place."
                "And she might be obsessed with money, but there's no way she'd {i}kill{/i} someone over it, right?"
                "...That's... what she has me for..."
                "...Right?"
                $ evidence_button_text_black_fabric = "???"
                $ evidence_button_text_head = "Who did it?"

                jump end_grading

    elif (evidence_button_text_mail == "Was written by Maddie" or evidence_button_text_mail == "Was left by Maddie") and evidence_button_text_broken_door == "Was broken by Maddie" and evidence_button_text_black_fabric == "Was worn by Maddie" and evidence_button_text_head == "Was left by Maddie" and seen_maddie_shoes == True:
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
                return

            "No":
                "No, that's... That's just ridiculous."
                "Maddie never mixes sex with work."
                "She's too... professional to do something like that."
                "...Right?"
                $ evidence_button_text_black_fabric = "???"
                $ evidence_button_text_head = "Who did it?"
                jump end_grading

    else:
        jump end_grading

label end_grading:
    python:
        renpy.retain_after_load()
    if current_scene == "maddies_backyard_scene":
        call screen maddies_backyard_scene
    elif current_scene == "jasons_house_scene":
        call screen jasons_house_scene
    elif current_scene == "jasons_corpse_scene":
        call screen jasons_corpse_scene
    else:
        call screen maddies_house_scene
