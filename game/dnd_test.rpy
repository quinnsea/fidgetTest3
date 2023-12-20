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

                                    if (item1.type == "matches" or item1.type == "lantern") and (item2.type == "matches" or item2.type == "lantern"): ## this is the only type of item that can be combined in this, rinse and repeat for all combineable items

                                        i_combine = True

                                        if item1.type == "matches":
                                            removeInventoryItem(item1)

                                        else:
                                            removeInventoryItem(item2)

                                        lantern_image = Image("dnd_test_files/Inventory Items/inventory-lantern-lit.png")
                                        t = Transform(child = lantern_image) ## might need to add ", zoom = 0.7", but we'll see

                                        inventory_sprites[inventory_items.index("lantern")].set_child(t)
                                        inventory_sprites[inventory_items.index("lantern")].item_image = lantern_image
                                        inventory_sprites[inventory_items.index("lantern")].state = "lit"
                                        renpy.show_screen("inspectItem", ["lantern"])

                                        characterSay(who = "Levi", what = ["Looks like that did the trick. The lantern is lit."], inspectItem = True)

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

                else:
                    t = Transform(child = item.idle_image)
                    item.set_child(t)
                    environment_SM.redraw(0)

        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP: ## if the event is a click, i'm assuming this is "up" to avoid accidentally skipping dialogue

            if event.button == 1: ## check if it's a left click

                for item in environment_sprites:

                    if i_overlap == False and ie_overlap == False: ## if there is an overlap currently happening, don't trigger these

                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height: ## check if the mouse is in the hitbox

                            if item.type == "key": ## checking the type of item to figure out what to do omg this is going to be a NIGHTMARE WITH A FULL GAME OF THESE
                                addToInventory(["key"])

                            elif item.type == "lantern": ## checking the type of item to figure out what to do
                                addToInventory(["lantern"])

                            elif item.type == "box": ## if you try to call a say screen in a python function, it'll return an error according to the tut?
                                #renpy.call("box_label")
                                characterSay(who = "Levi", what = ["It's locked. Wonder where the key is."]) ## wrapping in a list to make a distinction between ren'py say and our custom say that doesn't break the scene

                            elif item.type == "door-vines":
                                #renpy.call("doorvines_label")
                                characterSay(who = "Levi", what = ["The door is stuck behind these vines."])

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

            if item == "lantern": ## since this item has 2 states as it appears in the inventory, it's listed as a special case

                item_image = Image("dnd_test_files/Inventory Items/inventory-lantern-unlit.png") ## should be unlit as a standard, will be lit if combined with matches

            else:

                item_image = Image("dnd_test_files/Inventory Items/inventory-{}.png".format(item))

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

            if item == "lantern": ## this is pretty much just the thing we do with combined items in this house, so copy paste as needed per object

                inventory_sprites[-1].state = "unlit"

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
    image "dnd_test_files/UI/inventory-icon-bg.png" xpos 0 ypos 0.8
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

screen inspectItem(items):
    modal True
    zorder 4
    button:
        xfill True
        yfill True
        action If(len(items) > 1, true=RemoveFromSet(items, items[0]), false=[Hide("inspectItem"), If(len(dnd_dialogue) > 0, true=Show("characterSay"), false=NullAction())])
        image "dnd_test_files/Items Pop Up/items-pop-up-bg.png" align (0.5, 0.5)

        python:
            item_name = ""
            for name in inventory_item_names:
                temp_name = name.replace(" ", "-")
                if temp_name.lower() == items[0]:
                    item_name = name

        text "{}".format(item_name) size 30 align (0.5, 0.28) color "#000000"
        if items[0] == "lantern": ## friendly reminder that this is code for if an item has multiple states like lit/unlit
            $ lantern_state = inventory_sprites[inventory_items.index("lantern")].state
            image "dnd_test_files/Items Pop Up/{}-{}-pop-up.png".format("lantern", lantern_state) at two_third_size align (0.5, 0.5)
        else:
            image "dnd_test_files/Items Pop Up/{}-pop-up.png".format(items[0]) at two_third_size align (0.5, 0.5)

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

screen scene1:
    add environment_SM

## sprite transform
transform two_third_size:
    zoom 0.7

# point and click setup
label setup_scene1:
    python:
        for item in environment_items: # getting all the item info into an array FUCK arrays just DON'T touch this unless you absolutely have to
            idle_image = Image("dnd_test_files/Environment Items/{}-idle.png".format(item))
            hover_image = Image("dnd_test_files/Environment Items/{}-hover.png".format(item))
            t = Transform(child = idle_image)
            environment_sprites.append(environment_SM.create(t))
            environment_sprites[-1].type = item # -1 is the index for the last item in a list
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hover_image = hover_image

            if item == "box": ## list of properties for each object
                environment_sprites[-1].width = 126 # make sure each image has its actual width and height
                environment_sprites[-1].height = 92
                environment_sprites[-1].x = 1175 # positioning of each object in the scene
                environment_sprites[-1].y = 625

            elif item == "door-vines":
                environment_sprites[-1].width = 360
                environment_sprites[-1].height = 482
                environment_sprites[-1].x = 504
                environment_sprites[-1].y = 250

            elif item == "key":
                environment_sprites[-1].width = 81
                environment_sprites[-1].height = 44
                environment_sprites[-1].x = 1550
                environment_sprites[-1].y = 650

            elif item == "lantern":
                environment_sprites[-1].width = 98
                environment_sprites[-1].height = 144
                environment_sprites[-1].x = 1800
                environment_sprites[-1].y = 525

            renpy.retain_after_load()

    scene dnd_test_bg

    call screen scene1
