init python:
    def inventoryUpdate(st): # st = shown time

        if inventory_drag == True:

            for item in inventory_sprites:

                if item.type == item_dragged: ## identified the correct item that should be dragged on the screen

                    item.x = mousepos[0] - item.width / 2 ## make centerpoint same pos as mouse coordinates
                    item.y = mousepos[1] - item.height / 2
                    item.zorder = 99

            return 0 # as soon as this for loop finished, we run the function again to update everything.

        return None # if we stop dragging, we have to make sure we don't return to this function anymore

    def inventoryEvents(event, x, y, at): # event = event currently occuring, x & y = mouse pos, at = time since sprite manager was shown
        global mousepos, dnd_dialogue, inventory_drag, i_overlap, ie_overlap

        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP: ## check if the button got let go to stop dragging

            if event.button == 1: ## check if it's the left mouse button

                for item1 in inventory_sprites:

                    if item1.visible == True:

                        if item1.x <= x <= item1.x + item1.width and item1.y <= y <= item1.y + item1.height: ## check if the mouse is in the hitbox

                            inventory_drag = False
                            i_combine = False
                            ie_combine = False

                            for item2 in inventory_sprites:

                                items_overlap = checkItemsOverlap(item1, item2)

                                if items_overlap == True:

                                    i_overlap = True

                                    if (item1.type == "grocery_list" or item1.type == "mail") and (item2.type == "grocery_list" or item2.type == "mail"): ## this is the only type of item that can be combined in this, rinse and repeat for all combineable items

                                        i_combine = True

                                        if item1.type == "grocery_list":
                                            removeInventoryItem(item1)

                                        else:
                                            removeInventoryItem(item2)

                                        mail_image = Image("test_case/evidence inventory/inventory_mail_checked.png") ## "dnd_test_files/Inventory Items/inventory-lantern-lit.png"
                                        t = Transform(child = mail_image) ## might need to add ", zoom = 0.7", but we'll see

                                        inventory_sprites[inventory_items.index("mail")].set_child(t)
                                        inventory_sprites[inventory_items.index("mail")].item_image = mail_image
                                        inventory_sprites[inventory_items.index("mail")].state = "checked"
                                        renpy.show_screen("inspectItem", ["mail"])

                                        characterSay(who = "Levi", what = ["...Yeah, the handwriting on these match up.", "It's definitely Maddie's."], inspectItem = True)

                                        inventory_SM.redraw(0)
                                        renpy.restart_interaction()

                                        break

                                    else:

                                        item1.x = item1.original_x
                                        item1.y = item1.original_y
                                        item1.zorder = 0

                                        characterSay(who = "Levi", what = ["...No, that's not doing anything.", "Let's try something else."])

                                        break

                            if i_combine == False: ## 2 inventory items were not combined

                                for item3 in environment_sprites:

                                    items_overlap = checkItemsOverlap(item1, item3)

                                    if items_overlap == True:

                                        ie_overlap = True

                                        if item1.type == "key" and item3.type == "box":

                                            ie_combine = True
                                            removeInventoryItem(item1)
                                            removeEnvironmentItem(item3)
                                            addToInventory(["secateur", "matches"])
                                            renpy.show_screen("inspectItem", ["secateur", "matches"])
                                            characterSay(who = "Levi", what = ["This tool might come in handy.", "But for what?"], inspectItem = True)
                                            inventory_SM.redraw(0)
                                            environment_SM.redraw(0)
                                            renpy.restart_interaction()
                                            break

                                        elif item1.type == "secateur" and item3.type == "door-vines":

                                            ie_combine = True
                                            removeInventoryItem(item1)
                                            removeEnvironmentItem(item3)
                                            characterSay(who = "Levi", what = ["Looks like that freed up the door."])
                                            inventory_SM.redraw(0)
                                            environment_SM.redraw(0)
                                            renpy.restart_interaction()
                                            break

                                        else:

                                            item1.x = item1.original_x
                                            item1.y = item1.original_y
                                            item1.zorder = 0
                                            characterSay(who = "Levi", what = ["...No, that's not doing anything.", "Let's try something else."])
                                            break

                            if i_combine == False and ie_combine == False:

                                item1.x = item1.original_x
                                item1.y = item1.original_y
                                item1.zorder = 0

        if event.type == renpy.pygame_sdl2.MOUSEMOTION: ## if the event is a mouse movement

            mousepos = (x, y)

            if inventory_drag == False: ## make sure as long as we're not dragging an item on a screen, then we can show the item menu if the mouse happens to be over one of these items

                for item in inventory_sprites:

                    if item.visible == True:

                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height: ## check if the mouse is in the hitbox

                            renpy.show_screen("inventoryItemMenu", item = item)
                            renpy.restart_interaction()
                            break

                        else:
                            renpy.hide_screen("inventoryItemMenu")
                            renpy.restart_interaction()

    def environmentEvents(event, x, y, at): # see above, might wanna make a unique function for each investigation just because that's a LOT of items

        if event.type == renpy.pygame_sdl2.MOUSEMOTION: ## if the event is a mouse movement

            for item in environment_sprites:

                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height: ## check if the mouse is in the hitbox

                    t = Transform(child = item.hover_image)
                    item.set_child(t)
                    environment_SM.redraw(0) # ensures redraw only goes off once
                    renpy.restart_interaction()
                    break

                else:
                    t = Transform(child = item.idle_image)
                    item.set_child(t)
                    environment_SM.redraw(0)

        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP: ## if the event is a click, i'm assuming this is "up" to avoid accidentally skipping dialogue

            if event.button == 1: ## check if it's a left click

                for item in environment_sprites:

                    if i_overlap == False and ie_overlap == False: ## if there is an overlap currently happening, don't trigger these

                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height: ## check if the mouse is in the hitbox

                            if item.type == "grocery_list": ## checking the type of item to figure out what to do omg this is going to be a NIGHTMARE WITH A FULL GAME OF THESE
                                addToInventory(["grocery_list"])

                            elif item.type == "roses": ## checking the type of item to figure out what to do
                                addToInventory(["roses"])

                            elif item.type == "mail": ## if you try to call a say screen in a python function, it'll return an error according to the tut?
                                characterSay(who = "", what = ["...Maddie's having an affair with Jason Hughes and wants to confront him about it?", "She's so pissed she handwrote the letter, but I wonder if it's actually her handwriting."])
                                #renpy.call("box_label")
                                addToInventory(["mail"])
                                #characterSay(who = "Levi", what = ["It's locked. Wonder where the key is."]) ## wrapping in a list to make a distinction between ren'py say and our custom say that doesn't break the scene

                            elif item.type == "black_fabric":
                                #renpy.call("doorvines_label")
                                addToInventory(["black_fabric"])

                            elif item.type == "champagne":
                                #renpy.call("doorvines_label")
                                addToInventory(["champagne"])

                            elif item.type == "body":
                                #renpy.call("doorvines_label")
                                addToInventory(["body"])

                            elif item.type == "head":
                                characterSay(who = "", what = ["I check the mouth out of instinct.", "She's definitely a vampire. Right down to the black blood.", "Who got my target first?"])
                                #renpy.call("doorvines_label")
                                addToInventory(["head"])

                            elif item.type == "security_system":
                                #renpy.call("doorvines_label")
                                addToInventory(["security_system"])

                            elif item.type == "wedding_ring":
                                characterSay(who = "", what = ["Is it wrong to steal someone's wedding ring?", "...Not if it's a cheating whore."])
                                #renpy.call("doorvines_label")
                                addToInventory(["wedding_ring"])

                            elif item.type == "purse":
                                characterSay(who = "", what = ["...There's nothing in this purse?"])
                                #renpy.call("doorvines_label")
                                addToInventory(["purse"])

                            elif item.type == "broken_door":
                                characterSay(who = "", what = ["I try to open the door to the backyard, but there's no use. It's jammed.", "Still, good to know."])
                                #renpy.call("doorvines_label")
                                addToInventory(["broken_door"])

                            elif item.type == "bite":
                                characterSay(who = "", what = ["So a vampire killed him.", "I wonder if it was whoever killed the victim.", "It looks like he gets bitten a lot..."])
                                #renpy.call("doorvines_label")
                                addToInventory(["bite"])

                global i_overlap, ie_overlap
                i_overlap = False
                ie_overlap = False

    def startDrag(item):

        global inventory_drag, item_dragged
        inventory_drag = True
        item_dragged = item.type
        inventory_SM.redraw(0)

    def checkItemsOverlap(item1, item2): ## find the distance between these 2 items based on their centerpoints to see if they're overlapping

        if abs((item1.x + item1.width / 2) - (item2.x + item2.width / 2)) * 2 < (item1.width + item2.width) and abs((item1.y + item1.height / 2) - (item2.y + item2.height / 2)) * 2 < (item1.height + item2.height) and item1.type != item2.type:
            return True

        else:
            return False

    def characterSay(who, what, inspectItem = False): ## = false as a default if it's not specified when this function is called

        if isinstance(what, str): ## object and object type (string)

            renpy.call_screen("characterSay", who = who, what = what)

        elif isinstance(what, list):

            global dnd_dialogue
            dnd_dialogue = {"who" : who, "what" : what}

            if inspectItem == False:
                renpy.show_screen("characterSay")
                renpy.restart_interaction()

    def repositionInventoryItems():
        global inventory_lb_enabled, inventory_rb_enabled

        for i, item in enumerate(inventory_sprites):

            if i == 0: ## make sure first item is in the first slot

                item.x = inventory_first_slot_x
                item.original_x = item.x

            else: ## this is for any non-first iteration

                item.x = (inventory_first_slot_x + inventory_slot_size[0] * i) + (inventory_slot_padding * i)
                item.original_x = item.x

            if item.x < inventory_first_slot_x or item.x > (inventory_first_slot_x + (item.width * 7)) + (inventory_slot_padding * 5):
                setItemVisibility(item = item, visible = False)

            elif item != "":
                setItemVisibility(item = item, visible = True)

        if len(inventory_sprites) > 0:

            if inventory_sprites[-1].visible == True:
                inventory_rb_enabled = False

            else:
                inventory_rb_enabled = True

            if inventory_sprites[0].visible == True:
                inventory_lb_enabled = False

            else:
                inventory_lb_enabled = True

        renpy.retain_after_load()

    def addToInventory(items):

        for item in items:

            inventory_items.append(item)

            if item == "mail": ## since this item has 2 states as it appears in the inventory, it's listed as a special case

                item_image = Image("test_case/evidence inventory/inventory_mail_unchecked.png") ## should be unchecked as a default, will be checked if combined with grocery list

            else:

                item_image = Image("test_case/evidence inventory/inventory_{}.png".format(item))

            t = Transform(child = item_image)
            inventory_sprites.append(inventory_SM.create(t))
            inventory_sprites[-1].width = inventory_slot_size[0]
            inventory_sprites[-1].height = inventory_slot_size[1]
            inventory_sprites[-1].type = item
            inventory_sprites[-1].item_image = item_image
            inventory_sprites[-1].y = 916
            inventory_sprites[-1].original_y = 916 ## store original pos so if you don't combine it with the right thing it returns to its original spot
            inventory_sprites[-1].original_x = 0 ## store original pos so if you don't combine it with the right thing it returns to its original spot
            inventory_sprites[-1].visible = True ## for when the inventory is more than 7 items

            if item == "mail": ## this is pretty much just the thing we do with combined items in this house, so copy paste as needed per object

                inventory_sprites[-1].state = "unchecked"

            else:

                inventory_sprites[-1].state = "default"

            for envitem in environment_sprites:

                if envitem.type == item:

                    removeEnvironmentItem(item = envitem)
                    break

            repositionInventoryItems()

            inventory_SM.redraw(0)
            environment_SM.redraw(0)
            renpy.restart_interaction() ## interaction is still ongoing, but we wanna make changes and make sure they're actually reflected on the screen

    def removeEnvironmentItem(item):

        item.destroy()
        environment_items_deleted.append(item.type)
        environment_sprites.pop(environment_sprites.index(item))
        environment_items.pop(environment_items.index(item.type))

    def removeInventoryItem(item):

        item.destroy()
        inventory_sprites.pop(inventory_sprites.index(item))
        inventory_items.pop(inventory_items.index(item.type))
        repositionInventoryItems()

    def inventoryArrows(button):
        global inventory_lb_enabled, inventory_rb_enabled

        if len(inventory_sprites) > 7:

            citem = "" ## citem = current item

            for i, item in enumerate(inventory_sprites):

                if button == "right" and inventory_rb_enabled == True:

                    if inventory_sprites[-1].visible == False:
                        item.x -= item.width + inventory_slot_padding
                        citem = item

                elif button == "left" and inventory_lb_enabled == True:

                    if inventory_sprites[0].visible == False:

                        reversed_index = (len(inventory_sprites) - 1) - i
                        inventory_sprites[reversed_index].x += item.width + inventory_slot_padding
                        citem = inventory_sprites[reversed_index]

                if citem != "" and (citem.x < inventory_first_slot_x or citem.x > (inventory_first_slot_x + (citem.width * 7)) + (inventory_slot_padding * 5)):
                    setItemVisibility(item = citem, visible = False)

                elif citem != "":
                    setItemVisibility(item = citem, visible = True)

            if inventory_sprites[-1].visible == True:
                inventory_rb_enabled = False

            else:
                inventory_rb_enabled = True

            if inventory_sprites[0].visible == True:
                inventory_lb_enabled = False

            else:
                inventory_lb_enabled = True

            if citem != "":
                inventory_SM.redraw(0)
                renpy.restart_interaction()

    def setItemVisibility(item, visible):

        if visible == False:
            item.visible = False
            t = Transform(child = item.item_image, alpha = 0) ## might have to add zoom = 0.7
            item.set_child(t)

        else:
            item.visible = True
            t = Transform(child = item.item_image, alpha = 100) ## might have to add zoom = 0.7
            item.set_child(t)

        inventory_SM.redraw(0)

    def prepareLoad():
        global dnd_dialogue, inventory_drag

        for item in inventory_sprites:

            if item_dragged == item.type:
                item.x = item.original_x
                item.y = item.original_y
                item.zorder = 0

        dnd_dialogue = {}
        inventory_drag = False
        renpy.hide_screen("characterSay")

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

screen inventoryItemMenu(item):
    zorder 7
    frame:
        xysize (inventory_slot_size[0], inventory_slot_size[1])
        background "#ffffff30"
        xpos item.x
        ypos item.y ## was feeling p lazy when it came to resizing at this point, feel free to remove all "at two_third_size" and the transform for "two_third_size" when constructing. you're smart and sexy, you'll make everything the right size
        imagebutton auto "dnd_test_files/UI/view-inventory-item-%s.png" at two_third_size align (0.0, 0.5) action [Show("inspectItem", items = [item.type]), Hide("inventoryItemMenu")]
        imagebutton auto "dnd_test_files/UI/use-inventory-item-%s.png" at two_third_size align (1.0, 0.5) action [Function(startDrag, item = item), Hide("inventoryItemMenu")]
        ## might wanna do this differently by making this a collapsible list of options or a couple of text buttons that say "View" and "Use" that are stacked on top of each other

## item fill variables
default evidence_button_text_mail = "???"
default evidence_button_text_roses = "???"
default evidence_button_text_grocery_list = "???"
default evidence_button_text_black_fabric = "???"
default evidence_button_text_champagne = "???"
default evidence_button_text_body = "???"
default evidence_button_text_head = "Who did it?"
default evidence_button_text_broken_door = "???"
default evidence_button_text_footprints = "???"
default evidence_button_text_security_system = "???"
default evidence_button_text_wedding_ring = "???"
default evidence_button_text_purse = "???"
default evidence_button_text_bite = "???"

default current_item = ""

screen inspectItem(items):
    modal True
    zorder 4
    button:
        xfill True
        yfill True
        action If(len(items) > 1, true=RemoveFromSet(items, items[0]), false=[Hide("inspectItem"), If(len(dnd_dialogue) > 0, true=Show("characterSay"), false=NullAction())])
        image "dnd_test_files/Items Pop Up/items-pop-up-bg.png" align (0.5, 0.5)
        if "mail" in inventory_items:
            $ mail_state = inventory_sprites[inventory_items.index("mail")].state

        python:
            item_name = ""
            item_desc = ""
            #item_state = ""
            for name in inventory_item_names:
                temp_name = name.replace(" ", "_")
                if temp_name.lower() == items[0]:
                    item_name = name
            for desc in inventory_item_desc:
                if inventory_item_desc.index(desc) == inventory_item_names.index(item_name):
                    item_desc = desc
                elif item_name == "Mail" and mail_state == "checked":
                    item_desc = "Confirmed to be \nMaddie's handwriting."
            ## get the description from a list
            ## check if the index of the item and the index of the description matches, and if it does you have your description

        if items[0] == "mail":
            image "test_case/evidence popup/{}_{}_popup.png".format("mail", mail_state) at half_size align (0.4, 0.5)
        else:
            image "test_case/evidence popup/{}_popup.png".format(items[0]) at half_size align (0.4, 0.5)

        text "{}".format(item_name) size 30 align (0.5, 0.28) color "#000000"
        text "{}".format(item_desc) size 25 align (0.6, 0.4) ## show the description to the right of the image below

        ## add a button that opens a specific choice menu that lets you figure out what makes this evidence matter
        if item_name == "Roses":
            textbutton evidence_button_text_roses:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Mail":
            textbutton evidence_button_text_mail:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Grocery List":
            textbutton evidence_button_text_grocery_list:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Black Fabric":
            textbutton evidence_button_text_black_fabric:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Champagne":
            textbutton evidence_button_text_champagne:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Body":
            textbutton evidence_button_text_body:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Head":
            textbutton evidence_button_text_head:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Broken Door":
            textbutton evidence_button_text_broken_door:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Footprints":
            textbutton evidence_button_text_footprints:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Security System":
            textbutton evidence_button_text_security_system:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Wedding Ring":
            textbutton evidence_button_text_wedding_ring:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Purse":
            textbutton evidence_button_text_purse:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]
        elif item_name == "Bite":
            textbutton evidence_button_text_bite:
                yalign 0.7
                xalign 0.5
                action [SetVariable("current_item", item_name), Hide("inspectItem"), Jump("evidence_fill_1")]

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

    $ environment_items = ["roses", "mail", "grocery_list", "champagne"]
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

                if item == "roses": ## list of properties for each object
                    environment_sprites[-1].width = 148 # make sure each image has its actual width and height
                    environment_sprites[-1].height = 167
                    environment_sprites[-1].x = 795 # positioning of each object in the scene
                    environment_sprites[-1].y = 400

                elif item == "grocery_list":
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

    if seen_body == False:
        $ seen_body = True
        "Ah, damn."
        "It looks like there were footprints going to this place."
        "Could've been helpful if I didn't step all over them. Whoops."

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

label evidence_fill_1:
    menu:
        "Was taken from by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was taken from by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was taken from by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was taken from by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was taken from by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was taken from by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was taken from by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was taken from by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was taken from by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was taken from by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was taken from by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was taken from by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was taken from by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was taken from by "

            jump evidence_fill_person

        "Was written by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was written by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was written by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was written by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was written by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was written by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was written by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was written by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was written by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was written by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was written by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was written by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was written by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was written by "

            jump evidence_fill_person

        "Was worn by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was worn by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was worn by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was worn by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was worn by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was worn by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was worn by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was worn by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was worn by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was worn by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was worn by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was worn by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was worn by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was worn by "

            jump evidence_fill_person

        "Was planted by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was planted by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was planted by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was planted by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was planted by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was planted by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was planted by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was planted by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was planted by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was planted by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was planted by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was planted by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was planted by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was planted by "

            jump evidence_fill_person

        "Was left by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was left by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was left by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was left by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was left by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was left by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was left by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was left by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was left by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was left by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was left by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was left by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was left by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was left by "

            jump evidence_fill_person

        "Belongs to":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Belongs to "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Belongs to "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Belongs to "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Belongs to "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Belongs to "
            elif current_item == "Body":
                $ evidence_button_text_body = "Belongs to "
            elif current_item == "Head":
                $ evidence_button_text_head = "Belongs to "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Belongs to "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Belongs to "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Belongs to "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Belongs to "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Belongs to "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Belongs to "

            jump evidence_fill_person

        "Was hidden by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was hidden by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was hidden by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was hidden by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was hidden by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was hidden by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was hidden by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was hidden by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was hidden by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was hidden by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was hidden by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was hidden by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was hidden by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was hidden by "

            jump evidence_fill_person

        "Was broken by":
            if current_item == "Roses":
                $ evidence_button_text_roses = "Was broken by "
            elif current_item == "Mail":
                $ evidence_button_text_mail = "Was broken by "
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list = "Was broken by "
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric = "Was broken by "
            elif current_item == "Champagne":
                $ evidence_button_text_champagne = "Was broken by "
            elif current_item == "Body":
                $ evidence_button_text_body = "Was broken by "
            elif current_item == "Head":
                $ evidence_button_text_head = "Was broken by "
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door = "Was broken by "
            elif current_item == "Footprints":
                $ evidence_button_text_footprints = "Was broken by "
            elif current_item == "Security System":
                $ evidence_button_text_security_system = "Was broken by "
            elif current_item == "Purse":
                $ evidence_button_text_purse = "Was broken by "
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring = "Was broken by "
            elif current_item == "Bite":
                $ evidence_button_text_bite = "Was broken by "

            jump evidence_fill_person

            ## used by??
            ## remove "written" and "worn"

label evidence_fill_person:
    menu:
        "Deja":
            if current_item == "Roses":
                $ evidence_button_text_roses += "Deja"
            elif current_item == "Mail":
                $ evidence_button_text_mail += "Deja"
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list += "Deja"
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric += "Deja"
            elif current_item == "Champagne":
                $ evidence_button_text_champagne += "Deja"
            elif current_item == "Body":
                $ evidence_button_text_body += "Deja"
            elif current_item == "Head":
                $ evidence_button_text_head += "Deja"
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door += "Deja"
            elif current_item == "Footprints":
                $ evidence_button_text_footprints += "Deja"
            elif current_item == "Security System":
                $ evidence_button_text_security_system += "Deja"
            elif current_item == "Purse":
                $ evidence_button_text_purse += "Deja"
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring += "Deja"
            elif current_item == "Bite":
                $ evidence_button_text_bite += "Deja"

            jump conclusion_grading

        "Maddie":
            if current_item == "Roses":
                $ evidence_button_text_roses += "Maddie"
            elif current_item == "Mail":
                $ evidence_button_text_mail += "Maddie"
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list += "Maddie"
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric += "Maddie"
            elif current_item == "Champagne":
                $ evidence_button_text_champagne += "Maddie"
            elif current_item == "Body":
                $ evidence_button_text_body += "Maddie"
            elif current_item == "Head":
                $ evidence_button_text_head += "Maddie"
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door += "Maddie"
            elif current_item == "Footprints":
                $ evidence_button_text_footprints += "Maddie"
            elif current_item == "Security System":
                $ evidence_button_text_security_system += "Maddie"
            elif current_item == "Purse":
                $ evidence_button_text_purse += "Maddie"
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring += "Maddie"
            elif current_item == "Bite":
                $ evidence_button_text_bite += "Maddie"

            jump conclusion_grading

        "Taffy":
            if current_item == "Roses":
                $ evidence_button_text_roses += "Taffy"
            elif current_item == "Mail":
                $ evidence_button_text_mail += "Taffy"
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list += "Taffy"
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric += "Taffy"
            elif current_item == "Champagne":
                $ evidence_button_text_champagne += "Taffy"
            elif current_item == "Body":
                $ evidence_button_text_body += "Taffy"
            elif current_item == "Head":
                $ evidence_button_text_head += "Taffy"
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door += "Taffy"
            elif current_item == "Footprints":
                $ evidence_button_text_footprints += "Taffy"
            elif current_item == "Security System":
                $ evidence_button_text_security_system += "Taffy"
            elif current_item == "Purse":
                $ evidence_button_text_purse += "Taffy"
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring += "Taffy"
            elif current_item == "Bite":
                $ evidence_button_text_bite += "Taffy"

            jump conclusion_grading

        "Samantha" if know_samantha == True:
            if current_item == "Roses":
                $ evidence_button_text_roses += "Samantha"
            elif current_item == "Mail":
                $ evidence_button_text_mail += "Samantha"
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list += "Samantha"
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric += "Samantha"
            elif current_item == "Champagne":
                $ evidence_button_text_champagne += "Samantha"
            elif current_item == "Body":
                $ evidence_button_text_body += "Samantha"
            elif current_item == "Head":
                $ evidence_button_text_head += "Samantha"
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door += "Samantha"
            elif current_item == "Footprints":
                $ evidence_button_text_footprints += "Samantha"
            elif current_item == "Security System":
                $ evidence_button_text_security_system += "Samantha"
            elif current_item == "Purse":
                $ evidence_button_text_purse += "Samantha"
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring += "Samantha"
            elif current_item == "Bite":
                $ evidence_button_text_bite += "Samantha"

            jump conclusion_grading

        "Jason":
            if current_item == "Roses":
                $ evidence_button_text_roses += "Jason"
            elif current_item == "Mail":
                $ evidence_button_text_mail += "Jason"
            elif current_item == "Grocery List":
                $ evidence_button_text_grocery_list += "Jason"
            elif current_item == "Black Fabric":
                $ evidence_button_text_black_fabric += "Jason"
            elif current_item == "Champagne":
                $ evidence_button_text_champagne += "Jason"
            elif current_item == "Body":
                $ evidence_button_text_body += "Jason"
            elif current_item == "Head":
                $ evidence_button_text_head += "Jason"
            elif current_item == "Broken Door":
                $ evidence_button_text_broken_door += "Jason"
            elif current_item == "Footprints":
                $ evidence_button_text_footprints += "Jason"
            elif current_item == "Security System":
                $ evidence_button_text_security_system += "Jason"
            elif current_item == "Purse":
                $ evidence_button_text_purse += "Jason"
            elif current_item == "Wedding Ring":
                $ evidence_button_text_wedding_ring += "Jason"
            elif current_item == "Bite":
                $ evidence_button_text_bite += "Jason"

            jump conclusion_grading

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
