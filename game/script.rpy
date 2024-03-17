# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Levi")
define t = Character("Taffy")
define d = Character("Deja")
define m = Character("Maddie")
define ta = Character("Taffy")
define mc = Character("Mortimer")
define w = Character("Waitress")

# sprites

image taffy smile = "sprites/taffy1.png"
image taffy w_smile = "sprites/taffy2.png"
image taffy worry = "sprites/taffy3.png"
image taffy pout = "sprites/taffy4.png"

image taffy investigate = "sprites/taffy_invest.png"
image maddie investigate = "sprites/maddie_invest.png"
image deja investigate = "sprites/deja_invest.png"

image bg rest = "bgs/restaurantBg.png"

image dnd_test_bg = "dnd_test_files/Scenes/dndTestBg.png"
image maddies_house = "test_case/maddie_house.png"
image maddies_backyard = "test_case/maddie_backyard.png"
image jasons_house = "test_case/jason_house.png"
image jasons_corpse = "test_case/jason_corpse.png"

default seen_deja = False
default seen_taffy = False
default seen_maddie = False

default seen_body = False

default seen_maddie_shoes = False
default seen_deja_shoes = False

default taffy_ask_jason = False
default maddie_ask_jason = False

default know_samantha = False

label start:

    $ config.after_load_callbacks = [prepareLoad]
    $ config.rollback_enabled = False # disable the ability to rollback on choices for convenience for the p&c segments
    $ quick_menu = False # hide the quick menu, will create a quick menu that works with point and click segments later

    $ is_investigating = True

    #$ environment_items = ["box", "door-vines", "key", "lantern"] # make sure these match up with the file names in the folder
    $ inventory_item_names = ["mail", "grocery_list", "black_fabric", "champagne", "body", "head", "broken_door", "security_system", "wedding_ring", "footprints", "purse", "bite", "deja", "maddie", "taffy"]
    $ environment_items = ["mail", "grocery_list", "black_fabric", "champagne", "body", "head", "broken_door", "security_system", "wedding_ring", "footprints", "purse", "bite", "deja", "maddie", "taffy"]
    $ dict_list = [mail_dict, grocery_list_dict, black_fabric_dict, champagne_dict, body_dict, head_dict, broken_door_dict, security_system_dict, wedding_ring_dict, footprints_dict, purse_dict, bite_dict, deja_bio, maddie_bio, taffy_bio]

    #show screen triangle

    #"-- Hi! Let's explain a few things before you get started. --"
    #"-- This prototype is primarily centered around deducing the relevance of evidence. --"
    #"-- There are also instances where your character, Levi, might get stressed or anxious. --"
    #"-- When this happens, try to mash a button to use body language that matches what you're saying. --"
    #"-- Q and E is smiling to show joy, W is eye contact to make other people trust you, 2 is wringing your hands out of nerves. --"
    #"-- Good luck! --"

    #"-- The way the game can tell that you reached a conclusion is by your evidence notes. --"
    #"-- It'll be a set of question marks by default, but after clicking it you can put in a deduction as to why that piece of evidence matters. --"
    #"-- It won't look like it, but you can change it again by clicking on whatever sentence you made. --"
    #"-- There are three possible conclusions, but none of them explain everything. --"
    #"-- Good luck! --"

    show screen dnd_ui # calling the ui for the inventory

    jump setup_scene_maddies_house

    #jump mash_test_start

    #jump dialogue_demo_start

    #return
