default grocery_list_dict = {
    "current_item": "Grocery List", ## what's the name
    "action": "???", ## what did someone do to this
    "item_image_inspect": "test_case/evidence popup/grocery_list_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_grocery_list.png",
    "culprit_image": "", ## who did it (what do they look like)
    "culprit_name": "???", ## who did it (what's their FUCKEN name)
    "desc": "Found on the fridge in Maddie's house.", ## default description
    "item_search": "mail", ## what item can they wanna combine with
    "item_search_remove": "grocery_list", ## if they combine, which item is getting axed
    "new_state": "", ## after being combined, what does the non-removed item become
    "found_dialogue": [], ## when found, what does levi say
    "combine_dialogue": [], ## when combined, what does levi say
    "deduction": "", ## what's the current deduction for the item
    "herring_action": "", ## what did someone do to this evidence to make it a red herring
    "herring_culprit": "", ## who did the red herring
    "deja_statement": "", ## what does deja have to say about this item
    "maddie_statement": "", ## what does maddie have to say about this item
    "taffy_statement": "" ## what does taffy have to say about this item
}

default mail_dict = {
    "current_item": "Mail",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/mail_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_mail.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Found on a table in Maddie's house.",
    "item_search": "grocery_list",
    "item_search_remove": "grocery_list",
    "new_state": "checked",
    "found_dialogue": ["...Maddie's having an affair with Jason Hughes and wants to confront him about it?", "She's so pissed she handwrote the letter, but I wonder if it's actually her handwriting."],
    "combine_dialogue": ["Yeah, this is definitely Maddie's handwriting"],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default black_fabric_dict = {
    "current_item": "Black Fabric",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/black_fabric_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_black_fabric.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Caught on the fence in Maddie's backyard.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default champagne_dict = {
    "current_item": "Champagne",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/champagne_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_champagne.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Spilled on the floor in Maddie's house.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default body_dict = {
    "current_item": "Body",
    "action": "Why kill this girl?",
    "item_image_inspect": "test_case/evidence popup/body_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_body.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "A vampire. Already dead by the time I got there. No wedding ring.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default head_dict = {
    "current_item": "Head",
    "action": "Who killed her?",
    "item_image_inspect": "test_case/evidence popup/head_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_head.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "A vampire. Already dead by the time I got there. Pretty lady.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": ["I check the mouth out of instinct.", "She's definitely a vampire. Right down to the black blood.", "Who got my target first?"],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default broken_door_dict = {
    "current_item": "Broken Door",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/broken_door_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_broken_door.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Back door to Jason\'s. Doesn't really seem to work.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": ["I try to open the door to the backyard, but there's no use. It's jammed.", "Still, good to know."],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default security_system_dict = {
    "current_item": "Security System",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/security_system_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_security_system.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Jason\'s security system. Looks pretty old.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default wedding_ring_dict = {
    "current_item": "Wedding Ring",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/wedding_ring_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_wedding_ring.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Jason\'s wedding ring.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": ["Is it wrong to steal someone's wedding ring?", "...No. No, I don't really feel bad about it if it is."],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default footprints_dict = {
    "current_item": "Footprints",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/footprints_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_footprints.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Jason\'s, mine, and likely the victim's. Still mad I ruined these.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default purse_dict = {
    "current_item": "Purse",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/purse_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_purse.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Purse with nothing in it. Found by the victim's body.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": ["...There's nothing in this purse?"],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default bite_dict = {
    "current_item": "Bite",
    "action": "???",
    "item_image_inspect": "test_case/evidence popup/bite_popup.png",
    "item_image_inventory": "test_case/evidence inventory/inventory_bite.png",
    "culprit_image": "",
    "culprit_name": "???",
    "desc": "Jason was bitten. Looks like he gets bitten a lot.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": ["So a vampire killed him.", "I wonder if it was whoever killed the victim.", "It looks like he gets bitten a lot..."],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default deja_bio = {
    "current_item": "Deja",
    "action": "",
    "item_image": "",
    "culprit_image": "gui/profiles/deja_icon.png",
    "culprit_name": "",
    "desc": "My best friend and agent. She\'s the one who got me into vampire hunting. She\'s a bit of a gold digger and worships Mhel'kug.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default maddie_bio = {
    "current_item": "Maddie",
    "action": "",
    "item_image": "",
    "culprit_image": "gui/profiles/maddie_icon.png",
    "culprit_name": "",
    "desc": "A director I like to work with a lot from the Northeast. She can get pretty moody, but it's only because she's an artist. I think.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}

default taffy_bio = {
    "current_item": "Taffy",
    "action": "",
    "item_image": "",
    "culprit_image": "gui/profiles/taffy_icon.png",
    "culprit_name": "",
    "desc": "A writer that I may or may not heard of? He's worked with Carol on some projects, and he's a pretty big fan of mine. He seems nice.",
    "item_search": "",
    "item_search_remove": "",
    "new_state": "",
    "found_dialogue": [],
    "combine_dialogue": [],
    "deduction": "",
    "herring_action": "",
    "herring_culprit": "",
    "deja_statement": "",
    "maddie_statement": "",
    "taffy_statement": ""
}
