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
                                    print(item1.type + " " + item2.type) ## need to add something that makes sure the right inspect menu opens up

                                    for dict in dict_list: ## for each dictionary in the dictionary list, do a for loop for that dictionary

                                        if dict["current_item"].replace(" ", "_").lower() == item1.type: ## if the current_item.replace(" ", "_").lower() == item1.type, save it under temp_dict1
                                            temp_dict1 = dict

                                        elif dict["current_item"].replace(" ", "_").lower() == item2.type: ## repeat for temp_dict2
                                            temp_dict2 = dict

                                    if (temp_dict1["item_search"] == temp_dict2["current_item"].replace(" ", "_").lower()) or (temp_dict2["item_search"] == temp_dict1["current_item"].replace(" ", "_").lower()):

                                        i_combine = True

                                        if item1.type == temp_dict1["item_search_remove"]:
                                            removeInventoryItem(item1)

                                        else:
                                            removeInventoryItem(item2)

                                        if temp_dict1["new_state"] != "": ## change the item image to a preset item image that Will Be Added To The Dictionaries
                                            temp_dict1["item_image_inventory"] = "test_case/evidence inventory/inventory_{}_{}.png".format(item1.type, temp_dict1["new_state"])
                                            temp_dict1["item_image_inspect"] = "test_case/evidence popup/{}_{}_popup.png".format(item1.type, temp_dict1["new_state"])
                                            temp_dict1["state_changed"] = True

                                            t = Transform(child = temp_dict1["item_image_inventory"])
                                            inventory_sprites[inventory_items.index(temp_dict1["current_item"].replace(" ", "_").lower())].set_child(t)
                                            inventory_sprites[inventory_items.index(temp_dict1["current_item"].replace(" ", "_").lower())].item_image = temp_dict1["item_image_inventory"]
                                            inventory_sprites[inventory_items.index(temp_dict1["current_item"].replace(" ", "_").lower())].state = temp_dict1["new_state"]
                                            renpy.show_screen("inspectItem", [temp_dict1["current_item"].replace(" ", "_").lower()])

                                            for dict in dict_list:
                                                if dict["current_item"] == temp_dict1["current_item"]:
                                                    dict_index = dict_list.index(dict)
                                                    dict_list[dict_index] = temp_dict1
                                                elif dict["current_item"] == temp_dict2["current_item"]:
                                                    dict_index = dict_list.index(dict)
                                                    dict_list[dict_index] = temp_dict2

                                            if temp_dict1["combine_dialogue"] != []:
                                                characterSay(who = "Levi", what = temp_dict1["combine_dialogue"], inspectItem = True)

                                            elif temp_dict2["combine_dialogue"] != []:
                                                characterSay(who = "Levi", what = temp_dict2["combine_dialogue"], inspectItem = True)

                                        else:
                                            temp_dict2["item_image_inventory"] = "test_case/evidence inventory/inventory_{}_{}.png".format(item2.type, temp_dict2["new_state"])
                                            temp_dict2["item_image_inspect"] = "test_case/evidence popup/{}_{}_popup.png".format(item2.type, temp_dict2["new_state"])

                                            t = Transform(child = temp_dict2["item_image"])
                                            inventory_sprites[inventory_items.index(temp_dict2["current_item"].replace(" ", "_").lower())].set_child(t)
                                            inventory_sprites[inventory_items.index(temp_dict2["current_item"].replace(" ", "_").lower())].item_image = temp_dict2["item_image"]
                                            inventory_sprites[inventory_items.index(temp_dict2["current_item"].replace(" ", "_").lower())].state = temp_dict2["new_state"]
                                            renpy.show_screen("inspectItem", [temp_dict2["current_item"].replace(" ", "_").lower()])

                                            for dict in dict_list:
                                                if dict["current_item"] == temp_dict1["current_item"]:
                                                    dict_index = dict_list.index(dict)
                                                    dict_list[dict_index] = temp_dict1
                                                elif dict["current_item"] == temp_dict2["current_item"]:
                                                    dict_index = dict_list.index(dict)
                                                    dict_list[dict_index] = temp_dict2

                                            if temp_dict1["combine_dialogue"] != []:
                                                characterSay(who = "Levi", what = temp_dict1["combine_dialogue"], inspectItem = True)

                                            elif temp_dict2["combine_dialogue"] != []:
                                                characterSay(who = "Levi", what = temp_dict2["combine_dialogue"], inspectItem = True)

                                        inventory_SM.redraw(0) ## i think there's something wrong with this method
                                        renpy.restart_interaction()

                                        break

                                    else: ## if you combine with an incompatible object

                                        item1.x = item1.original_x
                                        item1.y = item1.original_y
                                        item1.zorder = 0

                                        characterSay(who = "Levi", what = ["...No, that's not doing anything.", "Let's try something else."])

                                        break

                            if i_combine == False: ## if items in the inventory are not being combined, then it's combining with an item in the environment
                                print("item is combining with an environment item")
                                for item3 in environment_sprites:
                                    items_overlap = checkItemsOverlap(item1, item3)

                                    if items_overlap == True:
                                        ie_overlap = True

                                        for dict in dict_list:
                                            if dict["current_item"].replace(" ", "_").lower() == item1.type:
                                                temp_dict1 = dict
                                            elif dict["current_item"].replace(" ", "_").lower() == item3.type:
                                                temp_dict3 = dict

                                        ## if item1 or item3.type is in the suspect list
                                        ## start the relevant dialogue

                                        if temp_dict1["current_item"] in evidence_options_list_b:
                                            print("item convo is being called")
                                            ie_combine = True
                                            item1.x = item1.original_x
                                            item1.y = item1.original_y
                                            item1.zorder = 0
                                            renpy.hide_screen("inventory")
                                            renpy.hide_screen("dnd_ui")
                                            renpy.call("{}_{}".format(temp_dict1["current_item"].lower(), temp_dict3["current_item"].replace(" ", "_").lower())) ## this only works for the first item picked up
                                            ## after the first item picked up, all other items hide behind the culprit when attempting to show it to them
                                            inventory_SM.redraw(0)
                                            environment_SM.redraw(0)
                                            renpy.restart_interaction()
                                            break

                                        elif temp_dict3["current_item"] in evidence_options_list_b:
                                            print("item convo is being called")
                                            ie_combine = True
                                            item1.x = item1.original_x
                                            item1.y = item1.original_y
                                            item1.zorder = 0
                                            renpy.hide_screen("inventory")
                                            renpy.hide_screen("dnd_ui")
                                            renpy.call("{}_{}".format(temp_dict3["current_item"].lower(), temp_dict1["current_item"].replace(" ", "_").lower()))
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

        if event.type == renpy.pygame_sdl2.MOUSEMOTION: ## if the event is a mouse movement/hover

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

                            ## if item.type.title() not in evidence_options_list_b addToInventory([item.type])

                            if item.type.title() not in evidence_options_list_b:

                                addToInventory([item.type])

                                for dict in dict_list:

                                    if dict["current_item"].replace(" ", "_").lower() == item.type:

                                        if dict["found_dialogue"] != []:

                                            characterSay(who = "", what = dict["found_dialogue"])

                                            break

                            else:

                                print("attempting to call intro")
                                renpy.call("{}_intro".format(item.type))

                global i_overlap, ie_overlap
                i_overlap = False
                ie_overlap = False

    def startDrag(item):

        global inventory_drag, item_dragged ## maybe get the item's index here???
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

                elif envitem.type.lower() in evidence_options_list_b:

                    print("calling intro")

                    renpy.call("{}_intro".format(envitem.type.lower()))

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

        print("removed " + item.type)

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

    def checkHerring(dict_name):
        print(dict_name["herring_action"] + " " + dict_name["herring_culprit"])
