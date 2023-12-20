## dnd setup
default environment_SM = SpriteManager(event = environmentEvents) # sprite manager for shit you can pick up
default inventory_SM = SpriteManager(update = inventoryUpdate, event = inventoryEvents) # sprite manager for shit you already picked up

default environment_sprites = []
default inventory_sprites = []

default environment_items = []
default inventory_items = []

default environment_item_names = []
default inventory_item_names = ["Key", "Lantern", "Matches", "Secateur"]
default inventory_item_desc = []

default environment_items_deleted = []

default current_scene = "scene1"

default inventory_rb_enabled = False
default inventory_lb_enabled = False

default inventory_slot_size = (165, 150) ## how big are the slots (x, y)
default inventory_slot_padding = 16 ## how much space is between each slot
default inventory_first_slot_x = 480 ## where is the first slot

default dnd_dialogue = {}

default inventory_drag = False
default item_dragged = ""
default mousepos = (0.0, 0.0)

default i_overlap = False ## are inventory items overlapping with each other?
default ie_overlap = False ## are inventory items overlapping with the environment?
